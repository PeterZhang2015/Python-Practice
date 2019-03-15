#!/usr/bin/python
# -*- coding: UTF-8 -*-


from ftplib import FTP
import os
import sys
import time
import socket


class FTP:
    """
        ftp downloading or uploading
    """

    def __init__(self, host, port=21):
        """ Initialize FTP client
        arguments:
                 host:ip address

                 port:port number, take 21 as default.
        """
        # print("__init__()---> host = %s ,port = %s" % (host, port))

        self.host = host
        self.port = port
        self.ftp = FTP()
        # Set ftp encoding
        self.ftp.encoding = 'utf-8'
        self.log_file = open("log.txt", "a")
        self.file_list = []

    def login(self, username, password):
        """ Login FTP server
            parameters:
                  username: username to login FTP server

                 password: password to login FTP server
            """
        try:
            timeout = 60
            socket.setdefaulttimeout(timeout)
            # 0: positive mode 1:passitive mode
            self.ftp.set_pasv(True)
            # open debug level 2，showing detail information
            # self.ftp.set_debuglevel(2)

            self.debug_print('Starting to connect %s' % self.host)
            self.ftp.connect(self.host, self.port)
            self.debug_print('Successfully connected to %s' % self.host)

            self.debug_print('Starting login to %s' % self.host)
            self.ftp.login(username, password)
            self.debug_print('Successfully login to %s' % self.host)

            self.debug_print(self.ftp.welcome)
        except Exception as err:
            self.deal_error("FTP connection or login fail, error description is：%s" % err)
            pass

    def is_same_size(self, local_file, remote_file):
        """Check whether the remote file size is the same as the local file size.

           Parameters:
             local_file: local file

             remote_file: remote file
        """
        try:
            remote_file_size = self.ftp.size(remote_file)
        except Exception as err:
            # self.debug_print("is_same_size() Error description is：%s" % err)
            remote_file_size = -1

        try:
            local_file_size = os.path.getsize(local_file)
        except Exception as err:
            # self.debug_print("is_same_size() Error description is：%s" % err)
            local_file_size = -1

        self.debug_print('local_file_size:%d  , remote_file_size:%d' % (local_file_size, remote_file_size))
        if remote_file_size == local_file_size:
            return 1
        else:
            return 0

    def download_file(self, local_file, remote_file):
        """Download file from FTP server
            Parameters:
                local_file: local file

                remote_file: remote file
        """
        self.debug_print("download_file()---> local_path = %s ,remote_path = %s" % (local_file, remote_file))

        if self.is_same_size(local_file, remote_file):
            self.debug_print('%s File size is the same，no need to download again' % local_file)
            return
        else:
            try:
                self.debug_print('>>>>>>>>>>>>Downloading file %s ... ...' % local_file)
                buf_size = 1024
                file_handler = open(local_file, 'wb')
                self.ftp.retrbinary('RETR %s' % remote_file, file_handler.write, buf_size)
                file_handler.close()
            except Exception as err:
                self.debug_print('Fail to download，error：%s ' % err)
                return

    def download_file_tree(self, local_path, remote_path):
        """Download a file tree from remote path to local path
                       Parameters:
                         local_path: local file

                         remote_path: remote file
                """
        print("download_file_tree()--->  local_path = %s ,remote_path = %s" % (local_path, remote_path))
        try:
            self.ftp.cwd(remote_path)
        except Exception as err:
            self.debug_print('remote path %s not exist, continuing...' % remote_path + " ,error：%s" % err)
            return

        if not os.path.isdir(local_path):
            self.debug_print('local path %s not exist, create local path first' % local_path)
            os.makedirs(local_path)

        self.debug_print('Switch to folder: %s' % local_path)

        self.file_list = []

        self.ftp.dir(self.get_file_list)

        remote_names = self.file_list
        self.debug_print('remote names list: %s' % remote_names)
        for item in remote_names:
            file_type = item[0]
            file_name = item[1]
            local = os.path.join(local_path, file_name)
            if file_type == 'd':
                print("download_file_tree()---> Download tree： %s" % file_name)
                self.download_file_tree(local, file_name)
            elif file_type == '-':
                print("download_file()---> Download file： %s" % file_name)
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print('Return to parent directory %s' % self.ftp.pwd())
        return True

    def upload_file(self, local_file, remote_file):
        """FTP uploading

           Parameters:
             local_path: local file

             remote_path: remote file
        """
        if not os.path.isfile(local_file):
            self.debug_print('local file %s not exist' % local_file)
            return

        if self.is_same_size(local_file, remote_file):
            self.debug_print('Skip the file with the same size: %s' % local_file)
            return

        buf_size = 1024
        file_handler = open(local_file, 'rb')
        self.ftp.storbinary('STOR %s' % remote_file, file_handler, buf_size)
        file_handler.close()
        self.debug_print('Uploading: %s' % local_file + "Successfully!")

    def upload_file_tree(self, local_path, remote_path):
        """Uploading file tree to ftp
           Parameters:

             local_path: local path

             remote_path: remote path
        """
        if not os.path.isdir(local_path):
            self.debug_print('local path %s not exist' % local_path)
            return

        self.ftp.cwd(remote_path)
        self.debug_print('Switch to remote path: %s' % self.ftp.pwd())

        local_name_list = os.listdir(local_path)
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name)
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(local_name)
                except Exception as err:
                    self.debug_print("Directory exist %s ,error：%s" % (local_name, err))
                self.debug_print("upload_file_tree()---> Uploading file tree： %s" % local_name)
                self.upload_file_tree(src, local_name)
            else:
                self.debug_print("upload_file_tree()---> Uploading file： %s" % local_name)
                self.upload_file(src, local_name)
        self.ftp.cwd("..")

    def close(self):
        """ exit ftp
        """
        self.debug_print("close()---> FTP exit")
        self.ftp.quit()
        self.log_file.close()

    def debug_print(self, s):
        """ print logs
        """
        self.write_log(s)

    def deal_error(self, e):
        """ deal errors
            Parameters：
                e：error
        """
        log_str = 'Error: %s' % e
        self.write_log(log_str)
        sys.exit()

    def write_log(self, log_str):
        """ write log
            Parameters：
                log_str：log
        """
        time_now = time.localtime()
        date_now = time.strftime('%Y-%m-%d', time_now)
        format_log_str = "%s ---> %s \n " % (date_now, log_str)
        print(format_log_str)
        self.log_file.write(format_log_str)

    def get_file_list(self, line):
        """ Get file list
            Parameters：
                line：
        """
        file_arr = self.get_file_name(line)
        # skip  . and  ..
        if file_arr[1] not in ['.', '..']:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        """ get file name
            Parameters：
                line：
        """
        pos = line.rfind(':')
        while (line[pos] != ' '):
            pos += 1
        while (line[pos] == ' '):
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr


if __name__ == "__main__":
    my_ftp = MyFTP("172.28.180.117")
    my_ftp.login("ouyangpeng", "ouyangpeng")

    # Downloading single file
    my_ftp.download_file("G:/ftp_test/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")

    # Dowloading file tree
    # my_ftp.download_file_tree("G:/ftp_test/", "App/AutoUpload/ouyangpeng/I12/")

    # Uploading single file
    # my_ftp.upload_file("G:/ftp_test/Release/XTCLauncher.apk", "/App/AutoUpload/ouyangpeng/I12/Release/XTCLauncher.apk")

    # Uploading file tree
    # my_ftp.upload_file_tree("G:/ftp_test/", "/App/AutoUpload/ouyangpeng/I12/")

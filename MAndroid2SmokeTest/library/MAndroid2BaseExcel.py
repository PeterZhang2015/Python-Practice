import json

import xlsxwriter
import os
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperateReport:
    def __init__(self, wd):
        self.wd = wd

    def summary(self, worksheet, data):
        # Set width for columns and rows
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 30)
        worksheet.set_column("C:C", 30)
        worksheet.set_column("D:D", 30)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H1.set_align("center")
        define_format_H1.set_border(1)

        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H2.set_border(1)
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:D1', 'MAndroid2 Test Report Summary', define_format_H1)
        worksheet.merge_range('A2:D2', 'Summary', define_format_H2)
        worksheet.insert_image('A1', '../resources/Matrium_Icon.png', {'x_scale': 0.45, 'y_scale': 0.15})

        _write_center_bold(worksheet, "A3", 'MAndroid2 Agent Version', self.wd)
        _write_center_bold(worksheet, "A4", 'Testing Date', self.wd)
        _write_center_bold(worksheet, "A5", 'Test Duration', self.wd)

        _write_center(worksheet, "B3", data['MAndroid2AgentVersion'], self.wd)
        _write_center(worksheet, "B4", data['testingDate'], self.wd)
        _write_center(worksheet, "B5", data['testDuration'], self.wd)

        _write_center_bold(worksheet, "C3", "Test Case Number", self.wd)
        _write_center_bold(worksheet, "C4", "Passed Number", self.wd)
        _write_center_bold(worksheet, "C5", "Failded Number", self.wd)

        _write_center(worksheet, "D3", data['sum'], self.wd)
        _write_center(worksheet, "D4", data['pass'], self.wd)
        _write_center(worksheet, "D5", data['fail'], self.wd)

        draw_statistic_pie(self.wd, worksheet)

    def detail(self, worksheet, info):
        # Set width for columns and rows
        worksheet.set_column("A:A", 20)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)
        worksheet.set_column("I:I", 20)
        worksheet.set_column("J:J", 20)

        maxRowNum = 100
        for i in range(1, maxRowNum):
            worksheet.set_row(i, 30)

        worksheet.merge_range('A1:I1', 'MAndroid2 Test Case Detail', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                    'valign': 'vcenter', 'bg_color': 'blue',
                                                                    'font_color': '#ffffff'}))

        _write_center_bold(worksheet, "A2", 'Test Case ID', self.wd)
        _write_center_bold(worksheet, "B2", 'Test Case Description', self.wd)
        _write_center_bold(worksheet, "C2", 'MO Info', self.wd)
        _write_center_bold(worksheet, "D2", 'MT Info', self.wd)
        _write_center_bold(worksheet, "E2", 'Test Parameters', self.wd)
        _write_center_bold(worksheet, "F2", 'Test Precondition', self.wd)
        _write_center_bold(worksheet, "G2", 'Test Steps', self.wd)
        _write_center_bold(worksheet, "H2", 'Check Points', self.wd)
        _write_center_bold(worksheet, "I2", 'Test Result List', self.wd)
        _write_center_bold(worksheet, "J2", 'Test Result', self.wd)

        temp = 3
        for item in info:
            print("Current item is {}".format(item))
            _write_center(worksheet, "A" + str(temp), item["TestCaseID"], self.wd)
            _write_center(worksheet, "B" + str(temp), item["Description"], self.wd)
            _write_center(worksheet, "C" + str(temp), item["moInfo"], self.wd)
            _write_center(worksheet, "D" + str(temp), item["mtInfo"], self.wd)
            _write_center(worksheet, "E" + str(temp), item["testParameters"], self.wd)
            _write_center(worksheet, "F" + str(temp), item["Preconditions"], self.wd)
            _write_center(worksheet, "G" + str(temp), item["TestSteps"], self.wd)
            _write_center(worksheet, "H" + str(temp), item["CheckPoints"], self.wd)
            _write_center(worksheet, "I" + str(temp), item["testResultList"], self.wd)
            _write_center(worksheet, "J" + str(temp), item["testResult"], self.wd)

           # _write_center(worksheet, "L" + str(temp), "", self.wd)
            temp = temp + 1

    def close(self):
        self.wd.close()


def get_format(wd, option={}):
    return wd.add_format(option)


# def link_format(wd):
#     red_format = wd.add_format({
#         'font_color': 'red',
#         'bold': 1,
#         'underline': 1,
#         'font_size': 12,
#     })

def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})


def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)


def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


def get_format_center_bold(wd, num=1):
    return wd.add_format({'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': num})


def _write_center_bold(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center_bold(wd))


def set_row(worksheet, num, height):
    worksheet.set_row(num, height)


def draw_statistic_pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
        'name': 'Test Automation Statistics',
        'categories': '=TestSummary!$C$4:$C$5',
        'values': '=TestSummary!$D$4:$D$5',
    })
    chart1.set_title({'name': 'Test Statistics'})
    chart1.set_style(10)
    worksheet.insert_chart('A7', chart1, {'x_offset': 25, 'y_offset': 10})


if __name__ == '__main__':
    sum = {'MAndroid2AgentVersion': '36', 'testingDate': '2020-04-28 15:26:49', 'testDuration': '25 S',
           'pass': 5, 'sum': 7, 'pass': 5, 'fail': 2}

    moInfo = {"IMSI": "505025104559746", "MSISDN": "+61418673947", "handsetID": "mcloud.matrium.com.au:7541",
              "versions": {"MAndroid2": "2.20.41Build2020-04-08_18:06:26", "MAndroid2Agent": "2.19.33Build2020-03-27_04:28:38",
                           "MAndroid2Plugin": "2.19.17Build2020-03-30_03:13:15"}}
    mtInfo = {"IMSI": "505025703492762", "MSISDN": "+61402537622", "handsetID": "mcloud.matrium.com.au:7569",
              "versions": {"MAndroid2": "2.20.41Build2020-04-08_16:08:09", "MAndroid2Agent": "2.19.33Build2020-03-27_04:28:38",
                  "MAndroid2Plugin": "2.19.17Build2020-03-30_03:13:15"}}
    testParameters = {"VoiceCall": {"Duration": 2}}

    info = [{"TestCaseID": 1, "Description": "Basic voice call.", "moInfo": json.dumps(moInfo), "mtInfo": json.dumps(mtInfo),
             "testParameters": json.dumps(testParameters), "Preconditions": "None", "TestSteps": "1.Place voice call", "CheckPoints": "none",
             "testResult": "Passed"},
            {"TestCaseID": 2, "Description": "SMS.", "moInfo": json.dumps(mtInfo), "mtInfo": json.dumps(moInfo),
             "testParameters": json.dumps(testParameters), "Preconditions": "None", "TestSteps": "1.Send SMS.", "CheckPoints": "none",
             "testResult": "Passed"}]

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    # reportFileName = "MAndroid2TestReport_{}.xlsx".format(ts)
    reportFileName = "MAndroid2Report.xlsx"

    workbook = xlsxwriter.Workbook(reportFileName)
    worksheet = workbook.add_worksheet("TestSummary")
    worksheet2 = workbook.add_worksheet("TestDetail")
    bc = OperateReport(wd=workbook)

    bc.summary(worksheet, sum)
    bc.detail(worksheet2, info)
    bc.close()
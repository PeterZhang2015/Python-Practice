import xlsxwriter
import os
from datetime import datetime

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperateReport:
    def __init__(self, wd):
        self.wd = wd

    def summary(self, worksheet, data, devices):
        # Set width for columns and rows
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)
        worksheet.set_row(8, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:E1', 'Test Report Summary', define_format_H1)
        worksheet.merge_range('A2:E2', 'Summary', define_format_H2)

        worksheet.insert_image('A1', 'Telstra_Icon.png', {'x_scale': 1, 'y_scale': 0.63})

        _write_center_bold(worksheet, "A3", 'Version Code', self.wd)
        _write_center_bold(worksheet, "A4", 'Version Name', self.wd)
        _write_center_bold(worksheet, "A5", 'Packing Time', self.wd)
        _write_center_bold(worksheet, "A6", 'Testing Date', self.wd)

        _write_center(worksheet, "B3", data['versionCode'], self.wd)
        _write_center(worksheet, "B4", data['versionName'], self.wd)
        _write_center(worksheet, "B5", data['packingTime'], self.wd)
        _write_center(worksheet, "B6", data['testDate'], self.wd)

        _write_center_bold(worksheet, "C3", "Test Case Number", self.wd)
        _write_center_bold(worksheet, "C4", "Passed Number", self.wd)
        _write_center_bold(worksheet, "C5", "Failded Number", self.wd)
        _write_center_bold(worksheet, "C6", "Test Duration", self.wd)

        # data1 = {"test_sum": 100, "test_success": 80, "test_failed": 20, "test_date": "2018-10-10 12:10"}
        _write_center(worksheet, "D3", data['sum'], self.wd)
        _write_center(worksheet, "D4", data['pass'], self.wd)
        _write_center(worksheet, "D5", data['fail'], self.wd)
        _write_center(worksheet, "D6", data['testSumDate'], self.wd)

        _write_center_bold(worksheet, "E3", "Testing Tool", self.wd)

        worksheet.merge_range('E4:E6', 'appium1.7+python3', get_format_center(self.wd))
        _write_center_bold(worksheet, "A8", 'Device Type', self.wd)
        _write_center_bold(worksheet, "B8", 'Passed', self.wd)
        _write_center_bold(worksheet, "C8", 'Failed', self.wd)

        temp = 9
        for item in devices:
            _write_center(worksheet, "A%s" % temp, item["phone_name"], self.wd)
            _write_center(worksheet, "B%s" % temp, item["pass"], self.wd)
            _write_center(worksheet, "C%s" % temp, item["fail"], self.wd)
            temp = temp + 1

        draw_statistic_pie(self.wd, worksheet)

    def detail(self, worksheet, info):
        # Set width for columns and rows
        worksheet.set_column("A:A", 30)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)
        worksheet.set_column("I:I", 20)
        worksheet.set_column("J:J", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)
        worksheet.set_row(5, 30)
        worksheet.set_row(6, 30)
        worksheet.set_row(7, 30)
        worksheet.set_row(8, 30)
        worksheet.set_row(9, 30)
        worksheet.set_row(10, 30)

        worksheet.merge_range('A1:J1', 'Test Case Detail', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                    'valign': 'vcenter', 'bg_color': 'blue',
                                                                    'font_color': '#ffffff'}))
        _write_center_bold(worksheet, "A2", 'Device Type', self.wd)
        _write_center_bold(worksheet, "B2", 'Test Case ID', self.wd)
        _write_center_bold(worksheet, "C2", 'Test Case Introduction', self.wd)
        _write_center_bold(worksheet, "D2", 'Test case function', self.wd)
        _write_center_bold(worksheet, "E2", 'Test Pre-condition', self.wd)
        _write_center_bold(worksheet, "F2", 'Teset Steps', self.wd)
        _write_center_bold(worksheet, "G2", 'Check Point', self.wd)
        _write_center_bold(worksheet, "H2", 'Test Result', self.wd)
        _write_center_bold(worksheet, "I2", 'Note', self.wd)
        _write_center_bold(worksheet, "J2", 'Screenshot', self.wd)

        temp = 3
        for item in info:
            # print(item)
            _write_center(worksheet, "A" + str(temp), item["phoneName"], self.wd)
            _write_center(worksheet, "B" + str(temp), item["id"], self.wd)
            _write_center(worksheet, "C" + str(temp), item["title"], self.wd)
            _write_center(worksheet, "D" + str(temp), item["caseName"], self.wd)
            _write_center(worksheet, "E" + str(temp), item["info"], self.wd)
            _write_center(worksheet, "F" + str(temp), item["step"], self.wd)
            _write_center(worksheet, "G" + str(temp), item["checkStep"], self.wd)
            _write_center(worksheet, "H" + str(temp), item["result"], self.wd)
            _write_center(worksheet, "I" + str(temp), item.get("msg", ""), self.wd)
            if item.get("img", "false") == "false":
                _write_center(worksheet, "J" + str(temp), "", self.wd)
                worksheet.set_row(temp, 30)
            else:
                worksheet.insert_image('J' + str(temp), item["img"],
                                       {'x_scale': 0.18, 'y_scale': 0.18, 'border': 1})
                worksheet.set_row(temp - 1, 110)
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
        'name': 'Test automation statistics',
        'categories': '=TestSummary!$C$4:$C$5',
        'values': '=TestSummary!$D$4:$D$5',
    })
    chart1.set_title({'name': 'Test Statistics'})
    chart1.set_style(10)
    worksheet.insert_chart('D8', chart1, {'x_offset': 25, 'y_offset': 10})


if __name__ == '__main__':
    sum = {'testSumDate': '25 s', 'sum': 10, 'pass': 5, 'testDate': '2017-06-05 15:26:49', 'fail': 5,
           'appVersion': '17051515', 'appSize': '4.57M', 'appName': 'MAndorid2',
           'versionCode': '2.0', 'versionName': 'release', 'packingTime': '30102019', 'testDate': '30102019'}

    info = [{"id": 1, "title": "firstOpen", "caseName": "testf01", "result": "Passed", "img": "C:\\Temp\\screen_shot\\IR60.3.1_MS1(a)_calls_a_local_number_06-16-2018_13-23-34.png", "phoneName": "SAMSUNG S7", "info": "None", "step": "None", "checkStep": "None", "result": "Passed"},
            {"id": 1, "title": "firstOpen",
             "caseName": "testf01", "result": "Passed", "img": "C:\\Temp\\screen_shot\\IR60.2.2_Account_enquiry_via_USSD_06-16-2018_12-22-47.png", "phoneName": "SAMSUNG S8", "info": "None", "step": "None", "checkStep": "None", "result": "Passed"}]

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    # reportFileName = "MAndroid2TestReport_{}.xlsx".format(ts)
    reportFileName = "Report.xlsx"

    workbook = xlsxwriter.Workbook(reportFileName)
    worksheet = workbook.add_worksheet("TestSummary")
    worksheet2 = workbook.add_worksheet("TestDetail")
    bc = OperateReport(wd=workbook)

    devices = [{"phone_name": "SUMSANG S7", "pass": "1", "fail": "0"}]

    bc.summary(worksheet, sum, devices)
    bc.detail(worksheet2, info)
    bc.close()
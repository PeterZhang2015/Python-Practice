import os
import pytest

@pytest.mark.test

def test_expectedPassResult():
    expected_result = {}
    expected_result["1"] = {}
    expected_result["2"] = {}
    expected_result["1"]["expected_result"] = "The eBGP neighbor should form properly between the MRS_1 and PE routers"
    expected_result["1"]["result"] = "Passed"
    expected_result["2"]["expected_result"] = "Routes with the appropriate Autonomous System (AS) path attribute should be seen on the PE BGP routing table"
    expected_result["2"]["result"] = "Passed"
    print (expected_result)

    assert (expected_result["2"]["result"] == "Passed")

def test_expectedErrorResult():
    expected_result = {}
    expected_result["1"] = {}
    expected_result["2"] = {}
    expected_result["1"]["expected_result"] = "The eBGP neighbor should form properly between the MRS_1 and PE routers"
    expected_result["1"]["result"] = "Passed"
    expected_result["2"]["expected_result"] = "Routes with the appropriate Autonomous System (AS) path attribute should be seen on the PE BGP routing table"
    expected_result["2"]["result"] = "Passed"
    print (expected_result)

    assert (expected_result["2"]["result"] == "Failed")

if __name__ == '__main__':
    generateReportCommand = "pytest --reruns 3 --reruns-delay 1 -m 'test' -q -r test_Temp2.py"
    print(generateReportCommand)
    output3 = os.system(generateReportCommand)
    print(output3)



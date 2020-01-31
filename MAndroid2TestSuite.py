import os
import unittest
import HTMLTestRunner
from MAndroid2TestCases import MAndroid2TestCases

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


if __name__ == '__main__':
    testIMSI = '505025504563848'
    # testIMSI = 'ce071607a2e74a1a05'

    # Add test cases to test suite.
    suite = unittest.TestSuite()
    suite.addTest(MAndroid2TestCases('test_MAndroid2_Relogin', testIMSI))
#    suite.addTest(MAndroid2TestCases.MAndroid2TestCases('getDesiredCaps', testIMSI))

    # # Run test suite directly.
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # # Run test suite and generate txt report.
    # with open('MAndroid2UnittestTextReport.txt', 'a') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
    #     runner.run(suite)

    # Run test suite and generate HTML report.
    with open('MAndroid2HTMLReport.html', 'w') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
                    stream=f,
                    title='MAndroid2 Test Report',
                    description='MAndroid2 relogin automated by appium.'
                    )
        runner.run(suite)
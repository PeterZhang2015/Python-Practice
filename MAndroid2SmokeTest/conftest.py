import logging
import sys
from os import listdir

import pytest

from pytest_reportportal import RPLogger, RPLogHandler

from MAndroid2SmokeTest.library.MAndroid2BaseYaml import getYam
from MCloud import MCloudControl


@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger

@pytest.fixture(scope="session")
def setupMOMT(testEnvironment, testUsers):
    # Connect available test handset on mcloud from specified IMSI.
    mcloud = MCloudControl()

    # Set test environment variables.
    mcloud.mcloudBaseUrl = testEnvironment['MCloud']['baseUrl']
    mcloud.mcloudLoginUser = testEnvironment['Login']['User']
    mcloud.mcloudLoginToken = testEnvironment['Login']['accessToken']

    testUsers['MO']['handsetID'] = mcloud.connectToMcloudUser(testUsers['MO']['IMSI'])
    print("MO Handset ID is {}".format(testUsers['MO']['handsetID']))

    testUsers['MT']['handsetID'] = mcloud.connectToMcloudUser(testUsers['MT']['IMSI'])
    print("MT Handset ID is {}".format(testUsers['MT']['handsetID']))
    return testUsers





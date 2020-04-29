import pytest


@pytest.fixture(scope='class')
def api(request):
    print("Setup")
    yield
    print("TearDown")

class TestLogin(object):

    tempList = [1, 3, 5]


    def test_login_001(self,api):
        assert  1==1
    def test_login_002(self):
        assert  1==1


if __name__ == "__main__":
    pytest.main([__file__])
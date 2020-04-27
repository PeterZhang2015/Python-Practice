import pytest

class TimeLine:
    def __init__(self, instances):
        self.instances = instances

@pytest.fixture
def timeline(request):
    print("Current request.param is {}".format(request.param))
    return TimeLine(request.param)

@pytest.mark.parametrize(
    'input',
    ([1, 2, 3], [2, 4, 6], [6, 8, 10]),
    indirect=True
)
def test_timeline(timeline):
    print("Current timeline is {}".format(timeline))
    for instance in timeline.instances:
        print ("Current instance is {}".format(instance))
        assert instance % 2 == 0

if __name__ == "__main__":
    pytest.main([__file__])
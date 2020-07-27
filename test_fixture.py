import pytest

@pytest.fixture
def numbers():
    l=[10,20,30]
    return l
@pytest.mark.skip
def test_method1(numbers):
    assert numbers[0]==10

@pytest.mark.xfail
def test_method2(numbers):
    assert numbers[2]==1

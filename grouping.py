import pytest

class TestClass:
    def test_one(self):
        x="Nia"
        assert 'N' in x

    def test_two(self):
        x='Namazi'
        assert hasattr(x,"Nama")

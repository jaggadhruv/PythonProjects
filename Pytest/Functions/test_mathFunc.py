from Functions import mathFunc
import pytest
print("This is unit test script of matchFunc Script")


@pytest.mark.number
def test_add_two_num():
    assert mathFunc.add_two_num(5, 5) == 10
    assert mathFunc.add_two_num(5) == 5


@pytest.mark.number
def test_mul_two_num():
    assert mathFunc.mul_two_num(5, 2) == 10
    assert mathFunc.mul_two_num() == 1
    # Failed test case
    # assert mathFunc.mul_two_num(3) == 4


@pytest.mark.string
def test_add_string():
    result = mathFunc.add_string("Hello", "World")
    assert type(result) is str
    assert " " in result


@pytest.mark.string
def test_mul_string():
    result = mathFunc.mul_string("Hello", 4)
    assert result == "Hello"*4
    assert type(result) is str
    assert "Hello" in result

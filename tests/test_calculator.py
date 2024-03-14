import pytest
import src.calculator.calculator as calculator

@pytest.mark.parametrize(
    "input, expected",
    {
        pytest.param(5, 25, id="Square for 5"),
        pytest.param(10, 100, id="Square for 10"),
        pytest.param(15, 225, id="Square for 15"),
    }
)
def test_squareNums(input, expected):
    """Tests the squareNums function"""
    assert calculator.squareNums(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    {
        pytest.param(5, 15, id="Tri for 5"),
        pytest.param(10, 55, id="Tri for 10"),
        pytest.param(15, 120, id="Tri for 15"),
    }
)
def test_triNums(input, expected):
    """Tests the triNums function"""
    assert calculator.triNums(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    {
        pytest.param(5, 16, id="Lazy caterer for 5"),
        pytest.param(10, 56, id="Lazy caterer for 10"),
        pytest.param(15, 121, id="Lazy caterer for 15"),
    }
)
def test_lazyCaterer(input, expected):
    """Tests the lazyCaterer function"""
    assert calculator.lazyCaterer(input) == expected


@pytest.mark.parametrize(
    "input, expected",
    {
        pytest.param(5, 65, id="Magic squares for 5"),
        pytest.param(0, 0, id="Magic squares for 0"),
        pytest.param(-5, -65, id="Magic squares for -5"),
    }
)
def test_magicSquares(input, expected):
    """Tests the magicSquares function"""
    assert calculator.magicSquares(input) == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    {
        pytest.param(5, 5, 10, id="Add 5 and 5"),
        pytest.param(10, 10, 20, id="Add 10 and 10"),
        pytest.param(15, 15, 30, id="Add 15 and 15"),
    }
)
def test_add(input1, input2, expected):
    """Tests the add function"""
    assert calculator.add(input1, input2) == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    {
        pytest.param(5, 5, 25, id="Multiply 5 and 5"),
        pytest.param(10, 10, 100, id="Multiply 10 and 10"),
        pytest.param(15, 15, 225, id="Multiply 15 and 15"),
    }
)
def test_multiply(input1, input2, expected):
    """Tests the multiply function"""
    assert calculator.multiply(input1, input2) == expected


@pytest.mark.parametrize(
    "input1, input2, expected",
    {
        pytest.param(5, 5, 7.0710678118654755, id="Hypotenuse for 5 and 5"),
        pytest.param(10, 10, 14.142135623730951, id="Hypotenuse for 10 and 10"),
        pytest.param(15, 15, 21.213203435596427, id="Hypotenuse for 15 and 15"),
    }
)
def test_hypotenuse(input1, input2, expected):
    """Tests the hypotenuse function"""
    assert calculator.hypotenuse(input1, input2) == expected


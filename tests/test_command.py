"""Testing menu driven calculator commands"""
import pytest
from calculator.__init__ import CommandProcessor

def test_add_command():
    """testing add command"""
    processor = CommandProcessor()
    assert processor.execute_command('add', 1, 2, 3) == 6

def test_subtract_command():
    """testing subtract command"""
    processor = CommandProcessor()
    assert processor.execute_command('subtract', 10, 5, 2) == 3

def test_multiply_command():
    """testing multiply command"""
    processor = CommandProcessor()
    assert processor.execute_command('multiply', 2, 3, 4) == 24

def test_divide_command():
    """testing divide command"""
    processor = CommandProcessor()
    assert processor.execute_command('divide', 8, 2, 2) == 2

def test_invalid_command():
    """testing invalid command"""
    processor = CommandProcessor()
    with pytest.raises(ValueError):
        processor.execute_command('invalid', 1, 2)

def test_divide_by_zero():
    """testing divide by zero"""
    processor = CommandProcessor()
    with pytest.raises(ZeroDivisionError):
        processor.execute_command('divide', 8, 0)

# Additional tests for edge cases
def test_subtract_negative_result():
    """testing subtract of negative result"""
    processor = CommandProcessor()
    assert processor.execute_command('subtract', 5, 10) == -5

def test_multiply_with_zero():
    """testing multiply with zero"""
    processor = CommandProcessor()
    assert processor.execute_command('multiply', 0, 5) == 0

if __name__ == "__main__":
    pytest.main()

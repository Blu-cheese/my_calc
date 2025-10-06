"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, multiply, subtract,power ,square

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-2, -3) == -5
        assert add(-10, 15) == 5

class TestmultiplyDivide:
    """Test multiplication and division"""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(5, 3) == 15
        assert multiply(7, 6) == 42
    
    def test_multiply_zeros(self):
        """Test multiplying positive numbers"""
        assert multiply(5, 0) == 0
        assert multiply(7, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying positive numbers"""
        assert multiply(5, -3) == -15
        assert multiply(-7, -6) == 42

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
    
    def test_divide_negative_numbers(self):
        """Test dividing positive numbers"""
        assert divide(10, -2) == -5
        assert divide(-9, -3) == 3
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
class TestPowerSquare:
    """Test power and square functions"""
    
    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
        assert power(5, 0) == 1
    
    def test_power_negative_exponent(self):
        """Test power with negative exponent"""
        assert power(2, -2) == 0.25
        assert power(5, -1) == 0.2

    def test_square_positive_number(self):
        """Test square of a positive number"""
        assert square(4) == 16
        assert square(7) == 49
    
    def test_square_negative_number(self):
        """Test square of a negative number"""
        assert square(-4) == 16
        assert square(-7) == 49
# class TestMultiplyDivideWithValidation:
#     """Test multiplication and division with input validation."""
    
#     def test_multiply_input_validation(self):
#         """Test multiply rejects non-numeric inputs."""
#         with pytest.raises(TypeError, match="Both arguments must be numbers"):
#             multiply("5", 3)
#         with pytest.raises(TypeError, match="Both arguments must be numbers"):
#             multiply(5, "3")
    
#     def test_divide_input_validation(self):
#         """Test divide rejects non-numeric inputs."""
#         with pytest.raises(TypeError, match="Division requires numeric inputs"):
#             divide("10", 2)

# TODO: Students will add TestMultiplyDivide class
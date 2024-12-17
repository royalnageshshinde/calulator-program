# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test Cases

def test_add():
    assert add(2, 3) == 5, "Test case failed for addition"
    assert add(-1, 1) == 0, "Test case failed for addition with negative number"
    assert add(0, 0) == 0, "Test case failed for addition with zeros"
    print("All addition tests passed!")

def test_subtract():
    assert subtract(5, 3) == 2, "Test case failed for subtraction"
    assert subtract(3, 5) == -2, "Test case failed for subtraction with result negative"
    assert subtract(0, 0) == 0, "Test case failed for subtraction with zeros"
    print("All subtraction tests passed!")

def test_multiply():
    assert multiply(2, 3) == 6, "Test case failed for multiplication"
    assert multiply(-2, 3) == -6, "Test case failed for multiplication with negative number"
    assert multiply(0, 100) == 0, "Test case failed for multiplication with zero"
    print("All multiplication tests passed!")

def test_divide():
    assert divide(6, 2) == 3, "Test case failed for division"
    assert divide(-6, 2) == -3, "Test case failed for division with negative number"
    assert divide(5, 2) == 2.5, "Test case failed for division with floating point result"
    
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero", "Test case failed for division by zero"
        print("Caught division by zero correctly")
    else:
        print("Test failed for division by zero")

    print("All division tests passed!")


# Main function to run all tests
def run_tests():
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

if __name__ == "__main__":
    run_tests()

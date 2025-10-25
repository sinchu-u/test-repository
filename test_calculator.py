from calculator import add_numbers, multiply_numbers

def test_add_positive_numbers():
    assert add_numbers(3, 5) == 8, "Має бути 8"

def test_add_negative_numbers():
    assert add_numbers(-2, -4) == -6, "Має бути -6"

def test_multiply_positive_numbers():
    assert multiply_numbers(8, 3) == 24, "Має бути 24"

def test_multiply_negative_numbers():
    assert multiply_numbers(-5, -4) == 20, "Має бути 20"

def test_multiply_negative_and_positive_numbers():
    assert multiply_numbers(-2, 7) == -14, "Має бути -14"

if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    test_multiply_positive_numbers()
    test_multiply_negative_numbers()
    test_multiply_negative_and_positive_numbers()
    print("Усі тести пройдено успішно!")
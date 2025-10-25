from calculator import add_numbers

def test_add_positive_numbers():
    assert add_numbers(3, 5) == 8, "Має бути 8"

def test_add_negative_numbers():
    assert add_numbers(-2, -4) == -6, "Має бути -6"

if __name__ == "__main__":
    test_add_positive_numbers()
    test_add_negative_numbers()
    print("Усі тести пройдено успішно!")
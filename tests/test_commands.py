from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


# Test for AddCommand
def test_add():
    add_cmd = AddCommand()
    assert add_cmd.execute(3, 2) == 5
    assert add_cmd.execute(-1, 5) == 4


# Test for SubtractCommand
def test_subtract():
    sub_cmd = SubtractCommand()
    assert sub_cmd.execute(10, 3) == 7
    assert sub_cmd.execute(0, 5) == -5


# Test for MultiplyCommand
def test_multiply():
    mul_cmd = MultiplyCommand()
    assert mul_cmd.execute(4, 5) == 20
    assert mul_cmd.execute(0, 10) == 0


# Test for DivideCommand
def test_divide():
    div_cmd = DivideCommand()
    assert div_cmd.execute(10, 2) == 5
    assert div_cmd.execute(5, 0) == "Error: Division by zero is not allowed"


# Run the tests
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests passed!")

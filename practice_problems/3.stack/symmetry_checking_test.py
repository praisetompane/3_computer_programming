from symmetry_checking import SymmetryChecker

def main():
    symmetry_checker = SymmetryChecker()
    valid_code = '(){()[]{()[]}}'
    print("valid code")
    assert(symmetry_checker.lint(valid_code))

    invalid_code = '[]){()[]{()[]}}'
    print("invalid code - expect Exception('Stack is empty')")
    assert(symmetry_checker.lint(invalid_code))

if __name__ == "__main__":
    main()
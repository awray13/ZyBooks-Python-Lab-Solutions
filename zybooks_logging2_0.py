def validate_grades(grades):
    """Validates the list of grades and ensures all conditions are met."""
    assert all(0 <= grade <= 100 for grade in grades), "One of the grades is wrong"
    assert sum(grades) <= 100, "Sum of grades exceeds 100"

def main():
    # Accept input for the four grades
    try:
        grades = list(map(int, input("Enter four grades separated by commas: ").split(',')))
        assert len(grades) == 4, "Exactly four grades are required"

        # Validate the grades
        validate_grades(grades)

        # If valid, print the sum of the grades
        print(sum(grades))
    except AssertionError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter four integers separated by commas.")

# Entry point for the program
if __name__ == "__main__":
    main()



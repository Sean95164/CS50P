from validator_collection import validators, errors

def main():
    print(is_valid(input("What's your email address? ")))

def is_valid(s):
    try:
        validators.email(s)
        return "Valid"
    except (errors.InvalidEmailError,errors.EmptyValueError):
        return "Invalid"

if __name__ == "__main__":
    main()

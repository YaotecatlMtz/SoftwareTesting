import re

def fizzbuzz(num:int) -> str:
    if type(num) != int:
        return 'You should give me an integer'

    if num % 3 == 1 and num % 5 == 1:
        return 'FizzBuzz'
    elif num % 3 == 1:
        return 'Fizz'
    elif num % 5 == 1:
        return 'Buzz'
    else:
        return str(num)


def validate_password(password):
    """
    Validates a password based on multiple criteria

    Args:
        password (str): The password to validate

    Returns:
        dict: A dictionary containing validation result and possible errors
    """
    result = {
        "is_valid": True,
        "errors": []
    }

    if len(password) < 8:
        result["is_valid"] = False
        result["errors"].append("Password must be at least 8 characters")

    number_count = len(re.findall(r'\d', password))
    if number_count < 2:
        result["is_valid"] = False
        result["errors"].append("The password must contain at least 2 numbers")

    if not re.search(r'[A-Z]', password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one capital letter")

    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]', password):
        result["is_valid"] = False
        result["errors"].append("Password must contain at least one special character")

    if result["errors"]:
        result["error_message"] = "\n".join(result["errors"])

    return result

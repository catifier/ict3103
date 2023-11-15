from markupsafe import escape


def validate(text):
    escaped = escape(text)
    if escaped == text:
        return [escaped, True]
    else:
        return [escaped, False]


def validate_addition(number1, number2):
    result = 0
    escaped1 = escape(number1)
    escaped2 = escape(number2)
    if escaped1 == number1 and escaped2 == number2:
        if escaped1.isnumeric() and escaped2.isnumeric():
            result = int(escaped1) + int(escaped2)
            return [str(result), True]
        else:
            return [str(result), False]
    else:
        return [str(result), False]
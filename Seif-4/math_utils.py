# פונקציה שבודקת אם מספר אחד הוא מכפלה של השני
def check_if_multiple(a, b):
    return a % b == 0 or b % a == 0
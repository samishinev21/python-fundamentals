grade_str = input()

def grades(grade):
    if grade >= 2.00 and grade <= 2.99:
        print("Fail")
    elif grade >= 3.00 and grade <= 3.49:
        print("Poor")
    elif grade >= 3.50 and grade <= 4.49:
        print("Good")
    elif grade >= 4.50 and grade <= 5.49:
        print("Very Good")
    elif grade >= 5.50 and grade <= 6.00:
        print("Excellent")

grades(float(grade_str))
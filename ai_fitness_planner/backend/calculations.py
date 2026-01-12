# backend/calculations.py
def calculate_bmi(weight, height):
    """
    Safe BMI calculation
    weight: kg
    height: cm
    """
    if height is None or height <= 0:
        return None
    if weight is None or weight <= 0:
        return None
    return weight / ((height / 100) ** 2)


def calculate_bmr(gender, weight, height, age):
    """
    Mifflin-St Jeor Formula
    """
    if gender == "Male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161




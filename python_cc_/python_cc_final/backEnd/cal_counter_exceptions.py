class BigMealException(Exception):
    """
    Raised when a meal exceeds the maximum calorie limit.
    """

    def __init__(self, calories):
        message = f"Meal has {calories} calories, which exceeds the maximum limit!"
        super().__init__(message)


class InvalidMealException(Exception):
    """
    Raised when an invalid meal item is encountered.
    """

    def __init__(self, item):
        message = f"Meal item {item} is invalid!"
        super().__init__(message)

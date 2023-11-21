import json
import datetime
from backEnd.exceptions import BigMealException, InvalidMealException
from backEnd.jsonUtils import comp_cal_counter_json, price_counter_json

# Load meals and combos data from JSON files
with open("data/meals.json") as file:
    meals_json = json.load(file)["meals"]

with open("data/combos.json") as file:
    combos_json = json.load(file)["combos"]

# Create dictionaries for quick access to meals and combos by id and name
meal_dict_by_id = {meal["id"]: meal for meal in meals_json}
meal_dict_by_name = {meal["name"]: meal for meal in meals_json}
combo_dict_by_id = {combo["id"]: combo for combo in combos_json}
combo_dict_by_name = {combo["name"]: combo for combo in combos_json}


class Order:
    """
    This class represents an order.

    Arguments:
        items (list): A list of item ids.
        date (datetime): The date and time of the order.

    Class attributes:
        counter (int): A counter for the number of orders.

    Attributes:
        order_id (str): A unique identifier for the order.
        order_accepted (bool): Whether or not the order was accepted.
        order_refused_reason (str): The reason the order was refused.
        date (datetime): The date and time of the order.
        items (list): A list of item ids.

    Properties:
        calories (int): The total calories for the order.
        price (int): The total price for the order.
    """

    counter = 1

    def __init__(self, items, date=None):
        self.order_id = f"order-{Order.counter}"
        Order.counter += 1
        self.items = items
        self._calories = None
        self._price = None
        self.order_accepted = False
        self.order_refused_reason = None

        if date is None:
            self.date = datetime.date.today()
        else:
            self.date = datetime.datetime.strptime(date, "%d-%b-%Y")

        try:
            self.calories
            self.price
        except (BigMealException, InvalidMealException) as e:
            self._calories = 0
            self._price = 0
            self.order_refused_reason = str(e)
        else:
            self.order_accepted = True
            self.order_refused_reason = None

    @property
    def calories(self):
        if self._calories is None:
            self._calories = comp_cal_counter_json(*self.items)
        return self._calories

    @property
    def price(self):
        if self._price is None:
            self._price = price_counter_json(*self.items)
        return self._price

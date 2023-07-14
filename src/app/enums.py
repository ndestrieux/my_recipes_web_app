from enum import Enum


class LanguageChoice(Enum):
    EN = "English"
    FR = "Français"
    PL = "Polski"


class VoteChoice(Enum):
    UP = "Up"
    DOWN = "Down"


class UnitChoice(Enum):
    ml = "milliliter"
    l = "liter"
    tsp = "teaspoon"
    tbsp = "tablespoon"
    mg = "milligram"
    g = "gram"
    kg = "kilogram"
    lb = "pound"
    oz = "ounce"
    piece = "piece"


class CategoryChoice(Enum):
    breakfast = "breakfast"
    lunch = "lunch"
    dinner = "dinner"
    dessert = "dessert"
    drink = "drink"
    appetizer = "appetizer"
    bakery = "bakery"


class MailTypeChoice(Enum):
    RECIPE_SHARING = "Recipe sharing"
    PASSWORD_RESET = "Password reset"

"""
easy_converter is built to simplify different types of conversions
"""

from datetime import timedelta


def seconds_to_hh_mm_ss(seconds: int):
    """
    Returns seconds in HH:MM:SS format.

    Arguments:
        seconds (int) -- number of seconds to convert

    Example:
        seconds_to_hh_mm_ss(90)
        (00:01:30)
    """
    return str(timedelta(seconds=seconds))


def km_to_mile(km: float):
    """
    Converts kilometers to miles. Returns miles as a float.

    Arguments:
        km (float) -- kilometers

    Example:
        km_to_mile(100)
        (62.13)
    """
    return float(f"{km * 0.621371:.2f}")


def miles_to_km(miles: float):
    """
        Converts miles to kilometers. Returns kilometers as a float.

        Arguments:
            miles (float) -- miles

        Example:
            miles_to_km(100)
            (160.93)
    """
    return float(f"{miles * 1.60934:.2f}")


def fluid_oz_to_ml(oz: float, standard = 'us'):
    """
    Converts fluid ounces to milliliters. Returns milliliters as a float.

    :param:
        oz (float) -- fluid ounces
        standard -- us or uk

    Example:
        standard = 'us'
        fluid_oz_to_ml(1)
        (29.6)
        standard = 'uk'
        fluid_oz_to_ml(1)
        (28.4)

    """
    match standard:
        case "uk":
            return float(f"{oz * 28.4:.2f}")
        case "us":
            return float(f"{oz * 29.6:.2f}")
    return None


def ml_to_fluid_oz(milliliters: float, standard = 'us'):
    """
        Converts milliliters to fluid ounces. Returns fluid ounces as a float.

        :param:
            milliliters (float) -- milliliters
            standard -- us or uk

        Example:
            standard = 'us'
            ml_to_fluid_oz(1)
            (0.03)
            standard = 'uk'
            ml_to_fluid_oz(1)
            (0.04)

        """
    match standard:
        case "uk":
            return float(f"{milliliters * 0.035:.2f}")
        case "us":
            return float(f"{milliliters * 0.034:.2f}")
    return None


def celsius_to_fahrenheit(temp_celsius: float):
    """
        Converts temperature in Celsius to temperature in Fahrenheit.
        Returns degrees Fahrenheit as float.

        :param:
            temp_celsius (float) -- temperature in Celsius

        Example:
            celsius_to_fahrenheit(40)
            (104.0)

        """
    return float(f"{((temp_celsius * 9 / 5) + 32):.2f}")


def fahrenheit_to_celsius(temp_fahrenheit: float):
    """
        Converts temperature in Fahrenheit to temperature in Celsius.
        Returns degrees Celsius as float.

        :param:
            temp_fahrenheit (float) -- temperature in Fahrenheit

        Example:
            fahrenheit_to_celsius(104)
            (40.0)
        """
    return float(f"{((temp_fahrenheit - 32) * 5 / 9):.2f}")


def kg_to_lb(kg: float):
    """
        Converts kilograms to pounds.
        Returns pounds as float.

        :param:
            kg (float) -- kilograms

        Example:
            kg_to_lb(50)
            (110.23)
        """
    return float(f"{kg * 2.20462:.2f}")


def lb_to_kg(lb: float):
    """
        Converts pounds to kilograms.
        Returns kilograms as float.

        :param:
            lb (float) -- pounds

        Example:
            lb_to_kg(110.23)
            (50.0)
        """
    return float(f"{(lb * 0.453592):.2f}")

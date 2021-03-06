import random
from datetime import datetime, date

"""Classes for melon orders."""

class AbstractMelonOrder():
    """ Abstract melon order """
    def __init__(self, order_type, tax):
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
       
        base_price = self.get_base_price()
        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_base_price(self):
        """Splurge pricing with base price."""
        
        base_price = random.randint(5, 9)

        order_timestamp = datetime.now()
        current_time = order_timestamp.strftime("%H:%M:%S")
        day_of_the_week = datetime.today().weekday()
        hour = int(current_time[:1])

        if day_of_the_week <=4 and hour >= 8 and hour < 11:
            base_price = base_price + 4

        return base_price

class GovernmentMelonOrder(AbstractMelonOrder):
    """ Government melon order"""
    
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__("domestic", 0.08)
        self.species = species
        self.qty = qty


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__("international", 0.17)
        self.species = species
        self.qty = qty
        self.country_code = country_code

    def get_total(self):
        total = super().get_total()
        if self.qty < 10:
            total += 3 
        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

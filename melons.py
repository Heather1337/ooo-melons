"""Classes for melon orders."""

class AbstractMelonOrder():
    """ Abstract melon order """
    def __init__(self, order_type, tax):
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


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

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

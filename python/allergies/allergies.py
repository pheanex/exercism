class Allergies:
    allergens = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    def __init__(self, code):
        self.lst = [allergen for allergen in self.allergens if self.allergens[allergen] & code]

    def is_allergic_to(self, item):
        return item in self.lst

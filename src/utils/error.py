class TypeErr(Exception):
    def __init__(self, type_1, type_2):
        self.message = f"Can't compare objects of {type_1} and {type_2}"

    def __str__(self):
        return self.message

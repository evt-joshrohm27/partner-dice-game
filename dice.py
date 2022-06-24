from random import randint
class Dice:
    """A class that inplements a dice"""
    @staticmethod
    def roll():
        # returns a random number between 1 and 6
        return randint(1,6)
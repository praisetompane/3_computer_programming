import random


class Dice:
    _lowest = 1
    _highest = 6

    def roll(self):
        a = random.randint(self._lowest, self._highest)
        b = random.randint(self._lowest, self._highest)
        return(a, b)


def main():
    dice = Dice()
    print(dice.roll())
    print(random.random())
    
if __name__ == "__main__":
    main()

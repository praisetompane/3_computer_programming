from reverse_order import reverse_order

def main():
    s1 = "apple"
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = ""
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = "racecar"
    print("%s reversed: %s" % (s1, reverse_order(s1)))
    s1 = [1, 2, 3, 4, 5]
    print(s1, "reversed:", reverse_order(s1))
    s1 = []
    print(s1, "reversed:", reverse_order(s1))


main()
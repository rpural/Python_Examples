#! /usr/bin/env python3


def int2text(value, _lvl=0):
    digits = ["", "one", "two",
					"three", "four", "five",
					"six", "seven", "eight",
					"nine"]

    teens = ["ten", "eleven", "twelve",
					"thirteen", "fourteen", "fifteen",
					"sixteen", "seventeen",
					"eighteen", "nineteen"]

    tens =["", "", "twenty", "thirty",
				"forty", "fifty", "sixty",
				"seventy", "eighty", "ninety"]

    groupings = ["", "thousand", "million", "billion", "trillion",
                "quadrillion", "quintrillion", "sextillion", "septillion",
                "octillion", "nonillion", "decillion"]

    if value == 0 and _lvl == 0:
        return "zero"

    (excess, working) = (value // 1000, value % 1000)

    result = ""

    if excess > 0:
        result = int2text(excess, _lvl=_lvl+1)

    (hundreds, v) = (working // 100, working % 100)
    (t, v) = (v // 10, v % 10)

    if hundreds > 0:
        result = result + " " + digits[hundreds] + " hundred"

    if t == 1:
        result = result + " " + teens[v]
    elif t > 0:
        result = result + " " + tens[t]

    if t != 1:
        result = result + " " + digits[v]

    result = result + " " + groupings[_lvl]

    return result.strip()


if __name__ == "__main__":
    while(True):
        source = int(input("Enter a number: "))

        print(int2text(source))

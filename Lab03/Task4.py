import math
class SquareGenerator:
    def e_squares(SquareGenerator, start, end):
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

generator = SquareGenerator();

list = [math.sqrt(x) for x in generator.e_squares(1,10)]
print(list)
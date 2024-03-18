class SquareGenerator:
    def e_squares(SquareGenerator, start, end):
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

generator = SquareGenerator();
print(generator.e_squares(1,10))
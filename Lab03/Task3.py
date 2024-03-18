class SquareGenerator:
    def generate_squares(self, start, end):
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

generator = SquareGenerator();
print(generator.generate_squares(1,10))
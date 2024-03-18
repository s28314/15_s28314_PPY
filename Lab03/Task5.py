class SquareGenerator:
    def generate_squares(self, start, end):
        if(start > end):
            raise ValueError('End of the range is less than the start ')
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

generator = SquareGenerator();
print(generator.generate_squares(20,10))
class SquareGenerator:
    def generate_squares(self, start, end):
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        list = [x * x * x for x in range(end + 1) if x > start - 1]
        return list
    def generate_squares(self, start, end):
        if(start > end):
            raise ValueError('End of the range is less than the start ')
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

squaregenerator = SquareGenerator()
print(squaregenerator.generate_squares(1,10))
cubicgenerator = CubicGenerator()
print(cubicgenerator.generate_cubes(1,10))
print(cubicgenerator.generate_squares(20,10))
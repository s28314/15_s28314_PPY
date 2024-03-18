class SquareGenerator:
    def e_squares(SquareGenerator, start, end):
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

class CubicGenerator(SquareGenerator):
    def e_cubes(CubicGenerator, start, end):
        list = [x * x * x for x in range(end + 1) if x > start - 1]
        return list

squaregenerator = SquareGenerator();
print(squaregenerator.e_squares(1,10))
cubicgenerator = CubicGenerator();
print(cubicgenerator.e_cubes(1,10))
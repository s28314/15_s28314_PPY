from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        list = [x * x * x for x in range(end + 1) if x > start - 1]
        return list

    def generate_squares(self, start, end):
        if (start > end):
            raise ValueError('End of the range is less than the start ')
        list = [x * x for x in range(end + 1) if x > start - 1]
        return list

cubicgenerator = CubicGenerator()
print(cubicgenerator.generate_squares(1, 10))

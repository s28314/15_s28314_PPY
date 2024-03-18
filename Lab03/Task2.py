def generate_squares(start,end):
    list = [x * x for x in range(end+1) if x > start-1]
    return list

print(generate_squares(1,10))
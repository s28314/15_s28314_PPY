def e_squares(start,end):
    list = [x * x for x in range(end+1) if x > start-1]
    return list

print(e_squares(1,10))
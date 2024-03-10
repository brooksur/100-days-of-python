import math


def paint_calc(height, width, cover):
    area = height * width
    calc = math.ceil(area / cover)
    print(f"You'll need {calc} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

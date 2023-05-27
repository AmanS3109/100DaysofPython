import math
wall_height = int(input("Enter wall height (feet):\n"))
wall_width = int(input("Enter wall width (feet):\n"))
coverage = 5

def no_of_cans(height=wall_height, width=wall_width, cover=coverage):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")
no_of_cans()
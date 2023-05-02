import math
# paintareacalculation

def paint_area(height,width,cover):
        number_of_cans= math.ceil(height*width/cover)
        print(f"you will need {number_of_cans} cans of paint")


test_height=int(input("height of wall\n"))
test_width=int(input("width of the wall\n"))
coverage=5
paint_area(height=test_height,width=test_width,cover=coverage)
#the value of total painted matri
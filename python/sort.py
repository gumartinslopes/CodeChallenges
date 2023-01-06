import operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(10,5)
p2 = Point(8,15)
p3 = Point(6,11)

arr = [p1, p2, p3]
sorted_arr_x = sorted(arr, key = operator.attrgetter('x'))
sorted_arr_y = sorted(arr, key = operator.attrgetter('y'))

for point in sorted_arr_x:
    print(f'x:{point.x}, y:{point.y}')

for point in sorted_arr_y:
    print(f'x:{point.x}, y:{point.y}')

    

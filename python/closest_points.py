import math
import operator

# Find the two closest points in the space
class Point:
    def __init__(self, x, y ,label):
        self.x = x
        self.y = y
        self.label = label

def euclidian_distance(pa, pb):
    return math.sqrt(pow((pa.x - pb.x), 2) + pow((pa.y - pb.y), 2)) 

#brute force solution O(n^2)
def closest_points_bf(space):
    result = [None, None]
    min_distance = 10000000000000000000000000000000000000000000;
    for i in range(len(space) - 1):
        for j in range(i + 1, len(space)):
            current_distance = euclidian_distance(space[i], space[j])
            if(min_distance > current_distance):
                min_distance = current_distance
                result[0] = space[i]
                result[1] = space[j]

    return result[0], result[1], min_distance

def closest_rec(x_sort, y_sort):
    n = len(x_sort)
    # base case
    if n <= 3:
        return closest_points_bf(x_sort)
    else:
        mid = x_sort[n//2]
        x_sort_left = x_sort[:n//2]
        x_sort_right = x_sort[n//2:]
        y_sort_left = []
        y_sort_right = []
        print('----------')
        
        for point in y_sort:
            y_sort_left.append(point) if(point.x <= mid.x) else y_sort_right.append(point)
        print('Tamanho: ', len(y_sort))
        print(y_sort_left)
        print('\n\n')
        print(y_sort_right)
        print('----------\n\n\n')
        p1_left, p2_left, delta_left = closest_rec(x_sort_left, y_sort_left) 
        p1_right, p2_right, delta_right = closest_rec(x_sort_right, y_sort_right) 
        
        (p1, p2, delta) = (p1_left, p2_left, delta_left) if (delta_left < delta_right) else (p1_right, p2_right, delta_right)
        
        in_band = [point for point in y_sort if mid.x - delta < point.x < mid.x + delta]
        # calculating the points in the delimitation
        for i in range(len(in_band)):
            for j in range(i + 1, min(i+ 7, len(in_band))):
                d = euclidian_distance(in_band[i], in_band[j])
                if d < delta:
                    (p1, p2, delta) = (in_band[i], in_band[j], d)
        return p1, p2, delta


def closest_points_dq(space):
    # sorting the space by x and y
    x_sort = sorted(space, key = operator.attrgetter('x'))
    y_sort = sorted(space, key = operator.attrgetter('y'))
    return closest_rec(x_sort, y_sort)

p1 = Point(5, 3, 'P1')
p2= Point(5, 100, 'P2')
p4 = Point(5, 44, 'P4')
p3 = Point(5, 4, 'P3')

space = [p1, p4, p2, p3]
r1, r2, distance = closest_points_bf(space)
r3, r4, distance_dq = closest_points_dq(space)

print(r1.label, r2.label, distance)
print(r3.label, r4.label, distance_dq)

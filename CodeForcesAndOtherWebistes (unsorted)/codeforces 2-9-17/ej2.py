prittyAnswer = {True:"Yes", False:"No"}

n = int(raw_input())
numbers = list(map(lambda x: int(x),raw_input().split()))
points = []

for x in range(n):
    points.append([x+1,numbers[x]])


def pointTouchesVertex(point, vertex):
    multiplicacion_x = ((point[0] - vertex[2][0])* 1.0) / vertex[0] * 1.0
    new_y = multiplicacion_x * (vertex[1] * 1.0) + (vertex[2][1])
    return abs(point[1] - new_y) < 0.001

answer = False

for z in range(1,n):
    vertex = []
    vertex_p = []
    vertex.append(-points[0][0] + points[z][0])
    vertex_p.append(-points[0][0] + points[z][0])
    vertex.append(-points[0][1] + points[z][1])
    vertex_p.append(-points[0][1] + points[z][1])
    vertex.append(points[0])

    found_other = False
    found_outsider = False

    for y in range(1, z)+range(z+1,n):
        if not pointTouchesVertex(points[y], vertex):
            found_other = True
            break


    if found_other:
        vertex_p.append(points[y])
        found_outsider = False
        for x in (range(1, z) + range(y+1,n)):
            p = points[x]
            pt1 = pointTouchesVertex(p, vertex)
            pt2 = pointTouchesVertex(p, vertex_p)
            if not pt1 and  not pt2:
                found_outsider = True
                break
        if not found_outsider:
            answer = True


if not answer:
    vertex = []
    vertex.append(-points[1][0] + points[2][0])
    vertex.append(-points[1][1] + points[2][1])
    vertex.append(points[1])
    if not pointTouchesVertex(points[0], vertex):
        found_outsider = False
        for z in range(1,n):
            if not pointTouchesVertex(points[z], vertex):
                found_outsider = True
                #break
        answer  = not found_outsider


print prittyAnswer[answer]

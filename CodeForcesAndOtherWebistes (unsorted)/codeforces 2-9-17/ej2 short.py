prittyAnswer = {True:"Yes", False:"No"}

n,h = (map(lambda x: int(x),raw_input().split()))
numbers = list(map(lambda x: int(x),raw_input().split()))
input_points = []


for x in range(n):
    input_points.append([x+1,numbers[x]])


def pointTouchesVertex(point, vertex):
    multiplicacion_x = ((point[0] - vertex[2][0])* 1.0) / vertex[0] * 1.0
    new_y = multiplicacion_x * (vertex[1] * 1.0) + (vertex[2][1])
    return (point[1] == new_y)

def has2linesWithoutOutsiders(points):
	for x in [1,2,3]:
		vertex = []
		vertex_p = []
		if(x < 3):
			vertex.append(points[0][0] - points[x][0])
			vertex_p.append(points[0][0] - points[x][0])
			vertex.append(points[0][1] - points[x][1])
			vertex_p.append(points[0][1] - points[x][1])
			vertex.append(points[0])
			if(x == 1):
				first_outsider_point = 0
			 	for y in range(2,n):
			 		if first_outsider_point == 0 and not pointTouchesVertex(points[y], vertex):
						first_outsider_point = y

				if(first_outsider_point == 0):
					return False
					
				tmp_point_0 = points[first_outsider_point][0]
				tmp_point_1 = points[first_outsider_point][1]
				points[first_outsider_point][0] = points[2][0]
				points[first_outsider_point][1] = points[2][1]
				points[2][0] = tmp_point_0
				points[2][1] = tmp_point_1
				vertex_p.append(points[2])
			elif(x == 2):
				vertex_p.append(points[1])
		elif(x==3):
			vertex.append(points[1][0] - points[2][0])
			vertex_p.append(points[1][0] - points[2][0])
			vertex.append(points[1][1] - points[2][1])
			vertex_p.append(points[1][1] - points[2][1])
			vertex.append(points[1])
			vertex_p.append(points[0])

		found_outsider = False
		if n > 3:
			for z in range(3, n):
				p = points[z]
				pt1 = pointTouchesVertex(p, vertex)
				pt2 = pointTouchesVertex(p, vertex_p)
				if (not (pt1) and  not (pt2)):
					found_outsider = True

		if not found_outsider:
			return True
	return False

print prittyAnswer[has2linesWithoutOutsiders(input_points)]

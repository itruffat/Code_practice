import matplotlib.pyplot as plt
import math as Math

class Vector3:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def inv(self):
		try:
			assert(self.x != 0)
			assert(self.z != 0)
		except:
			raise Exception("Division por 0 en algun vector 3")
		new_x = self.x if self.x == 0 else 1/self.x
		new_z = self.z if self.z == 0 else 1/self.z  
		return Vector3(new_x,0,new_z)

	def __add__(self,v2):
		assert(type(v2) is Vector3)
		return Vector3(self.x+v2.x,self.y+v2.y,self.z+v2.z)
		
	def __sub__(self,v2):
		assert(type(v2) is Vector3)
		return Vector3(self.x-v2.x,self.y-v2.y,self.z-v2.z)
	
	def __eq__(self,v2):
		assert(type(v2) is Vector3)
		#return self.x == v2.x and self.y == v2.y and self.z == v2.z
		check = lambda x,y : Math.fabs(x - y) < 0.000001
		return check(self.x,v2.x) and check(self.y,v2.y) and check(self.z,v2.z)
		
	def __str__(self):
		return(str([self.x, self.y, self.z]))

	def __repr__(self):
		return str(self)

	def plot_point(self):
		plt.plot([self.x], [self.z], 'ro')
		#plt.show()


def norm_2(vector):
	assert(type(vector) is Vector3)
	return(Math.sqrt(Math.pow(vector.x,2)+Math.pow(vector.z, 2)))

def get_ortogonal_step(line_step, debug = False):
	assert(type(line_step) is Vector3)
	vector = line_step
	if vector.z == 0:
		return Vector3(0,0,-1)
	return Vector3(1,0, -vector.x/vector.z)

def step_multiplier_between_points(point1,step,point2, debug = False):
	assert(type(point1) is Vector3)
	assert(type(step) is Vector3)
	assert(type(point2) is Vector3)
	distance_to_travel_vector = point2 - point1
	#if debug:
	#	print(distance_to_travel_vector)
	distance_to_travel = distance_to_travel_vector.x
	step_to_travel = step.x
	if distance_to_travel == 0:
		distance_to_travel = distance_to_travel_vector.z
		step_to_travel = step.z
	if distance_to_travel == 0 and step_to_travel == 0:
		step_to_travel = 1
	return distance_to_travel/step_to_travel
	
def step_multiplier_between_lines(base1,step1,base2,step2, debug = False):
	assert(type(base1) is Vector3)
	assert(type(step1) is Vector3)
	assert(type(base2) is Vector3)
	assert(type(step2) is Vector3)
	# A line can be written as {{base + change * step}}
	# q = alpha y w = beta
	# b1 + q*s1 = b2 + w*s2
	#
	alpha = 0
	beta  = 0
	if step2.x == 0:
		alpha = (base2.x - base1.x)/step1.x
		beta  = (base1.z - base2.z)/step2.z
	else:
		f = step2.z / step2.x
		r = (step1.x * f - step1.z)
		if r == 0:
			alpha = step_multiplier_between_points(base1,step1,base2)
		else:
			# b1.x + q*s1.x = b2.x + w*s2.x
			# b1.x + q*s1.x - b2.x = w*s2.x
			#(b1.x + q*s1.x - b2.x)/s2.x = w
			#
			# b1.y + q*s1.y = b2.y + w * s2.y
			# b1.y + q*s1.y = b2.y + ((b1.x + q*s1.x - b2.x)/s2.x)*s2.y
			# b1.y + q*s1.y = b2.y + (b1.x + q*s1.x - b2.x)*(s2.y/s2.x)
			# >>>>>> (s2.y/s2.x) = f
			# b1.y + q*s1.y = b2.y + (b1.x + q*s1.x - b2.x)*f
			# b1.y + q*s1.y - b2.y = (b1.x + q*s1.x - b2.x)*f
			# b1.y + q*s1.y - b2.y = (b1.x - b2.x)*f + q* (s1.x * f)
			# b1.y + q*s1.y - b2.y - (b1.x - b2.x)*f = q* (s1.x * f)
			# b1.y + q*s1.y - b2.y - b1.x*f + b2.x*f = q* (s1.x * f)
			# b1.y - b2.y - b1.x*f + b2.x*f = q* (s1.x * f) - q*s1.y
			# b1.y - b2.y - b1.x*f + b2.x*f = q* (s1.x * f - *s1.y)
			# >>>>> r = (s1.x * f - *s1.y)
			# b1.y - b2.y - b1.x*f + b2.x*f = q* r
			#(b1.y - b2.y - b1.x*f + b2.x*f)/r = q
			alpha = (base1.z - base2.z - base1.x*f + base2.x*f) / r
			# (b1.x + q*s1.x - b2.x)/s2.x = w
			beta = (base1.x + alpha * step1.x - base2.x)/step2.x
	return alpha, beta


def walk_line(base,step,quantity, debug = False):
	return base + Vector3(quantity * step.x, 0, quantity * step.z)

def is_point_in_line(base1, base2, point, debug = False):
	in_line = False
	step = base2 - base1
	step_orto = get_ortogonal_step(step)
	alpha, beta = step_multiplier_between_lines(base1,step,point,step_orto)
	if beta == 0:
		line_alpha = step_multiplier_between_points(base1,step,base2)
		if alpha == 0:
			in_line = True
		elif (alpha > 0) == (line_alpha > 0):
			in_line = Math.fabs(alpha) <= Math.fabs(line_alpha)
	return in_line


def same_step(step1, step2, debug = False):
	answer = False
	if (step1.x == 0 or step2.x == 0):
		answer = (step1.x == 0 and step2.x == 0)
	else:
		#answer = (Math.fabs(step1.z/step1.x) == Math.fabs(step2.z/step2.x))
		answer = ((step1.z/step1.x) == (step2.z/step2.x))
	return answer

#def velocidad(pos_vieja, pos_nueva):
#	return pos_nueva - pos_vieja

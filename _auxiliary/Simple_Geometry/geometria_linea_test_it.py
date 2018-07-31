from geometria_linea import *
import math as Math

def test_it():
	print("testing\n-----")
	test_1()
	test_2()
	test_3()
	test_4()
	test_5()
	test_6()


def test_generico(v, f, test_name = "nameless test:", debug = []):
	print(test_name)
	for v_test in v:
		va = v_test[-1]
		vq = v_test[:-1]
		debug_flag = False
		if debug != []:
			debug_flag = debug.pop(0)
				
		result = f(*vq, debug = debug_flag)
		
		try:
			assert(va == result)
		except AssertionError:
			print("\n\n")
			print("input: {}\n expected:{} / result:{}".format(vq, va, result))
			raise AssertionError
		except Exception as e:
			raise e
	print("      passed")
	
def test_1(): # testing ortogonal step
	v = [
		[Vector3( 2,0, 3), Vector3(1,0,-2/3) ],
		[Vector3( 2,0,-3), Vector3(1,0, 2/3) ],
		[Vector3(-2,0, 3), Vector3(1,0, 2/3) ],
		[Vector3(-2,0,-3), Vector3(1,0, -2/3)],
		[Vector3(0,0,1)  , Vector3(1,0,0)    ],
		[Vector3(0,0,20) , Vector3(1,0,0)    ],
		[Vector3(1,0,0)  , Vector3(0,0,-1)   ],
		[Vector3(20,0,0) , Vector3(0,0,-1)   ]
		]
		
	debug = []
	test_generico(v,get_ortogonal_step,"ortogonal_test:", debug)
	
def test_2(): #testing step_multiplier_between_points
	v = [
		[Vector3(1,0,-2/3) , Vector3(1,0,-2/3),Vector3(1,0,-2/3),0],
		[Vector3(0,0,1)    , Vector3(1,0,0), Vector3(2,0,1)     ,2],
		[Vector3(1,0,0)    , Vector3(0,0,1), Vector3(1,0,2)     ,2],
		[Vector3(1,0,0)    , Vector3(1,0,1), Vector3(3,0,2)     ,2],
		[Vector3(0,0,1)    , Vector3(0,0,0.5), Vector3(0,0,11) ,20],
		[Vector3(0,0,1)    , Vector3(0,0,0.5), Vector3(0,0,-9),-20],
		[Vector3(0,0,1)    , Vector3(0,0,-0.5),Vector3(0,0,11),-20],
		[Vector3(0,0,1)    , Vector3(0,0,-0.5),Vector3(0,0,-9), 20]
		]
		
	debug = []
	test_generico(v,step_multiplier_between_points,"between_points_test:", debug)


def test_3(): #testing step_multiplier_between_lines
	v = [
		[Vector3(1,0,1) , Vector3(1,0,0),Vector3(4,0,7), Vector3(0,0,1),(3,-6)],
		[Vector3(1,0,1) , Vector3(0,0,1), Vector3(2,0,2), Vector3(11,0,0),(1,-1/11)],
		#[Vector3(1,0,0)    , Vector3(0,0,1), Vector3(1,0,2), Vector3(0,0,11),(1,2)],
		#[Vector3(1,0,0)    , Vector3(1,0,1), Vector3(3,0,2), Vector3(0,0,11),(1,2)],
		#[Vector3(0,0,1)    , Vector3(0,0,0.5), Vector3(0,0,11), Vector3(0,0,11),(1,2)],
		[Vector3(1,0,1)    , Vector3(0.75,0,0.5), Vector3(1,0,5), Vector3(0.75,0,-0.5),(4,4)],
		[Vector3(1,0,0)    , Vector3(-1,0,0),Vector3(7,0,6), Vector3(2,0,3),(-2,-2)],
		[Vector3(0,0,1)    , Vector3(0,0,2),Vector3(2,0,2), Vector3(1,0,0), (0.5,-2)]
		]
		
	debug = []
	test_generico(v,step_multiplier_between_lines,"between_lines_test:", debug)


def test_4(): #walk line
	v = [
		[Vector3(1,0,-2/3) , Vector3(1,0,1/2), 2,    Vector3(3,0,1/3)],
		[Vector3(0,0,1)    , Vector3(1,0,0), 3,    Vector3(3,0,1)],
		[Vector3(1,0,0)    , Vector3(0,0,1), 1,    Vector3(1,0,1)],
		[Vector3(1,0,0)    , Vector3(1,0,1), -1,   Vector3(0,0,-1)],
		[Vector3(1,0,1)    , Vector3(0.5,0,0.5), -3, Vector3(-0.5,0,-0.5)],
		[Vector3(0,0,1)    , Vector3(0,0,0.5), -1/2, Vector3(0,0,3/4)],
		[Vector3(0,0,1)    , Vector3(0,0,-0.5),-2/3, Vector3(0,0,4/3)],
		[Vector3(0,0,1)    , Vector3(0,0,-1), 75, Vector3(0,0,-74)]
		]		
	debug = []
	test_generico(v,walk_line,"walkline_test:", debug)

def test_5(): #point in line
	v = [
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(0,0,3), False],
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(1,0,6), False],
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(1,0,0), False],
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(1,0,3),  True],
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(1,0,5),  True],
		[Vector3(1,0,1) , Vector3(1,0,5), Vector3(1,0,1),  True],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(1,0,1),  True],
	
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(3,0,0), False],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(6,0,1), False],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(0,0,1), False],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(3,0,1),  True],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(5,0,1),  True],
		[Vector3(1,0,1) , Vector3(5,0,1), Vector3(1,0,1),  True],
		[Vector3(1,0,1) , Vector3(2,0,2), Vector3(1.5,0,1.5),  True]
		]		
	debug = [*([False]*5), True]
	test_generico(v,is_point_in_line,"dot_in_line_test:", debug)



def test_6(): #"Same Step"
	v = [
		[Vector3(1,0,1) , Vector3( 5,0, 5), True],
		[Vector3(1,0,1) , Vector3(-5,0,-5), True],
		[Vector3(1,0,-1), Vector3( 5,0,-5), True],
		[Vector3(1,0,1) , Vector3( 5,0,-5), False],
		[Vector3(1,0,1) , Vector3(-5,0, 5), False],
		[Vector3(-1,0,1), Vector3( 5,0, 5), False],
		
		[Vector3(1,0,1) , Vector3( 0,0, 1), False],
		[Vector3(1,0,1) , Vector3( 1,0, 0), False],
		
	
		[Vector3(0,0,1) , Vector3( 1,0, 1), False],
		[Vector3(1,0,0) , Vector3( 1,0, 1), False],
		
		[Vector3(0,0,5) , Vector3( 0,0, 1), True],
		[Vector3(0,0,5) , Vector3( 0,0,-1), True],
		[Vector3(0,0,-5), Vector3( 0,0, 1), True],
		[Vector3(0,0,-5), Vector3( 0,0,-1), True],
				
		
		[Vector3(5,0,0) , Vector3( 1,0, 0), True],
		[Vector3(5,0,0) , Vector3(-1,0, 0), True],
		[Vector3(-5,0,0), Vector3( 1,0, 0), True],
		[Vector3(-5,0,0), Vector3(-1,0, 0), True],
		
		[Vector3(1,0,1) , Vector3(1,0,5), False]
		]		
	debug = []
	test_generico(v,same_step,"same_step_test:", debug)
	
def test_basico():
	a1 = Vector3(2,0,3)
	a2 = Vector3(0,0,0)
	a3 = Vector3(1,0,1)

	
	plt.plot([a1.x, a2.x], [a1.z, a2.z], 'b')
	a3.plot_point()
	step1 = (a2 - a1)
	step3 = get_ortogonal_step(step1)

	steps2travel = steps_between_points(a1, step1, a2)
	print(steps2travel)
	#alpha = steps_between_lines(a1, step1, a2, step1)
	#print(beta)
	#move_in_line(a1,step1,alpha)

	plt.plot([a3.x, a3.x + step3.x*4], [a3.z, a3.z + step3.z*4], 'g')
	plt.plot([a3.x, a3.x - step3.x*4], [a3.z, a3.z - step3.z*4], 'g')

	#

	#a5 = a1 + Vector3(alpha * step1.x, 0, alpha * step1.z)
	#a5.plot_point()
	#print(alpha)

	alpha, beta = steps_between_lines(a1, step1, a2, step1)
	a6 = walk_line(a1,step1, alpha)
	a6.plot_point()

	alpha, beta = steps_between_lines(a1, step1, a3, step3)
	print(alpha)
	#a7 = walk_line(a1,step1, alpha)
	a7 = walk_line(a3,step3, beta)
	a7.plot_point()

	plt.ylim(0,8)
	plt.xlim(0,8)
	plt.show()
	

if __name__ == "__main__":
	test_it()

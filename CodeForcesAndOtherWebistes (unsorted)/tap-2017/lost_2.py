## Combinaciones que dan cuadrados
#####..L..O..S..T
#####..4..0..0..0.=l4
#####..2..2..0..0.=l2o2
#####..2..0..2..0.=l2s2
#####..1..0..1..2.=lst2
#####..0..4..0..0.=o4
#####..0..0..0..4.=t4

## lst2 solo me importa para un caso.
## Esto se debe a que:
## x_par   * lst2 =  0   + ((   x_par    )/2) * (t4 + l2s2)
## x_impar * lst2 = lst2 + (( x_impar - 1)/2) * (t4 + l2s2)

## lo mismo ocurre con l2o2 por la misma razon.
## x_par   * l2o2 =  0   + ((   x_par    )/2) * (l4 + o4)
## x_impar * l2o2 = l2o2 + (( x_impar - 1)/2) * (t4 + o4)

def inpt():
	#return "1 1 1 1"
	#return "1000000000 0 0 0"
	#return "99 99 99 99"
	return raw_input()

l,o,s,t = map(int, inpt().split() )

lst2 = ((l%2 + s%2)/2) * ((t%4)/2)

l2= l/2
o2= o/2
s2= s/2
t2= t/2

l2s2 = min(l2, s2)
l2 -= l2s2
l2o2 = (l2%2 + o2%2)/2

l4 = l2/2
o4 = o2/2
t4 = t2/2

answer= (l4) + (o4) + (l2s2) + (t4) + (l2o2) + (lst2)

print answer

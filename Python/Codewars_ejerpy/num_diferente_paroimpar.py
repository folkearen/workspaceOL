"""El problema aqui fue consultar si era par y luego comparar los indices 1 y 2
para comporbar si habia mas de un impar o par
arrojaba un pproblema si era diferents en lso primeros dos indices
se soluciono separando pares e impares en listas distintas
luego compara su longitud e imprimi el indice 0
"""
def find_outlier(integers):
	par = []
	impar = []
	for i in integers:
		if i % 2 == 0:
			par.append(i)
		else:
			impar.append(i)
	if len(par) < len(impar):
		
		return par[0]
	else:
		return impar[0]

    # odds = [x for x in integers if x%2!=0]
    # evens= [x for x in integers if x%2==0]
    # return odds[0] if len(odds)<len(evens) else evens[0]

	
print(find_outlier([2,4,6,7,8,10]))
print(find_outlier([1,3,5,6,7,9,11]))
print(find_outlier([-2117883, 9450873, -4458108, 7860505, 1925169, 7357561, 3937925, -2609755, 1182771, -1892585, -5760675, -978575]))
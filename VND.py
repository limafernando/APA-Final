def removeBucket(vertices, adjacentes, cores, k, usedColour):
	buckets = [[0]*1 for i in range(k)]

	print(vertices)
	print(cores)
	print(buckets)
	
	for i in range(0, len(cores)):
		v = vertices[i]
		c = cores[i]
		indice = usedColour.index(c)
		buckets[indice].append(v)

	for b in buckets:
		b.pop(0)

	print(usedColour)
	print(buckets)

	#tentar remover algum bucket
	for i in range(0, k):
		auxList = cores.copy()
		auxList.remove(usedColour[i]) #remove a cor que vamos tentar remover da solução
		bucket = buckets[i]

		for vertice in bucket:
			#tenta mudar a cor
			#semelhante a construção
			pass	
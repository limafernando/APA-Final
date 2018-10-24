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

	novasCores = [cores*1 for i in range(k)]
	print(adjacentes[vertices.index('9')])
	#tentar remover algum bucket
	for i in range(0, k):
		auxColourList = usedColour.copy()
		auxColourList.remove(usedColour[i]) #remove a cor que vamos tentar remover da solução
		bucket = buckets[i]
		print('usado:',usedColour[i])
		print('aux:',auxColourList)

		for vertice in bucket:

			#tenta mudar a cor
			#semelhante a construção

			indice = vertices.index(vertice)

			#print(novasCores)
			print(vertice)
			for c in auxColourList:
				print('c: ', c)
				print(adjacentes[indice])
				for adj in adjacentes[indice]:
					
					indiceAdj = vertices.index(adj)

					if c == cores[indiceAdj]:
						canUse = False
						break
						
					else:
						canUse = True

				if canUse:
					print('sim')
					novasCores[i][indice] = c
					'''if i ==3 and indice == 9:
						print(i, indice)
						print(novasCores[i][indice])'''
					break
				else:
					print('não')
					

	print("cores:", cores)
	print('novasCores:', novasCores)
	print('\n')
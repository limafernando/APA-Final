def removeBucket(vertices, adjacentes, cores, k, coresUsadas):
	
	buckets = [[0]*1 for i in range(k)] #lista com k listas, cada uma para uma cor

	#print(vertices)
	#print(cores)
	#print(buckets)
	
	#insere em cada bucket os vertices que estão usando a cor que o bucket representa
	for i in range(0, len(cores)):
		v = vertices[i]
		c = cores[i]
		indice = coresUsadas.index(c)
		buckets[indice].append(v)

	#para remover o primeiro elemento que iniciou cada bucket 
	for b in buckets:
		b.pop(0)

	#print(coresUsadas)
	#print(buckets)

	solucoes = [cores*1 for i in range(k)] #lista com k listas, cada uma para uma vizinhaça da solução

	#print(adjacentes[vertices.index('9')])
	
	#tentar remover os elementos dos buckets (vizinhança)
	for i in range(0, k):
		
		auxColourList = coresUsadas.copy()
		auxColourList.remove(coresUsadas[i]) #remove da lista a cor que vamos tentar remover da solução
		
		bucket = buckets[i]
		
		#print('usado:',coresUsadas[i])
		#print('aux:',auxColourList)

		for vertice in bucket: #tenta mudar a cor, semelhante a construção

			indice = vertices.index(vertice)

			#print(solucoes)
			#print(vertice)
			
			for c in auxColourList:
				#print('c: ', c)
				#print(adjacentes[indice])
				
				for adj in adjacentes[indice]:
					
					indiceAdj = vertices.index(adj)

					if c == cores[indiceAdj]:
						canUse = False
						break
						
					else:
						canUse = True

				if canUse:
					#print('sim')
					solucoes[i][indice] = c
					break				

	#print("cores:", cores)
	#print('solucoes:', solucoes)
	#print('\n')

	novasCoresUsadas = []
	novosN = []

	for nc in solucoes:
		usado = []
		n = 0
		for cor in nc:
			if cor not in usado:
				n += 1
				usado.append(cor)

		novasCoresUsadas.append(usado)
		novosN.append(n)
	
	#print(novasCoresUsadas)
	#print(novosN)
	
	pair = zip(novosN, novasCoresUsadas)
	ordenado = [x for y, x in sorted(pair)]
	
	#print(o)
	
	melhorCores = ordenado[0]

	#print(o)
	#print(melhorCores)

	melhorK = len(melhorCores)
	#print(solucoes)

	for i in range(0,len(solucoes)):
		if novasCoresUsadas[i] == melhorCores:
			break
		
	#print(i)
	melhorSolucao = solucoes[i]
	#print(melhorSolucao)

	return melhorSolucao, melhorK, melhorCores
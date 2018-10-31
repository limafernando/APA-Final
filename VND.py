import math

def vnd(vertices, adjacentes, cores, k, coresUsadas):
	while True:
		kA = k

		cores, k, coresUsadas = removeBucket(vertices, adjacentes, cores, k, coresUsadas)

		if(kA == k):
			break
	
	pair = zip(vertices, cores)
	cores = [x for y, x in sorted(pair)]
	
	return cores, k, coresUsadas

def removeBucket(vertices, adjacentes, cores, k, coresUsadas):
	
	buckets = [[0]*1 for i in range(k)] #lista com k listas, cada uma para uma cor

	#insere em cada bucket os vertices que estão usando a cor que o bucket representa
	for i in range(0, len(cores)):
		v = vertices[i]
		c = cores[i]
		indice = coresUsadas.index(c)
		buckets[indice].append(v)

	#para remover o primeiro elemento que iniciou cada bucket 
	for b in buckets:
		b.pop(0)

	solucoes = [cores*1 for i in range(k)] #lista com k listas, cada uma para uma vizinhaça da solução
	
	#tentar remover os elementos dos buckets (vizinhança)
	for i in range(0, k):
		
		auxColourList = coresUsadas.copy()
		auxColourList.remove(coresUsadas[i]) #remove da lista a cor que vamos tentar remover da solução
		
		bucket = buckets[i]

		for vertice in bucket: #tenta mudar a cor, semelhante a construção

			indice = vertices.index(vertice)
			
			for c in auxColourList:
				
				for adj in adjacentes[indice]:
					
					indiceAdj = vertices.index(adj)

					if c == solucoes[i][indiceAdj]:
						canUse = False
						break
						
					else:
						canUse = True

				if canUse:
					solucoes[i][indice] = c
					break				

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
	
	menor = math.inf
	menorInd = math.inf
	for i in range(0, len(novosN)):
		if novosN[i] < menor:
			menorInd = i
			menor = novosN[i]

	melhorCores = novasCoresUsadas[menorInd]

	melhorK = len(melhorCores)
	
	melhorSolucao = solucoes[menorInd]

	return melhorSolucao, melhorK, melhorCores
#import Vertice
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def readFile():
	#<Para selecionar o arquivo por GUI#
	Tk().withdraw()
	caminhoArq = askopenfilename()
	#print(caminhoArq)
	arq = open(caminhoArq, 'r')
	conteudoArq = arq.readlines()
	#print(conteudoArq)	
	arq.close()
	#Para selecionar o arquivo por GUI>
	
	conteudoArq = conteudoArq[1:]

	return conteudoArq

def graphRep(conteudoArq):
	#print(conteudoArq)

	vertices = []
	nConexoes = []
	adjacentes = [[]] #começa com 1 elemento/lista vazia que vai ser eliminada depois da primeira iteração

	#cont = 1

	for ele in conteudoArq:
		auxList = ele.split(' ')
		
		vertice1 = auxList[1]
		vertice2 = str(int(auxList[2])) #retira \n

		#print('v1:',vertice1)
		#print('v2:',vertice2)

		vInList = False

		if vertice1 in vertices:
			indice = vertices.index(vertice1)
			nConexoes[indice] += 1

			adjacentes[indice].append(vertice2)

		else:
			vertices.append(vertice1)
			nConexoes.append(1)

			l = [vertice2]
			adjacentes.append(l)


		if vertice2 in vertices:
			indice = vertices.index(vertice2)
			nConexoes[indice] += 1

			adjacentes[indice].append(vertice1)

		else:
			vertices.append(vertice2)
			nConexoes.append(1)

			l = [vertice1]
			adjacentes.append(l)

	#pra remover o primeiro elemento desnecessário
	adjacentes.pop(0)
		
	#print(vertices)
	#print(vertices[0])
	#print(type(vertices[0]))
	'''
	só para printar
	for i in range(0, len(vertices)):
		print('Vértice:', vertices[i])
		print('Num Conexões:', nConexoes[i])
		print('\n')
	'''
	#print(arestas)

	for i in range(0, len(adjacentes)):
		if '0' in adjacentes[i]:
			print(adjacentes[i])
			print(vertices[i])
	
	return vertices, nConexoes, adjacentes


def getColourSet():
	#colourDict = ['red','green','blue','yellow','black','gray','pink','violet', 'orange', 'purple', 'silver', 'indigo', 'gold', 'bronze', 'brown', 'jade', 'sepia']

	colourSet = ['R','G','B','Y','BK','GR','P','V', 'O', 'PP', 'S', 'I', 'GO', 'BZ', 'BN', 'J', 'S']

	return colourSet

def solution0(vertices, nConexoes, adjacentes):
	colourSet = getColourSet()

	#print(colourSet)

	cores = ['']*len(vertices)

	pair = zip(nConexoes, vertices)
	ordemVertices = [x for y, x in sorted(pair, reverse = True)]
	#print('\n')
	#print(ordemVertices)

	ordemIndices = []

	for i in ordemVertices:
		ordemIndices.append(ordemVertices.index(i))

	for i in ordemIndices:
		
		for c in colourSet:
			
			for adj in adjacentes[i]:
				
				indiceAdj = vertices.index(adj)

				if c == cores[indiceAdj]:
					canUse = False
					break
				else:
					canUse = True

			if canUse:
				cores[i] = c
				break

	return cores

def kCores(cores):
	coresUsadas = []
	k = 0
	for cor in cores:
		if cor not in coresUsadas:
			k += 1
			coresUsadas.append(cor)
	return k, coresUsadas

def build():
	conteudoArq = readFile()

	vertices, nConexoes, adjacentes = graphRep(conteudoArq)

	#print(adjacentes)

	cores = solution0(vertices, nConexoes, adjacentes)

	#print(cores)

	k, coresUsadas = kCores(cores)
	#print(k)

	return vertices, adjacentes, cores, k, coresUsadas
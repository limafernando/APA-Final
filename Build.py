from tkinter import Tk
from tkinter.filedialog import askopenfilename
from random import randint

def readFile():
	# Para selecionar o arquivo por GUI
	Tk().withdraw()
	caminhoArq = askopenfilename()
	arq = open(caminhoArq, 'r')
	conteudoArq = arq.readlines()
	arq.close()
	# Para selecionar o arquivo por GUI
	
	conteudoArq = conteudoArq[1:] # Remove a primeira linha

	return conteudoArq

def graphRep(conteudoArq):
	vertices = []
	nConexoes = []
	adjacentes = [] # Comeca com 1 elemento/lista vazia que vai ser eliminada depois da primeira iteracao

	for ele in conteudoArq:
		auxList = ele.split(' ')
		
		vertice1 = auxList[1]
		vertice2 = str(int(auxList[2])) # Retira \n

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

	return vertices, nConexoes, adjacentes

# Gera uma lista de numeros para servir como 'cores'
def getColourSet(numVertices):
	colourSet = [str(i) for i in range(numVertices)]
	return colourSet

def solution0(vertices, nConexoes, adjacentes, alfa):
	colourSet = getColourSet(len(vertices))

	cores = ['']*len(vertices)

	pair = zip(nConexoes, vertices)
	ordemVertices = [x for y, x in sorted(pair, reverse = True)]

	ordemIndices = []

	for i in ordemVertices:
		ordemIndices.append(ordemVertices.index(i))

	for i in ordemIndices:
		aux = []
		for c in colourSet:
			for adj in adjacentes[i]:
				
				indiceAdj = vertices.index(adj)

				if c == cores[indiceAdj]:
					canUse = False
					break
				else:
					canUse = True

			if canUse:
				aux.append(c)
		if(len(aux) > 0):
			random_index = randint(0, int(alfa*len(aux)))
			if(random_index == len(aux)):
				random_index -= 1
			cores[i] = aux[random_index]
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

	return vertices, adjacentes, nConexoes
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

def build():
	conteudoArq = readFile()

	print(conteudoArq)

	vertices = []
	nConexoes = []

	for ele in conteudoArq:
		auxList = ele.split(' ')
		
		vertice1 = auxList[1]
		vertice2 = str(int(auxList[2])) #retira \n

		print(vertice1)
		print(vertice2)

		vInList = False

		if vertice1 in vertices:
			indice = vertices.index(vertice1)
			nConexoes[indice] += 1

		else:
			vertices.append(vertice1)
			nConexoes.append(1)

		if vertice2 in vertices:
			indice = vertices.index(vertice2)
			nConexoes[indice] += 1

		else:
			vertices.append(vertice2)
			nConexoes.append(1)
		
		#print(vertices)

	#print(vertices[0])
	#print(type(vertices[0]))

	for i in range(0, len(vertices)):
		print('Vértice:', vertices[i])
		print('Num Conexões:', nConexoes[i])
		print('\n')
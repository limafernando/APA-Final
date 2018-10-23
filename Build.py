import Vertice
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
	verticeInicial = Vertice.Vertice('-1') #só pra poder entrar nos fors
	vertices.append(verticeInicial)

	for ele in conteudoArq:
		auxList = ele.split(' ')
		
		nomeVertice1 = auxList[1]
		nomeVertice2 = auxList[2]
		nomeVertice2 = nomeVertice2[:-1]

		print(nomeVertice1)
		print(nomeVertice2)

		vInList = False

		for v in vertices:
			
			if nomeVertice1 == v.getNome():
				#v.incNConexoes()
				vInList = True
				break
			
			else:
				#vertice = Vertice.Vertice(nomeVertice1)
				#vertices.append(vertice)
				vInList = False

		if vInList:
			v.incNConexoes()

		else:
			vertice = Vertice.Vertice(nomeVertice1)
			vertices.append(vertice)

		vInList = False

		for v in vertices:
			
			if nomeVertice2 == v.getNome():
				#v.incNConexoes()
				vInList = True
				break
			
			else:
				#vertice = Vertice.Vertice(nomeVertice2)
				#vertices.append(vertice)
				vInList = False

		if vInList:
			v.incNConexoes()

		else:
			vertice = Vertice.Vertice(nomeVertice2)
			vertices.append(vertice)

		print(vertices)

	print(vertices[0])
	print(type(vertices[0]))

	del vertices[0] #removendo o -1

	for v in vertices:
		print('Nome: ', v.getNome())
		print('Nome: ', v.getNConexoes())
		print('\n')
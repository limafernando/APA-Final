import Vertice
import math
import Build as bld
import VND as vnd

def main():
	graspMAX = 1000 # Numero de iteracoes do Grasp
	alfa = 1 # Grau de aleatoriedade

	# Solucao inicial
	cores = []
	k = math.inf
	coresUsadas = []

	# Leitura da instancia e construcao das estruturas
	vertices, adjacentes, nConexoes = bld.build()

	#GRASP
	for i in range(graspMAX):
		coresA = bld.solution0(vertices, nConexoes, adjacentes, alfa) # Fase de Construcao

		kA, coresUsadasA = bld.kCores(coresA)

		coresA, kA, coresUsadasA = vnd.vnd(vertices, adjacentes, coresA, kA, coresUsadasA) # Fase de Busca Local
		
		# Checa se a nova solucao e melhor
		if(kA < k):
			cores = coresA
			k = kA
			coresUsadas = coresUsadasA

	# Imprime a solucao
	print('Solução:', cores)
	print('Número de Cores: ', k)
	print('Cores Usadas: ', coresUsadas)

if __name__ == '__main__':
	main()
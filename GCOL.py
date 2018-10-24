import Vertice
import Build as bld
import VND as vnd


def main():
	vertices, adjacentes, cores, k, coresUsadas = bld.build()

	coresA, kA, coresUsadasA = cores, k, coresUsadas

	cores, k, coresUsadas = vnd.removeBucket(vertices, adjacentes, cores, k, coresUsadas)

	print('Solução Incial:', coresA, kA, coresUsadasA)
	print('Solução vizinhança (buckets):', cores, k, coresUsadas)

if __name__ == '__main__':
	main()
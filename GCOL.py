import Vertice
import Build as bld
import VND as vnd


def main():
	vertices, adjacentes, cores, k, usedColour = bld.build()
	vnd.removeBucket(vertices, adjacentes, cores, k, usedColour)



if __name__ == '__main__':
	main()
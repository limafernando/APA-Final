class Vertice(object):
	
	"""docstring for Vertice"""
	
	def __init__(self, nome):
		
		super(Vertice, self).__init__()
		
		self.nome = nome
		self.nConexoes = 1
	
	def incNConexoes(self):
		self.nConexoes += 1

	def getNome(self):
		return self.nome

	def getNConexoes(self):
		return self.nConexoes
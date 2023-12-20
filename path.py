'''
	Read in a dictionary of nodes, similar to:
	
		nodes : {
			"First" : {
				"Second" : 3,
				"Third" : 2,
				"Fourth" : 4 },
			"Second" : {
				"Third" : 1,
				"Fourth" : 2 },
			"Third" : {
				"Fourth" : 4 },
			"Fourth" : {}
		}
			
	This defines each node in the graph, 
	and each unique weighted path to
	other nodes. If the graph is directed,
	then these define all the available
	paths. If undirected, then the back-paths
	will be created before seeking a shortest
	path.
	
	Note: debugging lines are commented out,
	and produce output beginning with a dash.
	Uncomment as required, comment out
	for production.
'''

import json

class graphUnknownNodeError(Exception):
	pass
class graphNoPathError(Exception):
	pass
	
class graph:
	'''
		read in and process a graph, and
		seek the shortest path between two nodes.
	'''
	
	def __init__(self, filename, directed=False):
		f = open(filename)
		raw = f.read()
		f.close()
		
		''' due to a quirk in MobileC, drop
			the first character.
		'''
		self._nodes = json.loads(raw[1:])
		if not directed:
			for node in self._nodes:
				for edge in self._nodes[node]:
					self._nodes[edge][node] = self._nodes[node][edge]
					
	def display_graph(self):
		'''
			display the dictionary holding the 
			nodes
		'''
		return f"{self._nodes}"
		
	def shortest_path(self, begin, end):
		'''
			find the shortest path from
			begin to end, using the graph
			already defined here
		'''
		# initialize some accumulators
		self._shortest = []
		self._shortest_length = None
		self._path =[]
		self._path_length = 0
		
		# print("-begin search...")
		
		# sanity checks
		if begin not in self._nodes:
			raise graphUnknownNodeError(f"Node {begin} not defined")
		if end not in self._nodes:
			raise graphUnknownNodeError(f"Node {end} not defined")
		
		def find_path(self, begin, end):
			# print(f"-find_path: {self._path_length}: {self._path}")
			
			# case 1: initial node
			if not self._path:
				self._path.append(begin)
				# print(f"-added beginning: {self._path}")
				find_path(self, begin, end)
				return 
				
			# case 2: at the end node
			if self._path[-1] == end:
				# print(f"-at end: {self._path_length}: {self._path}")
				if self._shortest_length == None or self._shortest_length > self._path_length:
					self._shortest = self._path.copy()
					self._shortest_length = self._path_length
				return
			
			# case 3: the general case
			current = self._path[-1]
			# print(f"-current: {current}: {self._nodes[current]}")
			if self._shortest_length:
				if self._path_length >= self._shortest_length:
					# print(f"-short at: {self._path_length} {current}")
					return
			for check in self._nodes[current]:
				if check in self._path:
					continue
				if self._shortest_length:
					if self._path_length >= self._shortest_length:
						# print(f"-short-circuited at {check}")
						return
				# print(f"-checking {current}->{check}")
				self._path.append(check)
				length = self._nodes[current][check]
				self._path_length += length
				find_path(self, begin, end)
				self._path_length -= length
				self._path.pop()
			return
			
		find_path(self, begin, end)
		return (self._shortest_length, self._shortest)

# f = open("path.json")
# data = f.read()
# print(data)
# nodes = json.loads(data[1:])
# print(nodes)

gra = graph("path.json", directed=False)

# print(f"- defined graph: {gra.display_graph()}")

(short_len, short_path) = gra.shortest_path("A", "G")
print(f"shortest = {short_len}, {short_path}")
class Land:
		def __init__(self, name, type, identity):
			self.name = name
			self.type = type
			self.identity = identity
			


		def isWithinIdentity(self, colors=[]):
			#colors = colors
			print(colors)

			if self.type == "dual":
				if colors.contains(self.identity[0]) and colors.contains(self.identity[1]):
					return True

			if self.type == "fetch":
				if colors.contains(self.identity[0]) or colors.contains(self.identity[1]):
					return True
			
			
		
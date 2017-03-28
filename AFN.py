class AFN:

	def __init__(self):
		self.alphabet = []
		self.initialState = None
		self.finalStates = []
		self.states = []		
		self.nextSteps = {}
		self.state = []

	def setInitialState(self):
		self.state = [self.initialState]

	def setAlphabet(self, _alphabet):
		self.alphabet = _alphabet.split(',')

	def checkCurrentWord(self, word):
		for c in word:
			if c not in self.alphabet:
				return 0
		return 1

	def nextStep(self, c):
		next = []		
		for _state in self.state:
			next += self.checkNextSteps(_state, c)
		self.state = next	

	def checkNextSteps(self, _state, c):
		next = []
		for step in self.nextSteps[str(_state)]:
			if step[0] == c:				
				next.append(step[1])
			elif step[0] == '':
				steps = self.checkNextSteps(step[1], c)
				for _step in steps:
					next.append(_step)
		return next

	def tryReadWord(self, word):
		self.setInitialState()
		for c in word:
			self.nextStep(c)
		for _state in self.state:
			if _state in self.finalStates:
				return 'OK'
		return 'not OK'
from AFN import AFN

def loadFile(automaton):
	_file = open('input.txt', 'r')
	ignore = False
	data = []

	for line in _file:
		# check if the character is the # and ignore line
		if line[0] != '#':
			# normalize current line
			line = line.replace(' ','').replace('\r','').replace('\n','')
			# check EOF
			if ignore == False and len(line) > 0:
				# mark the automaton states and mark keys in nextSteps dictionary 
				if len(automaton.states) == 0:
					automaton.states = line.split(',')
					for state in automaton.states:
						automaton.nextSteps[state] = []

				# mark the automaton alphabet
				elif len(automaton.alphabet) == 0:
					automaton.setAlphabet(line)
				
				# mark the automaton transitions and ignore empty nextStep
				elif '|' in line:				
					transition = line.split('|')
					nextStep = transition[2]
					if nextStep != '':
						automaton.nextSteps[transition[0]].append([transition[1], transition[2]])
					
				# mark the initial state
				elif automaton.initialState == None:
					automaton.initialState = line
				
				# mark the final states
				elif len(automaton.finalStates) == 0:
					automaton.finalStates = line.split(',')
					ignore = True
			else:
				data.append(line)

	_file.close()
	return data

def main():	
	automaton = AFN()
	words = loadFile(automaton)
	for word in words:
		automaton.setInitialState()
		if automaton.checkCurrentWord(word) == 0:
			print("\'%s\' : invalide alphabet" % (word))
		else:
			result = automaton.tryReadWord(word)			
			print("\'%s\' : %s" % (word, result))

main()

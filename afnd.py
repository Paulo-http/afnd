import csv
import random
import math
import operator
import time

def load_file(filename):
	with open(filename, 'rb') as file:
		data = file.readlines()
		return data

def load_afnd(data):
	afnd = {}	
	for x in xrange(0,4):
		line = data[x]
		key = line[0]
		line = line.split("=",1)[1]
		line = line.replace("{", "")
		line = line.replace(" ", "")
		line = line.replace("}", "")
		line = line.replace("\n", "")
		afnd[key] = line.split(',')
	return afnd

def load_matrix(data):
	matrix = []
	for x in xrange(5,len(data)):
		line = data[x]	
		line = line.replace("\n", "")
		line = line.replace("{", "")
		line = line.replace("}", "")
		array = line.split(' ')
		matrix.append(array)
	return matrix

def add_empty_character(word):
	characters = list()
	for x in range(len(word)):
		characters.append("")
		characters.append(word[x])
	return characters

def next_state(character, state, matrix):
	header = matrix[0]
	for x in range(len(matrix)):
		if state == matrix[x][0]:
			states = matrix[x]
			idx = header.index(character)
			return states[idx].split(',')

def automaton(word, states, matrix):	
	if word=="" and len(states)==1:
		finals.append(states[0])
	for x in range(len(word)):
		if states!=None:
			for state in states:
				if len(states)==1:
					states = next_state(word[x], state, matrix)					
				else:
					rest_word = word.split(word[x-1],1)[1]
					automaton(rest_word, [state], matrix)
	if states!=None and len(states)==1:
		finals.append(states[0])

finals = []

def main():
	data = load_file("automaton.txt")
	afnd = load_afnd(data)	
	matrix = load_matrix(data)
	word = raw_input('Type the word of the alphabet: ' + str(afnd['e']) + '\n')
	characters = add_empty_character(word)
	automaton(characters, afnd['i'], matrix)
	end_states = afnd['f']
	for x in range(len(finals)):
		if finals[x] in end_states:
			print "OK"
			return
	print "not OK"				

main()

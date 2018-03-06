import ply.lex as lex
import re
import codecs
import os
import sys

tokens =[ 'ID','NUMERO','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT', 'COMA','SEMICOLOM',
		'DOT','UPDATE']

reservadas ={
	'start': 'START', #begin 
	'ende': 'ENDE', #end
	'ob': 'OB', #if
	'dann': 'DANN', #then
	'wahrend':'WAHREND', #while
	'machen': 'MACHEN', #do
	'anruf': 'ANRUF', #call
	'const': 'CONST', #const
	'zahl': 'ZAHL', #int
	'verfahren': 'VERFAHREN', #procedure
	'aus': 'AUS', #out
	'im': 'IM', #in
	'sonst': 'SONST' #else
}

tokens = tokens+list(reservadas.values())

t_ignore = '\t'
t_PLUS = r'\+'
t_ASSIGN = r'='
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

def compilar(self, fileName):
	fp=codecs.open(fileName, 'r')
	file_text = fp.read()
	analizador = lex.lex()
	i=0
	analizador.input(file_text)
	num=self.contLineas(fileName)+1
	print('['+'/'*i+']', end='\r')
	while True:
		tok = analizador.token()
		if not tok:
			break
		else:
			i=i+1
			print('\n',tok)
			print('['+'/'*i+']', end='\r')
				
	fp.close()

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9]*'
	if t.value.upper() in reservadas():
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_COOMENT(t):
	r'\#-*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t
def t_erro(t):
	print ("caracter ilegal"'%s'"t.value[0]")
	t.lexer.skip(1)

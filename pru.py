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
	'begin': 'BEGIN', 
	'end': 'END',
	'if': 'IF',
	'then': 'THEN',
	'while':'WHILE',
	'do': 'DO',
	'call': 'CALL',
	'const': 'CONST',
	'int': 'INT',
	'procedure': 'PROCEDURE',
	'out': 'OUT',
	'in': 'IN',
	'else': 'ELSE'
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
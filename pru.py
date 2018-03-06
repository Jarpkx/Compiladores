import re
import codecs
import ply.lex as lex

#reservadas=['START','ENDE','OB','DANN','WAHREND','MACHEN','ANRUF','CONST','ZAHL','VERFAHREN','AUS','IM','SONST']
tokens = ['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE','ODD','ASSIGN','NE','LT','LTE','GT','GTE','LPARENT','RPARENT','COMMA','SEMMICOLOM','DOT','UPDATE']


reservadas={'start':'START', #begin
'ende':'ENDE', #end
'ob':'OB', #if
'dann':'DANN', #then
'wahrend':'WAHREND', #while
'machen':'MACHEN', #do
'anruf':'ANRUF', #call
'const':'CONST', #const
'zahl':'ZAHL', #int
'verfahren':'VERFAHREN', #procedure
'aus':'AUS', #out
'im':'IM', #in
'sonst':'SONST' #else
}
#listTokens = tokens+reservadas
tokens = tokens+list(reservadas.values())
#listTokens = tokens+list(reservadas.values())

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
	r'~[a-zA-Z_](" ")?[a-zA-Z0-9_]*(\n)?'
	if t.value.upper() in tokens:
 		t.value = t.value.upper()
 		t.type = t.value
	return t


def t_COOMENT(t):
	r'\#-*'
	pass

def t_ESPACE(t):
	r'\ '

def t_ENDLINE(t):
	r'\n'


def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("error lexico")
	t.lexer.skip(1)
	
class Lutor:
	
	def compilar(self,fileName):
		fp=codecs.open(fileName, 'r')
		file_text = fp.read()
		analizador = lex.lex()
		i=0
		analizador.input(file_text)
		print('['+'/'*i + ']',i,'%', end='\r')
		while True:
			tok = analizador.token()
			if not tok:
				break
			else:			
				i=i+1
				print('\n',tok)
				print('['+'/'*i + ']',i,'%', end='\r')
		fp.close()

	
fileName ="archivo.rex"
lexico=Lutor()
lexico.compilar(fileName)

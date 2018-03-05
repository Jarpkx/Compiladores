from time import sleep

for i in range(32):
	if(i != 31):
		print('['+'/'*i+'-'*(30-i) + ']',i,'%', end='\r')
	else:
	  print('\n',"Proceso Terminado")
	
	sleep(0.1)

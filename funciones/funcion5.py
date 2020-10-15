def funcion5(packet):
	try:
		if packet['IP']['src']=='172.17.0.2' and packet['PGSQL']['type']== 'C':
			print('paso1')
			packet['PGSQL']['tag']= "se cambio el tag"
			print('paso2')
			return packet
	except: 
		reuturn None
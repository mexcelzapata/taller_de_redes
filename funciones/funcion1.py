def funcion1(packet):
	try:
		if packet['IP']['src']=='172.17.0.3' and packet['PGSQL']['type']=='Q':
			packet['PGSQL']['type']='X'
			print('paso')
			return packet
	except:
		return None
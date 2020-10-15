def funcion2(packet):
	try:
		if packet['IP']['src']=='172.17.0.3':
			print("paso1")
			packet['PGSQL']['length']=1
			print("paso2")
			return packet
	except:
		return None
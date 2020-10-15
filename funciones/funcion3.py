def funcion3(packet):
	try:
		if packet['PGSQL']['type']=='T':
                        print("prueba1")
                        packet['PGSQL']['field.count']=1
                        print("prueba2")
                        return packet
        except:
                return None
def funcion4(packet):
        try:
                if packet['PGSQL']['type']=='p':
                        packet['PGSQL']['password']='mal'
                        print('paso')
                        return packet
        except:
                return packet
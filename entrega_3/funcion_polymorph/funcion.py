def delay_2(packet):
        import time as tiempo
        if (packet['TCP']['dstport'] == 5432):
                try:
                        time = int(tiempo.time())
                        try:
                                packet.conjunto[time] = packet.conjunto[time] + (packet['IP']['len'] + 14 ) * 8
                        except:
                                packet.conjunto[time] = (packet['IP']['len'] + 14 ) * 8
                        print (packet.conjunto)
                except:
                        repeticiones = {}
                        packet.global_var('conjunto',repeticiones)
                        packet.conjunto[time] = (packet['IP']['len'] + 14 ) * 8
                        print (packet.conjunto)
        return packet

import threading
import time

from UdpSocket import UdpSocket
from database import Connection
from decimal import Decimal
from packet import Packet
from packetTypes import PacketType

server_ip = "127.0.0.1"
server_port = 5555

class Client:

    def send(self, packet):
        self.outgoing.send(packet, server_ip, server_port)
        
    def __listen(self):
        print("Listening...")
        while True:
            data, server_info = self.incoming.receive();
            if server_info[0] != server_ip or server_info[1] != (server_port + 1): # packet not from server
                continue

            print("DEBUG: ", data)
            
            packet = Packet(raw_data = data)
            type = packet.get_type()
            
            print("DEBUG: Type ->", type)
            
            if type == PacketType.MESSAGE:
                print("message: ", packet.get())
                
            if type == PacketType.PING:
                print("ping from server: ")
                
            if type == PacketType.LOGIN:
                result = packet.get();
                print("DEBUG: Login result ->", result)
                
                
        
    def __init__(self):
        self.incoming = UdpSocket()
        self.incoming.bind(5557)
        
        self.outgoing = UdpSocket()
        self.outgoing.bind(5558)
        
        self.listening_thread = threading.Thread(target=self.__listen, args=(), daemon = True)
        # Database
        # cursor = Connection().getInstance()
        
    def run(self):
        self.running = True;
        self.listening_thread.start()
        while (True):
            self.__test_packets()
            time.sleep(1.0)
    
    def __test_packets(self):
        for i in range(1, len(PacketType)+1):
            print("[", i, "] : ", PacketType(i), sep='')
        packet_type = int(input("[packet type]>"))
        packet = Packet(PacketType(packet_type))
        
        print ('[0] : send')
        print ('add content: ')
        print ('[1] : Decimal')
        print ('[2] : int')
        print ('[3] : float')
        print ('[4] : str')
        
        while True:
            value = int(input("[data type]>"))
            if value == 0:
                self.send(packet)
                break
            elif value == 1:
                dec = input("[Decimal] >")
                packet.add( Decimal(dec) )
            elif value == 2:
                integer = input("[int] >")
                packet.add( int(integer) )
            elif value == 3:
                flt = input("[float] >")
                packet.add( float(flt) )
            elif value == 4:
                str = input("[str] >")
                packet.add( str )
                
                


if __name__ == "__main__":
    client = Client()
    client.run()
    
    
    
    
    
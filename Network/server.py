import threading
import time

from UdpSocket import UdpSocket
from database import Connection
from decimal import Decimal
from packet import Packet
from packetTypes import PacketType

class Server:

    def __listen(self):
        print("Listening...")
        cursor = Connection().getInstance()
        while True:
            data, clientInfo = self.incoming.receive();
            clientIP, clientPort = clientInfo
            
            print("DEBUG: Received from " + clientIP + ":" + str(clientPort))
            print("DEBUG: ", data)
            
            
            packet = Packet(raw_data = data)
            type = packet.get_type()
            
            print("DEBUG: Type ->", type)
            
            if type == PacketType.MESSAGE:
                print("message: ", packet.get())
                
            if type == PacketType.PING:
                outgoing_packet = Packet(PacketType.PING)
                outgoing_packet.add("pong")
                self.outgoing.send(outgoing_packet, clientIP, clientPort)
                
            if type == PacketType.LOGIN:
                outgoing_packet = Packet(PacketType.LOGIN)
                
                login = packet.get();
                password = packet.get();
                print("DEBUG: Login ->", login)
                print("DEBUG: Password ->", password)
                
                querry = "SELECT * FROM `users` WHERE `username`=? AND `password`=?";
                cursor.execute(querry, (login, password))
                
                users = cursor.fetchall()
                if len(users) == 1:
                    user = users[0]
                    print("DEBUG: Login success")
                    outgoing_packet.add(1)
                    self.users.append( [user[0], user[1], clientIP, clientPort] )
                else:
                    print("DEBUG: Login failed")
                    outgoing_packet.add(0)
                
                self.outgoing.send(outgoing_packet, clientIP, clientPort)
                
        
    def __init__(self):
        self.incoming = UdpSocket()
        self.incoming.bind(5555)
        self.users = [] # [ {id}, {username}, {ip}, {port} ]
        
        self.outgoing = UdpSocket()
        self.outgoing.bind(5556)
        
        self.listening_thread = threading.Thread(target=self.__listen, args=(), daemon = True)
        # Database
        # cursor = Connection().getInstance()
        
    def run(self):
        self.running = True;
        self.listening_thread.start()
        while (True):
            time.sleep(1.0)


if __name__ == "__main__":
    s = Server()
    s.run()
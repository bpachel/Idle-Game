import threading
import time
import bcrypt

from decimal import Decimal

from UdpSocket import UdpSocket
from database import Connection
from packet import Packet
from packetTypes import PacketType
from UserRepository import UserRepository, User
from UserCurrencyRepository import UserCurrencyRepository, UserCurrency
from ItemRepository import ItemRepository, Item
from UserEquipmentRepository import UserEquipmentRepository, UserEquipment

class PacketHandler:

    def __init__(self, server, cursor):
        self.cursor = cursor
        self.server = server
        self.userEquipmentRepository = UserEquipmentRepository()
        self.userCurrencyRepository = UserCurrencyRepository()
        self.itemRepository = ItemRepository()
        self.userRepository = UserRepository()

    def handle(self, packet, client_ip, client_port):
        type = packet.get_type()

        print("DEBUG: Type ->", type)
        outgoing_packet = Packet()

        if   type == PacketType.MESSAGE:
            print("message: ", packet.get())
            
        elif type == PacketType.PING:
            outgoing_packet = Packet(PacketType.PING)
            outgoing_packet.add("pong")
            
        elif type == PacketType.LOGIN:
            outgoing_packet = Packet(PacketType.LOGIN)
            
            login = packet.get()
            password = packet.get()
            print("DEBUG: Login ->", login)
            print("DEBUG: Password ->", password)
            
            user = self.userRepository.findOneBy({"username":login})

            print("DEBUG: Hashed Password ->", user.password)

            if bcrypt.checkpw(password.encode(), user.password.encode()):
                print("DEBUG: Login Success.")
                outgoing_packet.add(1)
            else:
                print("DEBUG: Login Failed.")
                outgoing_packet.add(0)

        elif type == PacketType.REGISTER:
            outgoing_packet = Packet(PacketType.REGISTER)
            login = packet.get()
            password = packet.get()
            email = packet.get()

            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode(), salt)
            print("DEBUG: Hashed Password ->", hashed_password)

            user = User()
            user.username = login
            user.password = hashed_password.decode()
            user.email = email
            result = self.userRepository.add(user)

            if result:
                outgoing_packet.add(1)
            outgoing_packet.add(0)
            
        return outgoing_packet

class Server:

    def __listen(self):
        print("Listening...")
        cursor = Connection().getInstance()
        packet_handler = PacketHandler(self, cursor)

        while True:
            data, client_info = self.incoming.receive()
            client_ip, client_port = client_info
            
            print("DEBUG: Received from " + client_ip + ":" + str(client_port))
            print("DEBUG: data: [", data, "]", sep='')
            
            packet = Packet(raw_data = data)
            outgoing_packet = packet_handler.handle(packet, client_ip, client_port)
            if not outgoing_packet.get_size() == 0:
                self.outgoing.send(outgoing_packet, client_ip, client_port)
                
        
    def __init__(self):
        self.incoming = UdpSocket()
        self.incoming.bind(5555)
        self.users = [] # [ {id}, {username}, {ip}, {port} ]
        
        self.outgoing = UdpSocket()
        self.outgoing.bind(5556)
        
        self.listening_thread = threading.Thread(target=self.__listen, args=(), daemon = True)
        
    def run(self):
        self.running = True
        self.listening_thread.start()
        while (True):
            time.sleep(1.0)


if __name__ == "__main__":
    s = Server()
    s.run()
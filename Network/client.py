import threading
import time

from UdpSocket import UdpSocket
from database import Connection
from decimal import Decimal
from packet import Packet
from packetTypes import PacketType

server_ip = "127.0.0.1"
server_port = 5555
server_incoming_port = 5556

class Client:

    def send(self, packet):
        self.socket.send(packet, server_ip, server_port)
        
    def __listen(self, required_packet_type) -> Packet:

        server_info = (0, 0)
        packet_type = None
        packet = None

        # not from server
        while  server_info[0] != server_ip \
        or server_info[1] != server_incoming_port \
        or packet_type != required_packet_type: 
            data, server_info = self.socket.receive(timeout = 5)
            packet = Packet(raw_data = data)
            packet_type = packet.get_type()

        return packet
        """
        print("Listening...")
        while True:
            data, server_info = self.incoming.receive()
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
                result = packet.get()
                print("DEBUG: Login result ->", result)
        """

    def __init__(self):
        self.socket = UdpSocket()
        self.socket.bind(5557)
        
        self.listening_thread = threading.Thread(target=self.__listen, args=(), daemon = True)
        # Database
        # cursor = Connection().getInstance()
        
    def run(self):
        self.running = True
        self.listening_thread.start()
        while (True):
            if self.__test_packets() == 0:
                break
    
    def __test_packets(self):
        for i in range(1, len(PacketType)+1):
            print("[", i, "] : ", PacketType(i), sep='')
        packet_type = int(input("[packet type]> "))
        if packet_type == 0:
            return 0

        packet = Packet(PacketType(packet_type))
        
        print ('[0] : send')
        print ('add content: ')
        print ('[1] : Decimal')
        print ('[2] : int')
        print ('[3] : float')
        print ('[4] : str')
        
        while True:
            value = int(input("[data type]> "))
            if value == 0:
                self.send(packet)
                break
            elif value == 1:
                dec = input("[Decimal]> ")
                packet.add( Decimal(dec) )
            elif value == 2:
                integer = input("[int]> ")
                packet.add( int(integer) )
            elif value == 3:
                flt = input("[float]> ")
                packet.add( float(flt) )
            elif value == 4:
                str = input("[str]> ")
                packet.add( str )
    
    def register(self, username, password, email):
        """
            Register account
            Parameters:
                str 'username'
                str 'password'
                str 'email'
            Returns
                int
                    '0' - failed
                    '1' - success
        """
        
        if username.__class__.__name__ != 'str' \
        or password.__class__.__name__ != 'str' \
        or email.__class__.__name__ != 'str':
            raise TypeError("username, password and email must be 'str'")
        
        packet = Packet(PacketType.REGISTER)
        packet.add(username)
        packet.add(password)
        packet.add(email)
        self.send(packet)

        packet = self.__listen(PacketType.REGISTER)
        return packet.get()

    def login(self, username, password):
        """
            Login to server
            Parameters:
                str 'username'
                str 'password'
            Returns
                int
                    '0' - failed
                    '1' - success
        """
        
        if username.__class__.__name__ != 'str' \
        or password.__class__.__name__ != 'str':
            raise TypeError("username, password must be 'str'")
        
        packet = Packet(PacketType.LOGIN)
        packet.add(username)
        packet.add(password)
        self.send(packet)

        packet = self.__listen(PacketType.LOGIN)
        return packet.get()
    
    def logout(self):
        """
            Logout from server
            Parameters:
                None
            Returns
                int
                    '0' - failed
                    '1' - success
        """
        
        if username.__class__.__name__ != 'str' \
        or password.__class__.__name__ != 'str':
            raise TypeError("username, password must be 'str'")
        
        packet = Packet(PacketType.LOGOUT)
        self.send(packet)

        packet = self.__listen(PacketType.LOGOUT)
        return packet.get()
    
    def get_stats(self):
        """
            Get User Stats
            [Must be logged in]
            Parameters:
                None
            Return dict
                Decimal 'might'
                Decimal 'cunning'
                Decimal 'psyche'
                Decimal 'lore'
                Decimal `gold`
                Decimal `treasure`
                Decimal `might`
                Decimal `cunning`
                Decimal `psyche`
                Decimal `lore`
                Decimal `stamina`
                Decimal `health`
                Decimal `ploy`
                Decimal `spirit`
                Decimal `clarity`
        """
        packet = Packet(PacketType.GET_STATS)

        self.send(packet)

        packet = self.__listen(PacketType.GET_STATS)
        return {
            'gold' : packet.get(),
            'treasure' : packet.get(),
            'might' : packet.get(),
            'cunning' : packet.get(),
            'psyche' : packet.get(),
            'lore' : packet.get(),
            'stamina' : packet.get(),
            'health' : packet.get(),
            'ploy' : packet.get(),
            'spirit' : packet.get(),
            'clarity' : packet.get()
        }

    def get_items(self):
        """
            Get User Items
            [Must be logged in]
            Parameters:
                None
            Returns
                array [ tuple ]
                int 'n'
                    (n times)
                    int 'item_id'
                    bool 'equipped'
        """
        packet = Packet(PacketType.GET_ITEMS)

        self.send(packet)

        packet = self.__listen(PacketType.GET_ITEMS)
        items = []
        n = packet.get()
        print("N:",n)

        for i in range(n):
            item_id = packet.get()
            equipped = packet.get()
            items.append( (item_id, equipped) )
        
        return items

    def get_item_info(self, item_id):
        """
            Get Item Details
            [Must be logged in]
            Parameters:
                int item_id
            Returns: dict
                str 'name'
                str 'type'
                Decimal 'req_might'
                Decimal 'req_cunning'
                Decimal 'req_psyche'
                Decimal 'req_lore'
                Decimal 'might'
                Decimal 'cunning'
                Decimal 'psyche'
                Decimal 'lore'
        """
        packet = Packet(PacketType.GET_ITEM_INFO)
        packet.add(item_id)
        self.send(packet)

        packet = self.__listen(PacketType.GET_ITEM_INFO)

        return {
            'name' : packet.get(),
            'type' : packet.get(),
            'req_might' : packet.get(),
            'req_cunning' : packet.get(),
            'req_psyche' : packet.get(),
            'req_lore' : packet.get(),
            'might' : packet.get(),
            'cunning' : packet.get(),
            'psyche' : packet.get(),
            'lore' : packet.get()
        }
        
        return items

    def save_stats(self, stats):
        """
            Save Stats to Database
            Parameters:
                dict:
                    Decimal 'might'
                    Decimal 'cunning'
                    Decimal 'psyche'
                    Decimal 'lore'
                    Decimal `gold`
                    Decimal `treasure`
                    Decimal `stamina`
                    Decimal `health`
                    Decimal `ploy`
                    Decimal `spirit`
                    Decimal `clarity`
            Returns:
                int
                    '0' - failed
                    '1' - success
        """
        packet = Packet(PacketType.SAVE_STATS)
        packet.add(stats['might'])
        packet.add(stats['cunning'])
        packet.add(stats['psyche'])
        packet.add(stats['lore'])
        packet.add(stats['gold'])
        packet.add(stats['treasure'])
        packet.add(stats['stamina'])
        packet.add(stats['health'])
        packet.add(stats['ploy'])
        packet.add(stats['spirit'])
        packet.add(stats['clarity'])
        self.send(packet)

        packet = self.__listen(PacketType.SAVE_STATS)
        return packet.get()

    def save_items(self, items):
        """
            Save Stats to Database
            Parameters:
                array
                    dict
                        int : item_id
                        int : equipped
            Returns:
                int
                    '0' - failed
                    '1' - success
        """
        packet = Packet(PacketType.SAVE_ITEMS)

        packet.add( len(items) )

        for item in items:
            packet.add(item['item_id'])
            packet.add(item['equipped'])

        self.send(packet)

        packet = self.__listen(PacketType.SAVE_ITEMS)
        return packet.get()  

if __name__ == "__main__":
    import random
    client = Client()
    #client.run()

    # Rejestracja
    username =  "user" + str(random.randrange(10000)) #"user1111"       #
    password =  "password" + str(random.randrange(10000)) #"password1111"   #
    email = "email" + str(random.randrange(10000))

    print ("username:", username)
    print ("password:", password)
    print ("email:", email)
    
    username = "user3275"
    password = "password6220"
    
    if client.register(username, password, email):
        print ("register success.")
    else:
        print ("register failed.")

    # Logowanie
    if client.login(username, password):
        print ("login success.")
    else:
        print ("login failed.")
 
    # Wylogowanie
    #if client.logout():
    #    print ("logout success.")
    #else:
    #    print ("logout failed.")

    # Pobranie statystyk
    stats = client.get_stats()
    for k, v in stats.items():
        print('[{}]: {}'.format(k, v))

    # Pobranie itemow
    items = client.get_items()
    if items:
        for k, v in items:
            print ('v: ', v, ", ", v.__class__.__name__)
            print('[{}]: {}'.format(k, 'equipped' if v else 'in bags'))

    # Pobranie szczegolow itemu
    if items:
        unique_item_id = set() # set zeby nie pobierac kilka razy tego samego
        for k, v in set(items):
            unique_item_id.add(k)

        for item_id in unique_item_id:
            item_info = client.get_item_info(item_id)
            print(item_info)

    # Zapisanie statystyk
    
    if client.save_stats({
        'gold' : 100,
        'treasure' : 2,
        'might' : 6,
        'cunning' : 8,
        'psyche' : 12,
        'lore' : 24,
        'stamina' : 254,
        'health' : 1280,
        'ploy' : 13,
        'spirit' : 8,
        'clarity' : 6
    }):
        print ("save_stats success.")
    else:
        print ("save_stats failed.")
    
    if client.save_items([
        { "item_id" : 1, "equipped" : 0},
        { "item_id" : 2, "equipped" : 0},
        { "item_id" : 1, "equipped" : 0},
        { "item_id" : 1, "equipped" : 1}
    ]):
        print ("save_items success.")
    else:
        print ("save_items failed.")
    
    
    
    
import threading

from UdpSocket import UdpSocket;

class Server:

    def __listen__(self):
        print("Listening...")
        while True:
            data, client = self.incoming.receive();
            print("Received from " + client[0] + ":" + str(client[1]))
            print("\t", data)
            
            if data == b'ping':
                self.outgoing.send('pong', client[0], client[1])
        
    def __init__(self):
        self.incoming = UdpSocket()
        self.incoming.bind(5555)
        
        self.outgoing = UdpSocket()
        self.outgoing.bind(5556)
        
        self.listening_thread = threading.Thread(target=self.__listen__, args=(), daemon = True)
        # Database
        # cursor = Connection().getInstance()
        
    def run(self):
        self.running = True;
        self.listening_thread.start()
        while (True):
            pass


if __name__ == "__main__":
    s = Server()
    s.run()
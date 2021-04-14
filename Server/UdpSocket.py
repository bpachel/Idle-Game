import socket
import packet
from decimal import Decimal

class UdpSocket:

    def __create__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    
    def __close__(self):
        self.sock.close()
        
    def __init__(self):
        self.__create__()
        
    def __del__(self):
        self.__close__()
    
    def get_local_port(self) -> int:
        return self.sock.getsockname()[1]
        
    def bind(self, port):
        """
            Bind the socket to a specific port
            
            @param: port    Port to bind the socket to
        """
        self.sock.bind( ('localhost', port) )
        
    def send(self, data, server_ip, server_port):
        """
            Send data to a remote peer
            @param: data          Data to send
            @param: remoteAddress Address of the receiver
            @param: remotePort    Port of the receiver to send the data to
        """
        sent = self.sock.sendto(data.encode(), (server_ip, server_port))
        if sent < 0:
            raise Exception('Failed to send data');
        
    def receive(self):
        """
            Receive data from a remote peer
           
            This function will WAIT UNTIL the whole packet
            has been received.
           
            @return: (data, remote_address)
        """
        data, server = self.sock.recvfrom(4096)
        return data, server
        
if __name__ == "__main__":   
    
    sock = UdpSocket()
    message = 'ping'
    sock.send(message, "127.0.0.1", 5555)
    data, server = sock.receive()
    print(data)
    #print(data, server);










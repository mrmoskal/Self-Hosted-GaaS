import socket

HOSTNAME = socket.gethostname()
PORTS = { "VIDEO": 8001, "SOUND": 8002, "INPUT": 8003 }
# POSSIBLE_CONNECTIONS = 1

class ScreenCpture: 
    def __init__(self):
        self.videoSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def start(self):
        self.videoSocket.bind((HOSTNAME, PORTS["VIDEO"]))
        print(f"[server][info] ==> server listening on {HOSTNAME}:{PORTS["VIDEO"]}")

        self.data = ""
        while not self.data:
            clientData, clientAddress = self.videoSocket.recvfrom(4096)
            print(f"connection (from {clientAddress}) = data: {clientData}")
            self.videoSocket.sendto(bytes("test message from server", "utf-8"), clientAddress)
            self.data = clientData
        
        self.videoSocket.close()

def main():
    print(HOSTNAME)
    handler: ScreenCpture = ScreenCpture()
    handler.start()

if __name__ == "__main__":
    main()
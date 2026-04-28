import socket

SERVER_ADDR = "10.100.102.8"
SERVER_PORTS = { "VIDEO": 8001, "SOUND": 8002, "INPUT": 8003 }

def main():
    clientVideoSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverVideoSocketAddr = (socket.gethostname(), SERVER_PORTS["VIDEO"]) 

    clientVideoSocket.sendto(bytes("[client][request] ==> Send data please! I'm on my hands and knees!!", "utf-8"), serverVideoSocketAddr)
    data, addr = clientVideoSocket.recvfrom(65535)
    print(f"[client] Message from server {addr} ==> data: {str(data)}")


if __name__ == "__main__":
    main()
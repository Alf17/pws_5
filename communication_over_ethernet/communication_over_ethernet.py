from socket import *
import time

address = ( '192.168.8.243', 5000) #Defind who you are talking to (must match arduino IP and port)
client_socket = socket(AF_INET, SOCK_DGRAM) #Set Up the Socket
client_socket.settimeout(1) #only wait 1 second for a resonse

while(1): #Main Loop

    data = str.encode("Blue") #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(5001) #Read response from arduino
        print(rec_data) #Print the response from Arduino
    except:
        pass

    time.sleep(2) #delay before sending next command

    data = str.encode("Red") #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(5001) #Read response from arduino
        print(rec_data) #Print the response from Arduino
    except:
        pass

    time.sleep(2) #delay before sending next command

    data = str.encode("Green") #Set data to Blue Command
    client_socket.sendto(data, address) #send command to arduino
    try:
        rec_data, addr = client_socket.recvfrom(5001) #Read response from arduino
        print(rec_data) #Print the response from Arduino
    except:
        pass
    time.sleep(2) #delay before sending next command
import socket
import csv

def sendData():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('172.20.241.9', 20000))
        s.sendall(b'25\n')
        received_data = s.recv(1024)
        if not received_data:
            print("No data received from server.")
            return None
        else:
            print("Data received from server:")
            return received_data

def makeCSV(data):
    decoded_data = data.decode('utf-8')
    rows = decoded_data.split('\n')
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row:  
                writer.writerow(row.split(','))
    print("Data written to output.csv")


def main():
    data = sendData()
    if data:
        makeCSV(data)



if __name__ == "__main__":
    main()
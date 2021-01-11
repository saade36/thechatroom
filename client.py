import threading, socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

nick = input('Enter a nickname: ')


def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nick.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occurred')
            client.close()
            break


def write():
    while True:
        message = f'{nick}: {input("")}'
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=recieve)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
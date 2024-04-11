import socket

HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 8080        # Port sur lequel le serveur écoute

# Création d'un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((HOST, PORT))

# Envoi de données au serveur
client_socket.sendall(b"Bonjour, serveur !")

# Réception de la réponse du serveur
data = client_socket.recv(1024)
print(f"Réponse du serveur : {data.decode('utf-8')}")

# Fermeture de la connexion avec le serveur
client_socket.close()


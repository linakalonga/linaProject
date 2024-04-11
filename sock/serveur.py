import socket

# Configuration du serveur
HOST = '127.0.0.1'  # Adresse IP du serveur
PORT = 8080        # Port sur lequel le serveur écoute

# Création d'un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison du socket à l'adresse et au port spécifiés
server_socket.bind((HOST, PORT))

# Attente de connexions entrantes (maximum 1 client à la fois)
server_socket.listen(1)
print(f"Le serveur écoute sur {HOST}:{PORT}...")

while True:
    # Accepter une nouvelle connexion
    client_socket, client_address = server_socket.accept()
    print(f"Connexion entrante de {client_address}")

    try:
        # Recevoir des données du client
        data = client_socket.recv(1024)
        if data:
            # Afficher les données reçues
            print(f"Données reçues du client : {data.decode('utf-8')}")

            # Envoyer une réponse au client
            client_socket.sendall(b"Message reçu par le serveur. Merci !")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        # Fermer la connexion avec le client
        client_socket.close()


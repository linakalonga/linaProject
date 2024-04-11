import requests

# URL de l'API
base_url = 'http://127.0.0.1:5000'  # verifier le port de flask


# Exemple de requête GET
response = requests.get(f'{base_url}/data/my_key')
print(response.json())

# Exemple de requête POST
data_to_post = {'key': 'new_key', 'value': 'new_value'}
response = requests.post(f'{base_url}/data', json=data_to_post)
print(response.json())

# Exemple de requête PUT
data_to_put = {'value': 'updated_value'}
response = requests.put(f'{base_url}/data/new_key', json=data_to_put)
print(response.json())

# Exemple de requête DELETE
response = requests.delete(f'{base_url}/data/new_key')
print(response.json())


from db import insert_client

sample_clients = [
    {"name": "John Doe", "email": "jd@example.com", "company": "Spec LLC"},
    {"name": "Jane Doe", "email": "jdoe@example.com", "company": "Spec LLC"},
    {"name": "Bob Alice", "email": "ba@example.com", "company": "Pythonics LLC"}
]

for client in sample_clients:
    insert_client(client)

print("Test data inserted.")

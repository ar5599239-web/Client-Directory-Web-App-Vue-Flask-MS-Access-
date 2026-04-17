from db import insert_client

sample_clients = [
    {"name": "John Carter", "email": "john.carter@email.com", "company": "Carter Solutions"},
    {"name": "Lisa Monroe", "email": "lisa.monroe@email.com", "company": "Monroe Tech"},
    {"name": "David Kim", "email": "david.kim@email.com", "company": "Kim Consulting"}
]

for client in sample_clients:
    insert_client(client)

print("Test data inserted.")
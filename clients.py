clients = {}


def add_client():
    client_id = input("Enter client ID: ")
    name = input("Enter client name: ")
    email = input("Enter client email: ")

    if client_id in clients:
        print("Client ID already exists. Please use a unique ID.")
    else:
        clients[client_id] = {"name": name, "email": email}
        print("Client added successfully!")


def get_clients():
    return clients

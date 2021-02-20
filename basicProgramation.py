
import sys
import csv
import os

CLIENT_TABLE='.clients.csv'
CLIENT_SCHEMA=['name','company','email','position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name,mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)


def create_client(client):
    if (client not in clients):
        clients.append(client)
    else:
        print('Client already is  in client\'s list')

def list_clients():
    for idx, client in enumerate(clients):
        info = _get_client_info(client)
        print(" {uid} | {clientInfo} ".format(
            uid=idx,
            clientInfo=info))


def _get_client_info(client):
    return "{name} | {company} | {email} | {position}".format(
        name=client['name'],
        company=client['company'], 
        email=client['email'],
        position=client['position'])
    

def update_client(client, update_client):
    if(client in clients):
        clients[clients.index(client)] = update_client 
    else:
        _client_no_exist()


def delete_client(client):
    if(client in clients):
        clients.remove(client)
    else: 
        _client_no_exist()


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*'*50)
    print('What would like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')  
    print('[L]ist clients')
    print('[F]inish program')


def _print_options_search():
    print('Fields for serach client in register')
    print('*'*50)
    print('For what would like search now?')
    print('[N]ame')
    print('[C]ompany')
    print('[E]mail')
    print('[P]osition')


def _print_menu():
    print('-'*50)
    print('What would like to do now?')
    print('-'*50)
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[L]ist clients')
    print('[F]inish program')
    print('-'*50)

def _get_client_field(field):
    client_field = None
    while not client_field:
        client_field = input('What is the client {}?: '.format(field))

        if client_field=='exit':
            client_field = None
            break
    if not client_field:
        sys.exit()
    return client_field


def _get_client_update (client):
    update_client = {}
    name = input("What is the new client name, push intro for not modify field: ")
    if(name == ''):
        name = client['name']
    company = input("What is the new company for this client, push intro for not modify field: ")
    if(company == ''):
        company = client['company']
    email = input("What is the new email for this client, push intro for not modify field: ")
    if(email == ''):
        email = client['email']
    position = input("What is the new position for this client, push intro for not modify field: ")
    if(position == ''):
        position = client['position']
    update_client['name'] = name
    update_client['company'] = company
    update_client['email'] = email
    update_client['position'] = position

    return update_client


def _definition_filed():

    _print_options_search()
    option = input()

    while not option:
        option = input()

        if option=='exit':
            option = None
            break
    if not option:
        sys.exit()

    option.upper()
    if option == 'N':
        return 'name'
    elif option == 'C':
        return 'company'
    elif option == 'E':
        return 'email'
    elif option == 'P':
        return 'position'
    else:
        return print('the option selected is not aviable')

def _search_client_for_field(field_name, field_value):
    for client in clients:
        if client[field_name] == field_value:
            return client

    return _client_no_exist()

def _get_client_name():
    client_field = None
    while not client_field:
        client_field = input('What is the client name? ')

        if client_field=='exit':
            client_field = None
            break
    if not client_field:
        sys.exit()
    return client_field

def _client_no_exist():
    return print("Client is not in clients list")

if __name__ == '__main__':
    
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()
    while(command != 'F'):
        """ Create client in app """
        
        if(command == 'C'):
            client = {
                'name': _get_client_field('name'),
                'company':_get_client_field('company'),
                'email':_get_client_field('email'),
                'position': _get_client_field('position')
            }
            create_client(client)
            list_clients()
        # Delete client in
        elif (command == 'D'):
            field = _definition_filed()
            client = _search_client_for_field(field,_get_client_field(field))
            delete_client(client)
        elif (command == 'U'):
            field = _definition_filed()
            client = _search_client_for_field(field,_get_client_field(field))
            update_client(client,_get_client_update(client))
        elif (command == 'S'):
            field = _definition_filed()
            client = _search_client_for_field(field,_get_client_field(field))
            print(_get_client_info(client))
        elif (command == 'L'):
            list_clients()
        else:
            print('Invalid option')

        _print_menu()
        command = input()

    _save_clients_to_storage()
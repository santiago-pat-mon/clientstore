import click

from clients.services import ClientService
from clients.models import Client
@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass        


@clients.command()
@click.option('-n','--name',
              type=str,
              prompt=True,
              help='the client name')
@click.option('-a','--adress',
              type=str,
              prompt=True,
              help='the client adress')
@click.option('-e','--email',
              type=str,
              prompt=True,
              help='the client email')
@click.option('-p','--celphone',
              type=str,
              prompt=True,
              help='the client celphone')
@click.pass_context
def create(ctx, name, adress, email, celphone):
    """Create a new client"""
    client = Client(name,adress,email,celphone)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients """
    
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    click.echo('  ID  |  NAME  |  ADRESS  |  E-MAIL  | CELPHONE')
    click.echo('-'*50)
    
    for client in clients_list:
        
        click.echo('{uid} | {name} | {adress} | {email} | {celphone}'.format(
            uid = client['uid'],
            name = client['name'],
            adress = client['adress'],
            email = client['email'],
            celphone=client['celphone'],))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Update a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.adress = click.prompt('New adress', type=str, default=client.adress)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.celphone = click.prompt('New celphone', type=str, default=client.celphone)

    return client

@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Delete Client """
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_uid]
    if client:
        client_service.delete_client(client)
        click.echo('Client removed successfully')
    else:
        click.echo('Client not found in data base')

all = clients

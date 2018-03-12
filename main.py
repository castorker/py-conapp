import sys
from quibble import Quibble
from quibble_data_service import QuibbleDataService


def list_quibbles():
    """Retrieves all the quibbles and show them"""
    quibbles = data_service.get_all()
    if quibbles:
        for quibble in quibbles:
            print(f"{quibble.id}) {quibble.text} - {quibble.category}")
    else:
        print("Quibble list empty")


def enter_quibble():
    """Gets data to create a new quibble"""
    print("---------------")
    print("Category of quibble? ")
    category = input()
    print("Text? ")
    text = input()
    quibble = Quibble()
    quibble.text = text
    quibble.category = category
    data_service.create(quibble)


def query_quibble(quibble_id):
    """
    Retrieves a specific quibble by identifier and prompt the user to edit or delete it
    :param quibble_id: int - quibble id to query
    """
    quibble = data_service.get_by_id(quibble_id)
    if quibble is not None:
        print(f"{quibble.id}) {quibble.text}:")
        print(f"{quibble.category}")
        print("---------------")
        print("E) Edit quibble")
        print("D) Delete quibble")
        print("C) Continue")
        print("Please enter a command: ")
        command = input().upper()
        if command[:1] == "E":
            print(f'Editing Quibble {quibble_id}')
            edit(quibble_id)
        elif command[:1] == "D":
            print(f'Deleting quibble {quibble_id}')
            delete(quibble_id)
    else:
        print(f"There is no quibble with the id {quibble_id}")


def edit(quibble_id):
    """
    Gets data to update the current quibble
    :param quibble_id:
    """
    print("---------------")
    print("Category of quibble? ")
    category = input()
    print("Text? ")
    text = input()
    quibble = Quibble()
    quibble.id = quibble_id
    quibble.text = text
    quibble.category = category
    data_service.update(quibble)


def delete(quibble_id):
    """
    Gets confirmation to delete the current quibble
    :param quibble_id:
    """
    print("---------------")
    print("Are you sure you want to delete this quibble? (Y/N) ")
    answer = input().upper()
    if answer == "Y":
        data_service.delete(quibble_id)


# Program entry point
data_service = QuibbleDataService()
selection = ""
while selection[:1].upper() != "Q":
    print("---------------")
    print("L) List quibbles")
    print("#) Query specific quibble")
    print("N) Enter a new quibble")
    print("Q) Quit")
    print("Please enter a command: ")
    selection = input().upper()

    if selection[:1] == "L":
        print('Showing Quibbles')
        list_quibbles()
    elif selection[:1] == "N":
        print('Creating new quibble')
        enter_quibble()
    else:
        try:
            quibble_id_to_query = int(selection[:1])
        except ValueError:
            print('Quitting Quibbles')
            quibble_id_to_query = None
        else:
            print('Querying Quibbles')
            query_quibble(quibble_id_to_query)

sys.exit(0)

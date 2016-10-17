#!/usr/bin/python3

from map import rooms
from kirill import *
from items import *
from gameparser import *


def list_of_items(items):
    iteml = ""
    for item in items:
        iteml = iteml + ", " + item["name"]
    iteml = iteml[2:]
    return iteml

def print_room_items(room):
    items = room["items"]
    if len(items) != 0:
        print("There is " + list_of_items(items) + " here.")
        print("")

def print_inventory_items(items):
    print("You have " + list_of_items(inventory) + ".")
    print("")

def print_room(room):
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    for i in room_items:
        print("TAKE " + i["id"].upper() + " to take " + i["name"] + ".")
    for i in inv_items:
        print("DROP " + i["id"].upper() + " to drop your " + i["name"] + ".")
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def execute_go(direction):
    global current_room
    exits = current_room['exits']
    if is_valid_exit(exits, direction):
        current_room = move(exits, direction)
    else:
        print("You cannot go there.")

def execute_take(item_id):
    for item in current_room["items"]:
        if item_id == item["id"]:
            inventory.append(item)
            current_room["items"].remove(item)
            return
    print("You cannot take that.")
#
#
# IMPORTANT
# Need to add a use command into here, possibly to replace drop. If you know how to do it just do it and tell us lol
#
#
def execute_drop(item_id):
    for item in inventory:
        if item_id == item["id"]:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("You cannot drop that.")

def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room, or in this case scene of the game
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()


#!/usr/bin/python3

from map import rooms
from kirill import *
from items import *
from gameparser import *
from extras import *


def list_of_items(items):
    iteml = ""
    for item in items:
        iteml = iteml + ", " + item["id"]
    iteml = iteml[2:]
    return iteml

def print_room_items(room):
    items = room["items"]
    if len(items) != 0:
        print("There is " + list_of_items(items) + " here.")
        print("")

def print_inventory_items(items):
    if len(items) != 0:
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
    if current_room == rooms["Fight"]:
        print("HEROICALLY " + direction.upper() + " to defeat her.")
    if current_room != rooms["Fight"]:
        print("GO " + direction.upper() + " to " + leads_to + ".")

def print_menu(exits, room_items, inv_items):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))
    if len(room_items) != 0:
        print("TAKE " + list_of_items(room_items).upper() + " to take item(s).")
    if len(inv_items) != 0:
        print("DROP or EXAMINE your " + list_of_items(inv_items).upper() + " to drop/examine item(s).")
    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits

def try_enter_room(exits, direction):
    global current_room
    room = rooms[exits[direction]]
    if "requirements" in room:
        requirement = room["requirements"]
        item = requirement["item"]
        if item in inventory:
            inventory.remove(item)
            print(requirement["item_held"])
            del room["requirements"]
            current_room = move(exits, direction)
        else:
            print(requirement["item_missing"])
    else:
        current_room = move(exits, direction)

def execute_go(direction):
    global current_room
    exits = current_room['exits']
    if is_valid_exit(exits, direction):
        try_enter_room(exits, direction)
    else:
        print("This isn't Elder Scrolls, move where we tell you to.")

def execute_take(item_id):
    for item in current_room["items"]:
        if item_id == item["id"]:
            inventory.append(item)
            current_room["items"].remove(item)
            return
    print("You have not the power to take items from anywhere you want. Not quite, anyway.")

def execute_examine(item_id):
    for item in inventory:
        if item_id == item["id"]:
            print(str(item["name"]).upper() + ":")
            print(item["description"])
            return
    print("You attempt to examine something you don't have, and you fail miserably.")

def execute_drop(item_id):
    for item in inventory:
        if item_id == item["id"]:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("You didn't drop anything and you looked like a fool.")

def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go" or command[0] == "heroically":
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
    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
    else:
        print("Please English better, that made no sense.")


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
    global current_room
    print(intro)
    input("Press Enter to Continue")
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        if current_room == rooms["FinishHim"]:
            complete = show_outro()
            if complete:
                break
            else:
                current_room = rooms["PrintThreat"]
                continue

        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

def show_outro():
    print("C:\\users\Kirill\Protectotron> Hello Master. Have you got something to tell me?")
    machine_input = input("C:\\users\Kirill\Protectotron> ")
    if machine_input == "mylittlepony99":
        print(ending_win)
        return True
    else:
        print("C:\\users\Kirill\Protectotron> That input is not recognised. Subject being ejected from area.")
        return False

# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()


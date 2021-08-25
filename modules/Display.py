from typing import Optional


class Display:
    @staticmethod
    #display menu
    def display():
        with open("./data/list.txt", "r") as file:
            for line in file:
                print(line.strip())

        print(
            "\ninput 'D'  to delete an item on the list\n"+
            "input 'A'  to add item to the list\n"+
            "input 'CA' to clear all items on the list\n"+
            "input 'R'  to reset all item to false or none\n"+
            "input 'E'  to exit\n"
        )
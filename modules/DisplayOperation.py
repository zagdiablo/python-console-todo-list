import os

from modules.InputOutputOperation import IOOperation as io


#display operation
class Display:
    #display list items
    @staticmethod
    def displayList():
        os.system("clear")
        print(
            f"+---------------------------------------+\n"+
            f"|              Listed Items:            |\n"+
            f"+--+--------+---------------------------+\n"+
            f"|No| status |           title           |\n"+
            f"+--+--------+---------------------------+"
        )
        for data, status in zip(io.ListData, io.ListDataStatus):
            print(
                f"|{io.ListData.index(data)+1}.| {status} | {data}"
            )


    #display user options
    @staticmethod
    def displayOptions():
        print(
            f"+--+--------+---------------------------+\n"+
            f"|input 'A' to add an item to the list   |\n"+
            f"|input 'D' to delete an item on the list|\n"+
            f"|input 'S' to save list                 |\n"+
            f"|input 'R' to reset list                |\n"+
            f"|input 'E' or press ctrl+c to exit      |\n"+
            f"+---------------------------------------+"
        )


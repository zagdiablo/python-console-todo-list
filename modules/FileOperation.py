from modules.Display import Display
import os


class FileOperation:
    #check if file exist
    @staticmethod
    def checkFile():
        file = os.path.exists("./data/list.txt")

        if(file):
            return True
        FileOperation.createDataFile()


    #create data file
    @staticmethod
    def createDataFile():
        file = open("./data/list.txt", "w")
        file.close()
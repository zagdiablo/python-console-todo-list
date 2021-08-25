# obj:
# clear all, delete 1, delete all are Required
# able to add new matkul to the list and delete it based on needs


import modules.Display as dp
import modules.FileOperation as fo


def main():
    #display all on the list
    fo.FileOperation.checkFile()
    dp.Display.display()


    

if __name__ == "__main__":
    main()
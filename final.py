from pacs.Branch.secure import secure
from pacs.Branch.faceRecognition3 import faceRecognition3

while 1:
    x = input("enter 1 for advance and 2 for Normal and 'q' for quitting the program: ")
    if x == '1':
        f = faceRecognition3()
        f.adva()

    elif x == '2':
        normal = secure()
        normal.norm()

    elif x == 'q':
        break

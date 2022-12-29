import cv2
from datetime import datetime

class notify:
    def __init__(self, cap):
        self.cap1 = cap

    def pic(self, cap, fr):
        self.cap1 = cap

        while 1:
            original_frame = fr.copy()
            cv2.imwrite('p.png', original_frame)

            permission = input("If you want to allow this person press 'y' if not then 'n': ")
            if permission == 'y':
                print("Door is unlock for you 5 sec.")
            else:
                print("you are not allow....")

            break
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
#DETECTING IF SOMEONE BREAKING THE HOUSE
import cv2
import winsound

class secure:

    def __init__(self):
        self.cam = int(input("enter camera: "))
        # self.cam = int(input("enter camera: "))
        self.cap = cv2.VideoCapture(self.cam)
        self.key = cv2.waitKey(1)

    def norm(self):

        while True:
            _, frame1 = self.cap.read()
            frame1 = cv2.resize(frame1, (600, 400))
            _, frame2 = self.cap.read()
            frame2 = cv2.resize(frame2, (600, 400))
            diff = cv2.absdiff(frame1, frame2)
            gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv2.contourArea(c) < 5000:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print("wake up dude someone coming to your home")
                winsound.Beep(2500, 500)
                break

            self.key = cv2.waitKey(1)

            # stop if q is pressed
            if self.key == ord('q'):
                break
            cv2.imshow('Dibya', frame1)



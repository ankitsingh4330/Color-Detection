import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    # Yellow color
    lower_yellow = np.array([20,100,100])
    upper_yellow = np.array([35,255,255])

    # Blue color
    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    lower_orange = np.array([10, 100, 20])
    upper_orange = np.array([25, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 50, 200])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    '''
    mask_black = cv2.inRange(hsv, lower_black, upper_black)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_orange= cv2.inRange(hsv, lower_orange, upper_orange)
    mask_white= cv2.inRange(hsv, lower_white, upper_white)
    mask_gray= cv2.inRange(hsv, lower_gray, upper_gray)
    '''

    # Function to draw box and label
    def detect_color(mask, color_name):

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area > 500:

                x,y,w,h = cv2.boundingRect(cnt)

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,color_name,(x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    detect_color(mask_red, "Red")
    detect_color(mask_yellow, "Yellow")
    detect_color(mask_blue, "Blue")
    '''
    detect_color(mask_black, "Black")
    detect_color(mask_green, "Green")
    detect_color(mask_orange, "Orange")
    detect_color(mask_white, "White")
    detect_color(mask_gray, "Gray")
    '''


    cv2.imshow("Multi Color Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
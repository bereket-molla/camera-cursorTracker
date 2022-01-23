import cv2
import numpy as np
import pyautogui
center = (0, 0)
captured = cv2.VideoCapture(1)
realContour = []
x_coordinate = 100
y_coordinate = 100
def mapd2v(degree):
    value = (0.70833) * degree
    return value
def mapp2v(percentage):
    value = (2.55) * percentage
    return value
def map_location_x(camLocation):
    screen_location = 2.276 * camLocation
    return screen_location

def map_location_y(camLocation):
    screen_location = 1.92 * camLocation
    return screen_location

def finger_color_detection(color):
    global center
#    if color == 'blue':
#        high = np.array([mapd2v(225), mapp2v(100), mapp2v(100)])
#        low = np.array([mapd2v(160), mapp2v (45), mapp2v(50)])
    if color == 'red':
        high = np.array([mapd2v(25), mapp2v(100), mapp2v(100)])
        low = np.array([mapd2v(0), mapp2v (45), mapp2v(50)])
    elif color == 'green':
        high = np.array([mapd2v(129), mapp2v(100), mapp2v(100)])
        low = np.array([mapd2v(95), mapp2v (60), mapp2v(55)])
    elif color == 'yellow':
        high = np.array([mapd2v(60), mapp2v(100), mapp2v(100)])
        low = np.array([mapd2v(38), mapp2v (43), mapp2v(50)])
    else:
        print ('abort')


    # trueContour = largest_contour()
    _, frame = captured.read()
    Hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    median = cv2.medianBlur(Hsv, 15)
    mask = cv2.inRange(Hsv, low, high)
    res = cv2. bitwise_and(frame, frame, mask = mask)
    dilation = cv2.dilate(mask, np.ones((20, 20), "uint8"))
    # noNoise = cv2.filter2D(res, -1, kernel)

    _, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        #print (cv2. contourArea(contour))
        if cv2. contourArea(contour) > 2000:
            cv2.drawContours(frame, contour, -1, (0, 0, 255), 5)
            (x,y),radius   = cv2.minEnclosingCircle(contour)
            center  =(int(x),int(y))
            radius  = int(radius)
            cv2.circle(frame,center,radius,(255,0,0),2)
            height, width, channels = frame.shape
            return center



    cv2.imshow("input",frame)
    cv2.imshow("masked", mask)
    cv2.imshow("res", median)


    k = cv2.waitKey(1)
    cv2.destroyAllWindows()
    #cv2.imshow('ds', frame)
def mouse_movement():
    global y_coordinate
    global x_coordinate

    while True:

        location = finger_color_detection('yellow')
        click_location = finger_color_detection('green')
        print(click_location)
        if location != None:
            #print(location)
            x_coordinate = location[0]
            y_coordinate = location[1]
            pyautogui.moveTo(1366 - map_location_x(x_coordinate), map_location_y(y_coordinate))
            if click_location != None:
                print("click!")
                pyautogui.click(1366 - map_location_x(x_coordinate), map_location_y(y_coordinate))
        else:
            print("your finger is not detected please try and get it in to field of view")
            continue


def main():
    mouse_movement()
if __name__ == '__main__':
    main()

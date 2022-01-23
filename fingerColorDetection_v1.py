import cv2
import numpy as np

captured = cv2.VideoCapture(0)

def mapd2v(degree):
    value = (0.70833) * degree
    return value

def mapp2v(percentage):
    value = (2.55) * percentage
    return value


def finger_color_detection():
    highYellow = np.array([mapd2v(60), mapp2v(100), mapp2v(100)])
    lowYellow = np.array([mapd2v(38), mapp2v (43), mapp2v(50)])


    # trueContour = largest_contour()


    while True:
        _, frame = captured.read()
        Hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        median = cv2.medianBlur(Hsv, 15)
        mask = cv2.inRange(Hsv, lowYellow, highYellow)
        res = cv2. bitwise_and(frame, frame, mask = mask)
        dilation = cv2.dilate(mask, np.ones((20, 20), "uint8"))
        # noNoise = cv2.filter2D(res, -1, kernel)

        _, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_TREE)
        for contour in contours:
            #print (cv2. contourArea(contour))
            if cv2. contourArea(contour) > 2500:
                cv2.drawContours(frame, contour, -1, (0, 0, 255), 5)
                (x,y),radius   = cv2.minEnclosingCircle(contour)
                center  =(int(x),int(y))
                radius  = int(radius)
                print(center)
                cv2.circle(frame,center,radius,(255,0,0),2)
                height, width, channels = frame.shape




        cv2.imshow("input",frame)
        cv2.imshow("masked", mask)
        cv2.imshow("res", median)


        k = cv2.waitKey(1)
        if k == 27:
            break
    cv2.destroyallwindows()
def main():
    finger_color_detection()
if __name__ == '__main__':
    main()

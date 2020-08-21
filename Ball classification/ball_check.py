import cv2
import numpy as np

min=30    #min area
color_boundaries = [ ([0, 0, 220], [30, 30, 255]), ([0, 220, 0], [30, 255, 30])]    #red[0] and green[1]
images = ['test1.jpeg', 'test2.jpeg', 'test3.jpeg', 'test4.jpeg', 'test5.jpeg']

for image in images:
    img = cv2.imread(image, 1)
    img = cv2.resize(img, (550, 550))

    masks = []
    for (low, up) in color_boundaries:
        low=np.array(low, dtype='uint8')
        up=np.array(up, dtype='uint8')
        mask=cv2.inRange(img, low, up)
        op=cv2.bitwise_and(img, img, mask=mask)
        masks.append(op)

    red_zone = cv2.cvtColor(masks[0], cv2.COLOR_BGR2GRAY)
    green_zone = cv2.cvtColor(masks[1], cv2.COLOR_BGR2GRAY)

    _, red_zone = cv2.threshold(red_zone, 20, 255, cv2.THRESH_BINARY)
    _, green_zone = cv2.threshold(green_zone, 20, 255, cv2.THRESH_BINARY)

    contours_red, hierarchy = cv2.findContours(red_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, hierarchy = cv2.findContours(green_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours_red:
        if(cv2.contourArea(cnt)>min):
            print("Push the Red!")
    for cnt in contours_green:
        if(cv2.contourArea(cnt)>min):
            print("Grab the Green")

# def is_ball():
#     img = cv2.imread(image, 1)
#     img = cv2.resize(img, (550, 550))
#
#     masks = []
#     for (low, up) in color_boundaries:
#         low=np.array(low, dtype='uint8')
#         up=np.array(up, dtype='uint8')
#         mask=cv2.inRange(img, low, up)
#         op=cv2.bitwise_and(img, img, mask=mask)
#         masks.append(op)
#
#     red_zone = cv2.cvtColor(masks[0], cv2.COLOR_BGR2GRAY)
#     green_zone = cv2.cvtColor(masks[1], cv2.COLOR_BGR2GRAY)
#
#     _, red_zone = cv2.threshold(red_zone, 20, 255, cv2.THRESH_BINARY)
#     _, green_zone = cv2.threshold(green_zone, 20, 255, cv2.THRESH_BINARY)
#
#     contours_red, hierarchy = cv2.findContours(red_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours_green, hierarchy = cv2.findContours(green_zone, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     for cnt in contours_red:
#         if(cv2.contourArea(cnt)>min):
#             M = cv2.moments(cnt)
#             cx = int(M['m10']/M['m00'])
#             cy = int(M['m01']/M['m00'])
#             print("Push the Red!")
#     for cnt in contours_green:
#         if(cv2.contourArea(cnt)>min):
#             M = cv2.moments(cnt)
#             cx = int(M['m10']/M['m00'])
#             cy = int(M['m01']/M['m00'])
#             print("Grab the Green")

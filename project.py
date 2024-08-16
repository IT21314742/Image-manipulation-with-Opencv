import cv2

img = cv2.imread('assets/1.jpg', 1)
img = cv2.resize(img, (0, 0), fx=2, fy=0.5)

cv2.imshow('IMAGE', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2

img = cv2.imread("D:\PROJECTS\Color detection\python-project-color-detection\colorpic.jpg",1)

cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()
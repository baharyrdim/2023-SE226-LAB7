import cv2
img = cv2.imread("C:\\Users\\BAHAR\\Desktop\\fb.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Fenerbahce",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

blue,green,red = cv2.split(img)
cv2.imshow("blue",blue)
cv2.imshow("green",green)
cv2.imshow("red",red)

cv2.waitKey(0)
cv2.destroyAllWindows()
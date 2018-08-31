import cv2
import glob
"""
img = cv2.imread("galaxy.jpg",0)

print((img))
resize_image = cv2.resize(img,(500,500))
cv2.imshow("Gal",resize_image)
cv2.waitKey(20000)
cv2.destroyAllWindows()
"""
images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image,0)
    re = cv2.resize(img,(100,100))
    cv2.imshow("hey",re)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re)

import cv2


#Load image
image = cv2.imread("cat.png")

# Blur the image


gauss = cv2. GaussinaBlur(image, (7,7), 0)

#unsharp_image = cv2.addweighted(image, 2, gauss, -1, 0)ss

cv2.imshow("high boost filtering", unsharp_image)

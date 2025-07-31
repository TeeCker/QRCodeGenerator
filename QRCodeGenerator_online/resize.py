import cv2

img = cv2.imread('qr.png', cv2.IMREAD_UNCHANGED)
# Get original height and width
print(f"Original Dimensions : {img.shape}")

# resize image by specifying custom width and height
#resized = cv2.resize(img, (512, 600), interpolation = cv2.INTER_AREA)
resized_image = cv2.resize(img, (512, 600), interpolation=cv2.INTER_AREA)

print(f"Resized Dimensions : {resized_image.shape}")
cv2.imwrite('resized_qr.png', resized_image)
#cv2.imshow("Resized image", resized_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
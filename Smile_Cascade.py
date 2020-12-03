import cv2

image = cv2.imread("Test.jpg")
cv2.resize(image,(800,800))
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
smiles = smile_cascade.detectMultiScale(image, scaleFactor=2, minNeighbors=10)

for (sx, sy, sw, sh) in smiles:
    cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 5)

cv2.imshow("Smile Detected", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
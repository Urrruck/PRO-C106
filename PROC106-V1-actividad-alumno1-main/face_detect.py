import cv2

img = cv2.imread("4f.jpg")

#tonalidades de grises
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#detectMultiScale(imagen en escala de grises,factor de escala,parametro que cuenta rasgos faciales)
faces = face_cascade.detectMultiScale(gray,1.1,5)
print(len(faces))

for (x,y,w,h) in faces:
       #(255,0,0) colores azul/verde/rojo
       cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
       #face=img[y:y+h, x:x+w]
       #cv2.imwrite("face.jpg",face)
cv2.imshow('Imagen',img)
cv2.waitKey(0)




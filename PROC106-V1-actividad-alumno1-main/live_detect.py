# Importar la biblioteca OpenCV
from cgitb import grey
import cv2

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while(True):
    
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in faces:
       #(255,0,0) colores azul/verde/rojo
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    # Mostrar el cuadro resultante 
    cv2.imshow("Camara web", frame) # OpenCV no acepta caracteres especiales como el acento en "Cámara"
      
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()
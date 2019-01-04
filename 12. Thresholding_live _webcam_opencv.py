import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 400)
cap.set(4, 300)

if cap.isOpened():
    ret, frame = cap.read()
else:
    False
    
while ret:
    ret, frame = cap.read()
    
    th = 127
    maxval = 255
    
    ret, o1 = cv2.threshold(frame, th, maxval, cv2.THRESH_BINARY)
    ret, o2 = cv2.threshold(frame, th, maxval, cv2.THRESH_BINARY_INV)
    ret, o3 = cv2.threshold(frame, th, maxval, cv2.THRESH_TOZERO)
    ret, o4 = cv2.threshold(frame, th, maxval, cv2.THRESH_TOZERO_INV)
    ret, o5 = cv2.threshold(frame, th, maxval, cv2.THRESH_TRUNC)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                                
    
    cv2.imshow('Original', frame)
    cv2.imshow('Binary', o1)
    cv2.imshow('Binary Inv', o2)
    cv2.imshow('Zero', o3)
    cv2.imshow('Zero Inv', o4)
    cv2.imshow('Trunc', o5)
    
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

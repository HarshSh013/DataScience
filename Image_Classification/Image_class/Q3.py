import numpy as np
import cv2

img = np.zeros((400, 400, 3), dtype = "uint8")

# initial x & y
x,y=200,200
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'O'
cv2.putText(img, text, (x, y), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('Move Text', img)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # Press Esc to exit
        break
    elif key == ord('a'):
        x -= 10  # Move text left
    elif key == ord('d'):
        x += 10  # Move text right
    elif key == ord('w'):
        y -= 10  # Move text up
    elif key == ord('s'):
        y += 10  # Move text down

    # Clear the image
    img = np.zeros((400, 400, 3), dtype="uint8")

    # Draw the text at the new position
    cv2.putText(img, text, (x, y), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Move Text', img)

cv2.destroyAllWindows()
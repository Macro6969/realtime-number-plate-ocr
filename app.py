import cv2
import easyocr
import numpy as np
number_plate= cv2.CascadeClassifier("indian_license_plate.xml")
cap= cv2.VideoCapture(0)
reader = easyocr.Reader(['en'], gpu=False)
while True:
    ret, frame= cap.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate= number_plate.detectMultiScale(gray, 1.7, 8)
    for (x,y,w,h) in plate:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, "Number Plate", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        roi_gray= gray[y:y+h, x:x+w]
        roi_color= frame[y:y+h, x:x+w]
        ocr_result = reader.readtext(roi_gray)
        # If EasyOCR successfully found text inside the box
        if ocr_result:
            # EasyOCR returns a list of tuples: (bounding_box, text, confidence)
            # We take the text element [-2] from the first result found
            plate_text = ocr_result[0][-2]
            confidence = ocr_result[0][-1]
            
            # Clean up the string (capitalize and remove extra spaces)
            clean_text = plate_text.upper().strip()
            
            # Only display if it's a reasonably confident reading
            if confidence > 0.30:
                print(f"Detected Plate: {clean_text} (Match Accuracy: {confidence:.2f})")
                
                # Draw the text right above the green bounding box
                cv2.putText(frame, clean_text, (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Number Plate Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
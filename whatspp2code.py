import cv2
from twilio.rest import Client


classifier = cv2.CascadeClassifier("path/to/classifier.xml")
classifier.load("path/to/classifier.xml")




# Load the cascade classifiers for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# if image.shape[0] == 0 or image.shape[1] == 0:
#     print("Error: image is empty")


if classifier.empty():
    print("Error: classifier object is empty")

# Twilio account information
account_sid = 'AC980914cc39a77b4b83da6495784053e6'
auth_token = '956292a7b791087410a3f01df37e2557'
client = Client(account_sid, auth_token)

# Twilio Sandbox for WhatsApp number
whatsapp_number = 'whatsapp:+14155238886'

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Loop until the user quits
while True:
    # Read a frame from the video capture
    _, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # send message to the person
        message = client.messages.create(
            from_=whatsapp_number,
            body='Face Recognized, sending message',
            to='whatsapp:+1234567890' # replace with the target number
        )
    # Show the frame
    cv2.imshow("Face Detection", frame)
    
    # Exit if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()
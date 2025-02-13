import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
finger_Coord = [(8, 6), (12, 10), (16, 14), (20, 18)]
thumb_Coord = (4, 2)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Не удалось получить изображение с web-камеры")
        continue

    cv2.imshow('image', image)
    if cv2.waitKey(1) &  0xFF == 27:  # esc
        break

    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(RGB_image)
    if not result.multi_hand_landmarks:
        continue
    multiLandMarks = result.multi_hand_landmarks
    print("Руки", multiLandMarks)
    
   

cap.release()
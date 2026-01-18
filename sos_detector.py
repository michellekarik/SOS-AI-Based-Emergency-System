import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

FINGER_TIPS = [8, 12, 16, 20]
FINGER_PIPS = [6, 10, 14, 18]
THUMB_TIP = 4
THUMB_IP = 3

def four_fingers_thumb_folded(hand):
    fingers_up = 0
    for tip, pip in zip(FINGER_TIPS, FINGER_PIPS):
        if hand.landmark[tip].y < hand.landmark[pip].y:
            fingers_up += 1

    thumb_folded = hand.landmark[THUMB_TIP].x > hand.landmark[THUMB_IP].x
    return fingers_up == 4 and thumb_folded

def fist(hand):
    for tip, pip in zip(FINGER_TIPS, FINGER_PIPS):
        if hand.landmark[tip].y < hand.landmark[pip].y:
            return False
    return True

def detect_sos():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    ) as hands:

        stage = "WAIT_OPEN"

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            if result.multi_hand_landmarks:
                hand = result.multi_hand_landmarks[0]

                mp_draw.draw_landmarks(
                    frame,
                    hand,
                    mp_hands.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2),
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2)
                )

                if stage == "WAIT_OPEN" and four_fingers_thumb_folded(hand):
                    stage = "WAIT_FIST"

                elif stage == "WAIT_FIST" and fist(hand):
                    cap.release()
                    cv2.destroyAllWindows()
                    return True

            cv2.putText(frame, f"Stage: {stage}", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow("SOS Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
    return False

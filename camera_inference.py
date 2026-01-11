from ultralytics import YOLO
import cv2
import time
from collections import defaultdict

# ===============================
# Load trained model
# ===============================
MODEL_PATH = "runs/detect/yolov8_custom_50ep/weights/best.pt"
model = YOLO(MODEL_PATH)

# ===============================
# Open webcam
# ===============================
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ===============================
# Class colors (BGR)
# ===============================
CLASS_COLORS = {
    0: (255, 0, 0),     # car - Blue
    1: (0, 255, 0),     # cats - Green
    2: (0, 0, 255),     # dog - Red
    3: (255, 255, 0)    # person - Cyan
}

# ===============================
# FPS calculation
# ===============================
prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Start timer
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    # ===============================
    # Run inference (CPU optimized)
    # ===============================
    results = model(
        frame,
        imgsz=480,     # smaller size for CPU
        conf=0.35,     # confidence threshold
        device="cpu",
        verbose=False
    )

    detections = results[0].boxes
    names = results[0].names

    # ===============================
    # Object counter
    # ===============================
    class_counts = defaultdict(int)

    if detections is not None:
        for box in detections:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            class_counts[names[cls_id]] += 1

            color = CLASS_COLORS.get(cls_id, (255, 255, 255))

            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Label
            label = f"{names[cls_id]} {conf:.2f}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    # ===============================
    # Display FPS
    # ===============================
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ===============================
    # Display object counts
    # ===============================
    y_offset = 60
    for cls, count in class_counts.items():
        text = f"{cls}: {count}"
        cv2.putText(
            frame,
            text,
            (10, y_offset),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )
        y_offset += 30

    # ===============================
    # Show window
    # ===============================
    cv2.imshow("YOLOv8 Custom Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ===============================
# Cleanup
# ===============================
cap.release()
cv2.destroyAllWindows()

yolo detect train \
    data=/home/harsh/Desktop/CV_Task1/custom_object_detection/cat-dog-person.v1i.yolov8/data.yaml \
    model=yolov8n.pt \
    epochs=50 \
    batch=2 \
    imgsz=640 \
    device=cpu \
    name=yolov8_custom_50ep \
    augment=True

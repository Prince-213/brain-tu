import cv2
import supervision as sv
from ultralytics import YOLO

model = YOLO("./best.pt")
image = cv2.imread('./images/images (2).jpeg')
results = model(image)[0]
detections = sv.Detections.from_ultralytics(results)

mask_annotator = sv.MaskAnnotator()
label_annotator = sv.LabelAnnotator(text_position=sv.Position.TOP_LEFT)

corner_annotator = sv.BoxCornerAnnotator()

annotated_image = mask_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections)

# Save the annotated image
output_path = './annotated_dog.jpeg'
cv2.imwrite(output_path, annotated_image)

print(f"Annotated image saved at {output_path}")

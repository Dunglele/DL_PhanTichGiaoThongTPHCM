import os
import cv2

image_dir = "dataset/images"
label_dir = "dataset/labels"

classes = [
    "motorcycle",
    "car",
    "truck",
    "bus"
]

for img_name in os.listdir(image_dir):
    
    img_path = os.path.join(image_dir, img_name)
    label_path = os.path.join(label_dir, img_name.replace(".jpg", ".txt"))

    img = cv2.imread(img_path)
    h, w, _ = img.shape

    if os.path.exists(label_path):

        with open(label_path) as f:
            for line in f.readlines():

                cls, x, y, bw, bh = map(float, line.split())

                x1 = int((x - bw/2) * w)
                y1 = int((y - bh/2) * h)
                x2 = int((x + bw/2) * w)
                y2 = int((y + bh/2) * h)

                label = classes[int(cls)]

                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(img,label,(x1,y1-5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,(0,255,0),1)

    cv2.imshow("dataset", img)

    if cv2.waitKey(0) == 27:   # ESC để thoát
        break

cv2.destroyAllWindows()
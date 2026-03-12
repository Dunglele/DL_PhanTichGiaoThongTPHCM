import os
import cv2

image_dir = "dataset/images"
label_dir = "dataset/labels"

deleted = 0

for img_name in os.listdir(image_dir):

    img_path = os.path.join(image_dir, img_name)

    img = cv2.imread(img_path)

    # nếu ảnh lỗi hoặc không đọc được
    if img is None or img.shape[0] < 10 or img.shape[1] < 10:

        print("Delete:", img_name)

        os.remove(img_path)

        # xóa luôn label tương ứng
        label_name = os.path.splitext(img_name)[0] + ".txt"
        label_path = os.path.join(label_dir, label_name)

        if os.path.exists(label_path):
            os.remove(label_path)

        deleted += 1

print("Deleted images:", deleted)
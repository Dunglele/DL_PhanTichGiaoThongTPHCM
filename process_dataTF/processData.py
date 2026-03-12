import os
import shutil
import cv2
from ultralytics import YOLO
from sklearn.model_selection import train_test_split

# ==============================
# CONFIG
# ==============================

SOURCE_FOLDER = "../traffic_data"
DATASET_FOLDER = "dataset"

IMAGE_FOLDER = os.path.join(DATASET_FOLDER, "images")
LABEL_FOLDER = os.path.join(DATASET_FOLDER, "labels")

os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(LABEL_FOLDER, exist_ok=True)

# ==============================
# LOAD MODEL
# ==============================

model = YOLO("yolo11n.pt")

# ==============================
# GOM ẢNH + RENAME
# ==============================

all_images = []
counter = 0

for root, dirs, files in os.walk(SOURCE_FOLDER):
    for file in files:

        if file.lower().endswith((".jpg",".png",".jpeg")):

            src = os.path.join(root, file)

            new_name = f"img_{counter}.jpg"
            dst = os.path.join(IMAGE_FOLDER, new_name)

            shutil.copy(src, dst)

            all_images.append(dst)
            counter += 1

print("Tổng ảnh:", len(all_images))

# ==============================
# AUTO LABEL
# ==============================

model.predict(
    source=IMAGE_FOLDER,
    save_txt=True,
    save_conf=True,
    conf=0.3
)

print("YOLO auto label xong")

# ==============================
# TÌM PREDICT FOLDER MỚI NHẤT
# ==============================

runs_path = "../runs/detect"

predict_folders = [
    os.path.join(runs_path, d)
    for d in os.listdir(runs_path)
    if "predict" in d
]

predict_folders.sort(key=os.path.getmtime)

latest_predict = predict_folders[-1]

PREDICT_LABEL = os.path.join(latest_predict, "labels")

print("Label folder:", PREDICT_LABEL)

# ==============================
# REMAP + FILTER LABEL
# ==============================

for file in os.listdir(PREDICT_LABEL):

    src = os.path.join(PREDICT_LABEL, file)
    dst = os.path.join(LABEL_FOLDER, file)

    img_name = file.replace(".txt",".jpg")
    img_path = os.path.join(IMAGE_FOLDER,img_name)

    img = cv2.imread(img_path)

    if img is None:
        continue

    h,w = img.shape[:2]

    lines_new = []

    with open(src) as f:
        lines = f.readlines()

    for line in lines:

        parts = line.split()

        if len(parts) < 6:
            continue

        cls,x,y,bw,bh,conf = map(float,parts)

        cls = int(cls)

        # ===== lọc confidence =====
        if conf < 0.35:
            continue

        # ===== lọc box quá nhỏ =====
        if bw * bh < 0.0005:
            continue

        # ===== lọc box quá to =====
        if bw * bh > 0.5:
            continue

        # ===== lọc box sát biên =====
        if x < 0.02 or x > 0.98:
            continue

        # ===== remap class =====
        if cls == 1:      # bicycle
            cls = 0

        elif cls == 3:    # motorcycle
            cls = 0

        elif cls == 2:
            cls = 1

        elif cls == 5:
            cls = 2

        elif cls == 7:
            cls = 3

        else:
            continue

        lines_new.append(f"{cls} {x} {y} {bw} {bh}\n")

    with open(dst,"w") as f:
        f.writelines(lines_new)

print("Remap + filter xong")

# ==============================
# CHIA TRAIN / VAL
# ==============================

train,val = train_test_split(all_images,test_size=0.2)

os.makedirs("dataset/train/images",exist_ok=True)
os.makedirs("dataset/train/labels",exist_ok=True)
os.makedirs("dataset/val/images",exist_ok=True)
os.makedirs("dataset/val/labels",exist_ok=True)

def move_files(files,img_dst,label_dst):

    for img in files:

        name = os.path.basename(img)
        label = name.replace(".jpg",".txt")

        shutil.copy(img,os.path.join(img_dst,name))

        label_path = os.path.join(LABEL_FOLDER,label)

        if os.path.exists(label_path):
            shutil.copy(label_path,os.path.join(label_dst,label))


move_files(train,"dataset/train/images","dataset/train/labels")
move_files(val,"dataset/val/images","dataset/val/labels")

print("Dataset ready!")
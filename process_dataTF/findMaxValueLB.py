import os

DATASET = "..\\process_dataTF\\dataset\\labels"

classes = set()

for root, dirs, files in os.walk(DATASET):
    for file in files:
        if file.endswith(".txt"):

            path = os.path.join(root,file)

            with open(path) as f:
                for line in f:
                    if line.strip()=="":
                        continue

                    cls = int(line.split()[0])
                    classes.add(cls)

print("Classes tìm thấy:",classes)
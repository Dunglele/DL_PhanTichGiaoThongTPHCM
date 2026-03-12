import csv

list_camera = [
    {"ID": "5b19d34faf4ff60011d6ea52", "Name": "Nguyen Tat Thanh - Ton Dan"},
    {"ID": "63ae777cbfd3d90017e8f177", "Name": "Nguyen Tat Thanh - Doan Nhu Hai"},
    {"ID": "5deb576d1dc17d7c5515ad0f", "Name": "Nguyen Thi Minh Khai - Truong Dinh"},
    {"ID": "58af994abd82540010390c37", "Name": "Nguyen Huu Canh - Ton Duc Thang"},
    {"ID": "5deb576d1dc17d7c5515ad01", "Name": "Vo Thi Sau - Hai Ba Trung"},
    {"ID": "6623e7b76f998a001b25242d", "Name": "Dinh Bo Linh - Bui Dinh Tuy"},
    {"ID": "5a6060e08576340017d0660f", "Name": "Nguyen Thai Son - Phan Van Tri 2"},
    {"ID": "595d9b3b3dcfc400106f287e", "Name": "Quoc Lo 1 - An Phu Dong 12"},
    {"ID": "63b66051bfd3d90017eaa4a3", "Name": "No Trang Long - Phan Van Tri"},
    {"ID": "5a8253bc5058170011f6eac1", "Name": "Dinh Bo Linh - Bach Dang 2"},
    {"ID": "66b1c426779f74001867415e", "Name": "Dien Bien Phu - Nguyen Gia Tri"},
]

with open('data_traffic.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Name']) #Header row
    for i in list_camera:
        writer.writerow([i["ID"], i["Name"]])

print("CSV file 'data_traffic.csv' has been created successfully.")

print("===================================\n")

print("Tien hanh doc du lieu tu file CSV:\n")

with open('data_traffic.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        print(f"ID: {row[0]}, Name: {row[1]}")
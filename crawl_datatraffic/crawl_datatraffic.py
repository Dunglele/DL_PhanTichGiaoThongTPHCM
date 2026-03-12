import requests
from datetime import datetime
import csv
import os
from time import sleep

def introduction():
    print("\n===================================\n")
    print("CHƯƠNG TRÌNH CÀO DỮ LIỆU GIAO THÔNG TP.HCM\n")
    print("=====================================\n")
    print("Cách dùng: \n")
    print("1. Chọn '3' để tạo thư mục lưu trữ dữ liệu giao thông ngày hôm nay.\n")
    print("2. Chọn '1' để bắt đầu cào dữ liệu giao thông.\n")
    print("3. Chọn '2' để thêm dữ liệu camera vào file CSV nếu cần.\n")
    print("=====================================\n")
    print("=====================================\n")
    print("\n1. Cào dữ liệu giao thông ngày hôm nay")
    print("\n2. Thêm dữ liệu camera vào file CSV")
    print("\n3. Tạo thư mục lưu trữ ảnh giao thông ngày hôm nay")
    print("\n4. Thống kê số lượng ảnh của các khu vực giao thông")
    print("\n0. Thoát")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept": "image/avif,image/webp,*/*",
    "Referer": "https://giaothong.hochiminhcity.gov.vn/",
    "Origin": "https://giaothong.hochiminhcity.gov.vn",
}

cookies = {
    "ASP.NET_SessionId": "t2oslxxsqllan4lgzhah3cgt",
    ".VDMS": "C50F85C6C71667BE6ED050D74003980406811A8F6C3BE32B157BABF3CD92E74B0BA3E01A4B490B8BA16EAF15828702B1FB68957AD67317B9D42579BB90FCC150AF18CA519E195678537CA47740D9831A7E454628FC6A4097185A66629BB114F7EE9611E85CE9747C30D5968598EFBF67382F9DD1",
    "_frontend": "!9YOHO1qc4zwwKz24P1VY/lC/bQptjssYZ3m9UbDnTWnCQqqoOil+geXpFacMNljkY7bQh63nOwwyIko=",
    "CurrentLanguage": "vi",
    "_pk_ses.1.2f14": "*",
    "_ga": "GA1.3.709058770.1768372334",
    "_gid": "GA1.3.969540300.1768372334",
    "_pk_id.1.2f14": "2b57dfcf6efc5ad8.1768372334.1.1768372958.1768372334.",
    "_ga_JCXT8BPG4E": "GS2.3.s1768372334$o1$g1$t1768372958$j60$l0$h0",
    "TS01e7700a": "0150c7cfd19d45b130811deec284bb08de597c3105a4f85a3faba4aaa6a660813d2a5b1aa258c8cabc797769e8c8736c1810df1ef7d4b39bdef16eddcffa7b3039a815892aa662f7ad032d8f97064986070cde4999c518edb881cbc1f7826a21f1ea185ceb"
}

def crawl_datatraffic(headers, cookies): 
    count = 1
    print("\n===================================\n")
    print(f"Đang tiến hành cào dữ liệu giao thông vào thời gian {datetime.now()}\n")
    print("===================================\n")

    try:
        while True:
            with open('data_traffic.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                for i in reader:
                    id_camera = i[0]
                    url = f"https://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id={id_camera}&bg=black&w=640&h=480"

                    resp = requests.get(url, headers=headers, cookies=cookies)
                    now = datetime.now()
                    if resp.status_code == 200:
                        with open(f"traffic_data/{now.date()}/{i[1]}_{now.hour}H{now.minute}.jpg", "wb") as f:
                            f.write(resp.content)
                        print(f"{count}. Tải OK → {i[1]}_{now.hour}:{now.minute}.jpg")
                        count += 1
                    else:
                        print(f"{count}. Lỗi:", resp.status_code)
            print("\nĐang chờ 60 giây để tiếp tục cào dữ liệu...\n")
            print("Nhấn Ctrl+C để dừng cào dữ liệu.\n")
            sleep(60)
    except KeyboardInterrupt:
        print("\n\nĐã dừng cào dữ liệu giao thông theo yêu cầu người dùng.")

    print("\n===================================\n")
    print("Hoàn tất cào dữ liệu giao thông. Thu thập được", count, "ảnh.")

    quit = input("Bạn có muốn tiếp tục cào dữ liệu không? (y/n): ")

    if quit == "y":
        return switch_case(headers, cookies)
    return switch_case(headers, cookies)

def append_data_traffic_csv():

    new_id = input("\nNhập ID Camera: ")
    with open('data_traffic.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if new_id == row[0]:
                print(f"\nID Camera: {new_id} đã tồn tại trong file 'data_traffic.csv'. Vui lòng kiểm tra lại.\n")
                quit = input("Bạn có muốn thử lại không? (y/n): ")
                if quit == "y":
                    return append_data_traffic_csv()
                return switch_case(headers, cookies)
    new_name = input("Nhập Tên Camera: ")

    with open('data_traffic.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Add new camera data here if needed
        # Example:
        writer.writerow([new_id, new_name])

    print(f"\nĐã thêm Camera với ID: {new_id}, Tên: {new_name} vào file 'data_traffic.csv' thành công.\n")
    input("Nhấn Enter để tiếp tục...")
    return switch_case(headers, cookies)

def CreateFolderSaveTF():
    now = datetime.now()
    if not os.path.exists(f"traffic_data/{now.date()}"):
        os.mkdir(f"traffic_data/{now.date()}")
        print(f"\nĐã tạo thư mục 'traffic_data/{now.date()}' thành công.\n")
    else:
        print(f"\nThư mục 'traffic_data/{now.date()}' đã tồn tại.\n")
    input("Nhấn Enter để tiếp tục...")
    return switch_case(headers, cookies)

def CountImgData():
    folder = r"traffic_data"
    count = 0
    img_ext = (".jpg")

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(img_ext):
                count += 1
    
    print("\nTổng số ảnh: ", count)
    input("Nhấn Enter để tiếp tục...")
    return switch_case(headers, cookies)

def switch_case(headers, cookies):
    introduction()
    choice = int(input("\nNhập lựa chọn: "))
    if choice == 0:
        print("\nThoát chương trình. Tạm biệt!\n")
        return
    else:
        match choice:
            case 1:
                crawl_datatraffic(headers, cookies)
            case 2:
                append_data_traffic_csv()
            case 3:
                CreateFolderSaveTF()
            case 4:
                CountImgData()

def main():
    switch_case(headers, cookies)

if __name__ == "__main__":
    main()
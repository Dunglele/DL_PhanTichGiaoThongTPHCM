# DL_PhanTichGiaoThongTPHCM
Dự án huấn luyện mô hình học sâu, phục vụ phân tích, dự báo trạng thái giao thông trên một vài khu vực địa bàn TPHCM
<img width="1335" height="778" alt="image" src="https://github.com/user-attachments/assets/4d83c711-ddb2-4d97-99dd-d746ecf2ba34" />
<h2>Hướng dẫn gán nhãn dữ liệu</h2>
<br />
<h3>Bước 1: Clone thư mục dự án, chạy môi trường ảo "cd env/Scripts", sau đó chạy lệnh activate "./activate"</h3>
<img width="1320" height="133" alt="image" src="https://github.com/user-attachments/assets/d2f8af54-cd38-4232-ae07-77b4da339f2a" />
<br />
<hr />
<h3>Bước 2: Chạy lệnh "labelImg" trên cửa sổ dòng lệnh, để mở tool gán nhãn</h3>
<img width="2578" height="1709" alt="image" src="https://github.com/user-attachments/assets/8a905c9f-8e26-4d08-8bd6-bf94a8702d36" />
<br />
<hr />
<h3>Bước 3: Trong menu, chọn view > auto save mode. Vào tệp .\process_dataTF\dataset\labels\classes.txt để xem các lớp cần gán nhãn</h3>
<img width="2318" height="1391" alt="image" src="https://github.com/user-attachments/assets/005e68cc-09fa-43a0-a0ac-42802caac900" />
<br />
<hr />
<h3>Bước 4: Nếu menu hiển thị Pascal, hãy click vào nó để nó chuyển sang YOLO format</h3>
<img width="2314" height="1383" alt="image" src="https://github.com/user-attachments/assets/0959e9da-00b5-4084-a640-3284facfb389" />
<br />
<hr />
<h3>Bước 5: Nhấn vào File dir, chọn thư mục .\process_dataTF\dataset\images. Nhấn vào Change File Save, chọn thư mục .\process_dataTF\dataset\labels</h3>
<img width="2411" height="1666" alt="image" src="https://github.com/user-attachments/assets/c3692bc8-3064-41cd-baac-4c9c14929203" />
<hr />
<img width="2329" height="1664" alt="image" src="https://github.com/user-attachments/assets/e9096760-df05-4d68-aa71-27a820833366" />
<br />
<hr />
<h3>Bước 6: Nhấn W để tiến hành vẽ box gán nhãn, D để tới ảnh tiếp theo, A để quay lại ảnh trước.</h3>
<img width="2315" height="1384" alt="image" src="https://github.com/user-attachments/assets/378ae95c-6d58-497f-97e5-82b4a75428fd" />
<hr />
<h1>Nhớ Push Commit sau khi gán nhãn xong</h1> 

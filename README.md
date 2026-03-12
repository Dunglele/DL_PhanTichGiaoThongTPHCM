# Crawl_DataTFHCM
Chương trình cào dữ liệu giao thông, phục vụ huấn luyện học sâu tại thành phố Hồ Chí Minh
<img width="1335" height="778" alt="image" src="https://github.com/user-attachments/assets/4d83c711-ddb2-4d97-99dd-d746ecf2ba34" />
<h2>Hướng dẫn gán nhãn dữ liệu</h2>
<br />
Bước 1: Clone thư mục dự án, chạy môi trường ảo "cd env/Scripts./activate"
<br />
Bước 2: Chạy lệnh "labelImg" trên cửa sổ dòng lệnh, để mở tool gán nhãn
<br />
Bước 3: Trong menu, chọn view > auto save mode. Vào tệp .\process_dataTF\dataset\labels\classes.txt để xem các lớp cần gán nhãn
<br />
Bước 4: Nếu menu hiển thị Pascal, hãy click vào nó để nó chuyển sang YOLO format
<br />
Bước 5: Nhấn vào File dir, chọn thư mục .\process_dataTF\dataset\images. Nhấn vào Change File Save, chọn thư mục .\process_dataTF\dataset\labels
<br />
Bước 6: Nhấn W để tiến hành vẽ box gán nhãn, D để tới ảnh tiếp theo, A để quay lại ảnh trước.

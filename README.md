# Age-Gender-Prediction
Predict age and gender of people using mobile net v2 and UTKFace datasets with 91% accuracy age, 80% accuracy ethnicity, 47.45 MSE age.

![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/UTKFaceDemo.png)
___
## 1. Mục đích và dataset
  - Giới tính và độ tuổi của người dùng rất quan trọng đối với các tổ chức để hiểu khách hàng và phát triển các chiến lược của họ để cung cấp các dịch vụ tốt hơn cho khách hàng.
  - Trong project trên sẽ đề cập tới vấn đề sử dụng mô hình mobile net v2 để dự đoán tuổi, giới tính và dân tộc của khách hàng khi đi vào vùng camera.
  - Trong bài sử dụng tập dữ liệu UTKFace bao gồm hơn 20000 hình ảnh khuôn mặt bao gồm các chú thích về tuổi (0 - 116), giới tính (2) và dân tộc (5). Các hình ảnh bao gồm sự thay đổi lớn trong tư thế, biểu hiện khuôn mặt, độ phân giải, ...
  - Liên kết tải tập dữ liệu gốc: [link](https://www.kaggle.com/datasets/jangedoo/utkface-new)
## 2. Phân tích và kĩ thuật bài toán
  - Dữ liệu sau khi tải về sẽ được đưa về dạng file csv với các tính năng chính là: age (tuổi), gender (giới tính), ethnicity (dân tộc), image (hình ảnh). Hình ảnh khuôn mặt sẽ được đưa về kích thước 50x50 phù hợp với cấu hình máy.
  - Tập dữ liệu sau khi chuyển về file csv: [link](https://www.kaggle.com/datasets/lngcthun/utkface-convert-csv)
  #### Phân tích bài toán
  - Mô hình bài toán được thể hiện như sau:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/project.png)
  - Mô hình được áp dụng là mobile net v2 do tính nhỏ gọn nhưng vẫn đem lại hiệu quả tốt, thích hợp triển khai trên biên, ngoài ra lớp FC sẽ sử dụng thêm regularizers l2.
## 3.Kiểm thử mô hình
Sau khi rèn luyện mô hình ta thu được kết quả của mô hình dự đoán tuổi và giới tính:
- Model Predict age:
  + MSE predict age:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/MSE_loss_age.png)
- Model predict gender:
  + Accuracy predict gender:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/Accuracy_gender.png)
  + Loss predict gender:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/Loss_gender.png)
- Model predict ethnicity:
  + Accuracy predict ethnicity:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/Accuracy_ethnicity.png)
  + Loss predict ethnicity:
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/Loss_ethnicity.png)
- Test model:
Image: General Secretary Nguyen Phu Trong visit becomes Chinese
  + Before
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/test.jpg)
  + After
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/test/test.jpg)
  + Before
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/test1.jpg)
  + After
  <br>![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/image/test/test1.jpg)

# Age-Gender-Prediction
Predict age and gender of people using CNN and UTKFace datasets


![image](https://production-media.paperswithcode.com/datasets/UTKFace-0000000710-4976bb64_rQrd7aQ.jpg)



_________________________________________________________________________________________________________________
I.Datasets
- Bài viết sử dụng bộ datasets UTKFace.
- Tải data tại đây: https://www.kaggle.com/datasets/jangedoo/utkface-new

II.Training
Quá trình train bao gồm 3 giai đoạn:
- Xử lí dữ liệu
- Rèn luyện mô hình
- Kiểm thử mô hình

1.Xử lí dữ liệu
- Do vấn đề về memory nên trong bài viết chỉ trích xuất 1 phần dữ liệu của data UTKFace để xử lí.
- Dữ liệu sau xử lí bao gồm: 1 mảng numpy 3 chiều, 2 mảng numpy về lable của tuổi và giới tính.
- Như đã nói, do vấn đề về giới hạn memory, bài viết chỉ trích xuất các phần của data UTKFace vào để xử lí. Vì vậy label của tuổi chỉ chia ra làm 8 loại là độ tuổi trong các khoảng 8-80 (Bỏ đi các phần còn lại) bao gồm: "8-12", "13-18", "19-25", "26-32", "33-44", "45-55", "56-70", "71-80". Giới tính có 2 loại là "Male" và "Female". Sau đó dùng phương pháp encoder là LabelBinarizer được sử dụng để chuyển đổi lại label.

2.Rèn luyện mô hình
- Bài viết sử dụng mạng CNN để rèn luyện mô hình.
- Mô hình sử dụng 2 lớp tích chập liên tiếp khiến lớp đó sâu hơn, giúp nó có thể trích xuất được nhiều đặc trưng hơn, sau đó kết hợp với các lớp Pooling. Mô hình sử dụng hàm ReLU giúp tăng tốc độ hội tụ và tính toán. Trong mô hình cũng sử dụng thêm lớp BatchNormalization giúp cho dữ liệu được đồng bộ về phân phối sau khi qua các hàm ReLU, giúp cho trọng số được phân bố đồng đều hơn, nó giới hạn độ lớn của gradients chặt chẽ hơn giúp việc tối ưu hàm mục tiêu sẽ trở nên dễ dàng nhanh chóng hơn từ đó thì mô hình có thể học nhanh hơn. Ngoài ra mô hình cũng sử dụng thêm regularizers tránh việc mô hình bị overfit.
- Mô hình dùng optimizer là Adam, loss là categorical_crossentropy và metrics là accuracy.

3.Kiểm thử mô hình
Sau khi rèn luyện mô hình ta thu được kết quả của mô hình dự đoán tuổi và giới tính:
- Mô hình dự đoán tuổi:
  + Accuracy và loss của mô hình dự đoán tuổi:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/acc_loss_age.png)
  + Các epochs cuối của mô hình dự đoán tuổi:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/predict_age.png)
- Mô hình dự đoán giới tính:
  + Accuracy và loss của mô hình dự đoán giới tính:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/acc_loss_gender.png)
  + Các epochs cuối của mô hình dự đoán giới tính:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/predict_gender.png)

III. Tài liệu tham khảo
- <1>: https://viblo.asia/p/normalization-and-normalization-techniques-in-deep-learning-QpmleJyn5rd
- <2>: https://keras.io/api/layers/regularizers/
- <3>: https://www.kaggle.com/datasets/jangedoo/utkface-new
- <4>: https://paperswithcode.com/dataset/utkface
  


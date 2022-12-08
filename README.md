# Age-Gender-Prediction
Predict age and gender of people using CNN and UTKFace datasets


![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/UTKFaceDemo.png)



_________________________________________________________________________________________________________________
I.Datasets
- Bài viết sử dụng bộ datasets UTKFace.
- Tải data tại đây: https://www.kaggle.com/datasets/jangedoo/utkface-new

II.Training
Quá trình train bao gồm 3 giai đoạn:
- Xử lí dữ liệu.
- Rèn luyện mô hình.
- Kiểm thử mô hình.
- Quá trình thực hiện sẽ được làm trên Google colab với GPU.

1.Xử lí dữ liệu
- Dữ liệu sau xử lí bao gồm: 1 mảng numpy 3 chiều, 2 mảng numpy về lable của tuổi và giới tính.
- Bài viết trích xuất các thành phần của datasets UTKFace và chia nó ra thành các khoảng độ tuổi để xử lí. Vì vậy label của tuổi chỉ chia ra làm 18 loại là độ tuổi trong các khoảng 1-116 bao gồm: "1-4", "5-8", "9-12", "13-16", "19-22", "23-26", "27-30", "31-34", "35-38", "39-42", "43-46", "47-50", "51-56", "57-62", "63-70", "71-80", "81-90", "91-116". Giới tính có 2 loại là "Male" và "Female". Sau đó dùng phương pháp encoder là LabelBinarizer được sử dụng để chuyển đổi lại label.

2.Rèn luyện mô hình
- Bài viết sử dụng mạng CNN để rèn luyện mô hình.
- Mô hình sử dụng 2 lớp tích chập liên tiếp khiến lớp đó sâu hơn, giúp nó có thể trích xuất được nhiều đặc trưng hơn, sau đó kết hợp với các lớp Pooling. Mô hình sử dụng hàm ReLU giúp tăng tốc độ hội tụ và tính toán. 
- Trong mô hình cũng sử dụng thêm lớp BatchNormalization giúp cho dữ liệu được đồng bộ về phân phối sau khi qua các hàm ReLU, giúp cho trọng số được phân bố đồng đều hơn, nó giới hạn độ lớn của gradients chặt chẽ hơn giúp việc tối ưu hàm mục tiêu sẽ trở nên dễ dàng nhanh chóng hơn từ đó thì mô hình có thể học nhanh hơn. Ngoài ra mô hình cũng sử dụng thêm regularizers tránh việc mô hình bị overfit.
- Mô hình dùng optimizer là Adam, loss là categorical_crossentropy và metrics là accuracy.
- Mô hình sử dụng ImageDataGenerator để tăng cường dữ liệu.

3.Kiểm thử mô hình
Sau khi rèn luyện mô hình ta thu được kết quả của mô hình dự đoán tuổi và giới tính:
- Mô hình dự đoán tuổi:
  + Accuracy và loss của mô hình dự đoán tuổi:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/age_loss_acc.png)
- Mô hình dự đoán giới tính:
  + Accuracy và loss của mô hình dự đoán giới tính:
  + ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/loss_accuracy/gender_loss_acc.png)
- Kiểm thử mô hình:
  ![image](https://github.com/chienthan2vn/Age-Gender-Prediction/blob/main/test.jpg)

III. Tài liệu tham khảo
- <1>: https://viblo.asia/p/normalization-and-normalization-techniques-in-deep-learning-QpmleJyn5rd
- <2>: https://keras.io/api/layers/regularizers/
- <3>: https://www.kaggle.com/datasets/jangedoo/utkface-new
- <4>: https://viblo.asia/p/tang-cuong-du-lieu-trong-deep-learning-oOVlYe4nl8W
- <5>: https://www.researchgate.net/figure/Comparative-analysis-of-FaceNet-VGGFace-VGG16-and-VGG19-for-face-recognition-on_fig1_353828254
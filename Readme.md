# **Website thử nghiệm phân loại COVID-19 FAKE NEWS**
## **Bộ dữ liệu**
Bộ dự liệu lấy từ cuộc thi CONSTRAINT-2021 do Codalab tổ chức.

![image](https://user-images.githubusercontent.com/29734492/109349580-338c5c00-789c-11eb-8400-a836364974af.png)

**English Dataset**: https://competitions.codalab.org/competitions/26655 or https://github.com/diptamath/covid_fake_news/tree/main/data

**Link cuộc thi**: https://constraint-shared-task-2021.github.io/

## **Về thiết kế model**

Chúng tôi tiến hành thực nghiệm các mô hình máy học đơn giản sau đây:
- **Decision Tree**
- **KNeighbors Classification**
- **Logistic Classification**
- **NaiveBayes**
- **Random Forest**
- **Support Vector Classification (rbf, sigmoid, linear)**

## **Về dữ liệu đầu vào**
Chúng tôi tiến hành tiến hành xử lý dữ liệu loại bỏ những đường link và kí tự đặc biệt. Sau đó loại bỏ Stopwords và vector hóa các từ.

## **Kết quả thử nghiệm model**
Dưới đây là hình ảnh chạy thử nghiệm của các model trên

![image](imgs/model.png)

Model SVC(rbf) cho kết quả tốt nhất với Accuracy: 0.9371 và F1-score: 0.9413.
Chúng tôi quyết định chọn model SVC(rbf) và tiếp tục tiến hành tinh chỉnh tham số. 

Kết quả đạt sau khi tinh chỉnh tham số với C=3, max_iter=1000 đã tăng lên  với Accuracy: 0.9411 và F1-score: 0.9442.

## **Xây dựng Website**
Chúng tôi sử dung Flask để xây dựng một Website đơn giản với chức năng đưa một mẫu tin tức đầu vào, đầu ra là nhãn (Real hoặc Fake) của mẫu tin tức đó.

## **Hướng dẫn sử dụng**



# 🎓 Student Success Prediction

## 📌 Overview

This project builds a machine learning classification model to **predict student success in internship programs** based on academic performance, participation, and soft skills.  
The model helps educational institutions understand which factors most impact success and can guide targeted student support.

---

## 🗂️ Dataset

The dataset contains anonymized data for students with the following features:

| Feature               | Description                                 |
|-----------------------|---------------------------------------------|
| StudentID             | Unique student identifier                   |
| CGPA                  | Cumulative Grade Point Average              |
| ProjectsDone          | Number of academic or personal projects     |
| ParticipationHours    | Total hours of participation in activities  |
| Domain                | Preferred technical domain (e.g., AI, Web)  |
| CommunicationSkills   | Self-assessed soft skill rating             |
| Success               | Target variable (1 = success, 0 = not)      |

---

## 🛠️ Technologies Used

- **Python 3.12**
- **Pandas**, **NumPy** – Data handling
- **Matplotlib**, **Seaborn** – Data visualization
- **Scikit-learn** – ML models and evaluation
- **LabelEncoder**, **StandardScaler**, **Train-Test Split**

---

## 📊 Process

1. **Data Loading & Preprocessing**
   - Encoded categorical variables
   - Scaled numerical features

2. **Exploratory Data Analysis**
   - Heatmap of correlations
   - Class imbalance visualization

3. **Modeling**
   - Logistic Regression
   - Random Forest Classifier
   - Support Vector Machine (SVM)

4. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - Confusion Matrix

---

## 🧠 Results

| Model                | Accuracy |
|----------------------|----------|
| Logistic Regression  | 90%      |
| Random Forest        | 90%      |
| SVM                  | 75%      |

Random Forest performed best in terms of balanced precision and recall across classes.

---

## 📌 Conclusion

- CGPA, Participation Hours, and Communication Skills were the most influential features.
- Random Forest is recommended for deployment.
- The model provides a simple yet effective way to flag students who may need intervention or support during internships.

---

## 📁 Project Structure

```
student-success-prediction/
├── dataset.csv
├── student_success_prediction.ipynb
├── README.md
├── images/
│   └── model_accuracy.png
└── saved_models/
    └── student_success_model.pkl
```

---

---

## 🙋‍♀️ Author

**Hanifa**  
Aspiring Data Scientist | Python, ML & Data Visualization Enthusiast

---

## ⭐ If you found this useful, give it a ⭐ on GitHub!

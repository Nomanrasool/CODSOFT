# Titanic Survival Prediction

### Introduction
The Titanic Survival Prediction project aims to predict passenger survival based on parameters like Pclass, sex, age, Fare, and embarkation point. New features such as FamilySize and Alone status are added for improved predictions. The project involves data exploration, cleaning, visualization, and building two models: Linear Regression and Random Forest. The best-performing model is saved for future use.

### Code Overview
#### 1. Data Exploration and Cleaning
* Importing Libraries: The project starts by importing essential libraries such as NumPy, Pandas, Matplotlib, Seaborn, and sklearn for linear model, model selection, and metrics.
* Loading the Dataset: The Titanic dataset is loaded from a CSV file from Google Drive using Pandas.
* Data Inspection and Cleaning: Basic exploratory data analysis (EDA) is performed to understand the structure of the dataset. The absence of missing values is confirmed, and countplots and histograms are used to identify outliers in the features (Pclass, Sex, Age, Fare, Embarked, Alone, and FamilySize).
#### 2. Exploratory Data Analysis (EDA)
* Univariate Analysis: Histograms and count plots are created to analyze the distribution of the target variable (Survived). Pair plots and a heatmap are generated to visualize relationships and correlations between different variables.
* Correlation Analysis: The correlation heatmap highlights the correlation between variables, helping to identify influential features.
#### 3. Logistic Regression Model
* Model Building: The Logistic Regression model is initialized and trained using the training dataset.
* Model Evaluation: The model's performance is evaluated using accuracy, confusion matrix, and classification report.
#### 4. Random Forest Classifier
* Model Building: The Random Forest Classifier model is initialized and trained using the training dataset.
* Model Evaluation: The model's performance is evaluated using accuracy, confusion matrix, and classification report.
#### 5. Model Comparison and Conclusion
* Model Comparison: The confusion matrices and accuracy scores of both models are compared. The Random Forest model is identified as the superior model in terms of prediction accuracy and explanatory power.
* Conclusion: The project concludes by summarizing the key findings and insights from both models.
#### 6. Model Saving
* Saving the Model: The trained Random Forest Classifier model is saved using the Pickle library for future use.
<br/><br/>


# Project Report 
### Linear Regression vs Random Forest
* In comparing the two models, Random Forest Classifier outperforms Linear Regression in terms of both prediction accuracy and explanatory power. The Random Forest model has a higher accuracy (0.832) and weighted avg (0.83 0.83 0.83 179) compared to Linear Regression Model accuracy (0.793) and weighted avg (0.79 0.79 0.79 179).
### Conclusion and Recommendations
* The Random Forest Classifier is recommended for predicting Titanic passenger survival, with an accuracy of 0.832 compared to 0.793 for Logistic Regression. It shows superior performance in precision, recall, and f1-score, effectively capturing complex feature interactions. This model provides valuable insights into factors influencing survival and can guide further predictive modeling efforts.
### Future Work
* Future work could involve exploring more advanced machine learning techniques, feature engineering, and incorporating additional features for a more comprehensive analysis. Techniques such as gradient boosting or neural networks might further improve prediction accuracy. Additionally, conducting more extensive hyperparameter tuning and cross-validation could yield better model performance.

## Acknowledgments
This project was developed as part of a data science initiative. The dataset used is sourced from Kaggle, and the project code is available on https://github.com/Nomanrasool/CODSOFT/tree/main/Task-1. Special thanks to the previous contributors whose efforts laid the groundwork for this analysis.


### NOTE:- Before running the jupyter notebook please ensure that you have the necessary libraries installed.
pip install -r requirements.txt

## Running the Application
### 1. Download the code
* Download the provided Python script (titanic_app.py) to your local machine.
### 2. Download the Pre-trained Model
* Make sure you have the pre-trained Random Forest model file (rf_final_model.pkl) available. If you don't have it, you can train the model using the provided code and save it using Pickle.
### 3. Navigate to the Script Directory
* Open a terminal or command prompt and navigate to the directory where the titanic_app.py script is located.
### 4. Run the Streamlit App
#### i. Install Streamlit and Ngrok:

!pip install streamlit pyngrok

### ii. Run the Streamlit app

!streamlit run /content/drive/MyDrive/Task-1/titanic_app.py
!nohup streamlit run /content/drive/MyDrive/Task-1/titanic_app.py &

### iii. Set up Ngrok for Public URL:

from pyngrok import ngrok

public_url = ngrok.connect(8501)
print("Public Url: ", public_url)

### iv. Streamlit App Code:

Run the code of titanic_survival.app

### Access the Application
* After running the above commands, Ngrok will provide a public URL. Open this URL in your web browser to access the application.

### Use the Application
* The application will open in your web browser. Enter the values for Pclass, Sex, Age, Fare, Embarked, FamilySize, and isAlone input fields. Click the "Predict" button to see the survival prediction based on the entered values.
* Click the "Predict" button to see the predicted sales based on the entered values.



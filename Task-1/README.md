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

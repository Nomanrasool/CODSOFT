
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_path = '/content/drive/MyDrive/Task-1/final_rf_model.pkl'
model = joblib.load(model_path)

# Title of the app
st.title('Titanic Survival Prediction')

# Input features for prediction
pclass = st.selectbox('Pclass', [1, 2, 3])
sex = st.selectbox('Sex', [0, 1])
age = st.slider('Age', 0, 100, 25)
fare = st.slider('Fare', 0.0, 500.0, 30.0)
embarked = st.selectbox('Embarked', [0, 1, 2])
family_size = st.slider('FamilySize', 1, 11, 1)
is_alone = st.selectbox('isAlone', [0, 1])

# Create input DataFrame
input_data = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex],
    'Age': [age],
    'Fare': [fare],
    'Embarked': [embarked],
    'FamilySize': [family_size],
    'isAlone': [is_alone]
})

# Display the input data
st.write('Input data:', input_data)

# Predict survival
prediction = model.predict(input_data)[0]

# Display prediction result
if st.button('Predict'):
    if prediction == 1:
        st.success('The passenger would have survived.')
    else:
        st.error('The passenger would not have survived.')

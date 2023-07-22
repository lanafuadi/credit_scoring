import streamlit as st
import pickle
import pandas as pd

# Load the trained logistic regression model
with open('logreg_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit app code
def main():
    st.title('Credit Scoring Prediction App')
    st.write('Enter the feature values and click the "Predict" button to get credit scoring prediction.')

    # Define the feature names based on the new coefficients
    feature_names = ['loan_amnt', 'int_rate', 'annual_inc', 'dti', 'total_acc', 'initial_list_status', 'last_pymnt_amnt', 'pymnt_time']

    # Input fields for the features required for prediction
    feature_values = {}
    for feature_name in feature_names:
        default_value = 100.0 if 'loan_amnt' in feature_name else 10.0 if 'int_rate' in feature_name else 50000.0
        feature_values[feature_name] = st.number_input(feature_name, value=default_value, step=0.01)

    # Prepare the input data as a DataFrame with the same column names as in the training data
    input_data = pd.DataFrame(feature_values, index=[0])

    # Make predictions when the user clicks the "Predict" button
    if st.button('Predict'):
        # Perform any necessary preprocessing on the input data (e.g., scaling, encoding)
        # Make predictions using the loaded model
        prediction = model.predict(input_data)
        proba = model.predict_proba(input_data)[:, 1]

        # Display the prediction and probability
        st.write(f'Prediction: {"Good" if prediction[0] == 0 else "Bad"}')
        st.write(f'Probability of Default: {proba[0]:.4f}')

if __name__ == '__main__':
    main()

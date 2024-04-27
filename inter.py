import streamlit as st
import joblib
import pyowm

st.title('AC temperature based on Humidity')

model = joblib.load("model_gbr_s.joblib")


owm = pyowm.OWM("cbf37349dcb5ddf818d16aece7a0adc3")
weatehr_mrg = owm.weather_manager()
place = st.text_input("Enter the City Name")
observation = weatehr_mrg.weather_at_place(place)

humidity = observation.weather.humidity

col1_data_option = ["Low(16-18)","Mid(19-21)",'High(22-24)']
Temp_Choice = st.selectbox("Enter your Choice",col1_data_option)

if st.button('Submit'):
    if col1_data_option == "Low(16-18)":
        Temp_Choice = 1
        st.write(model.predict([[humidity,Temp_Choice]]))
    elif col1_data_option == "Mid(19-21)":
        Temp_Choice = 0
        st.write(model.predict([[humidity,Temp_Choice]]))
    else:
        Temp_Choice = 2
        st.write(model.predict([[humidity,Temp_Choice]]))
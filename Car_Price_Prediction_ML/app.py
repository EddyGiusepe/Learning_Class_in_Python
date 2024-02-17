"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro


Execução:
---------
$ streamlit run app.py
"""
import pandas as pd 
import numpy as np 
import pickle as pk 
import streamlit as st

model = pk.load(open('./model_salvo_de_Car.pkl','rb'))


# URL da sua imagem:
image_url = './Eddy_DataScientist.jpeg'
# Imagem na barra lateral:
st.sidebar.image(image_url, width=200, caption='')

# Meus Dados pessoais:
st.sidebar.header('ℹ️ :blue[Informações de contato] ℹ️')
st.sidebar.markdown('<span style="color:red;">Data Scientist.:</span> Dr. Eddy Giusepe Chirinos Isidro', unsafe_allow_html=True)
#st.sidebar.markdown('<span style="color:red;">Telefone:</span> (27) 9974-55087', unsafe_allow_html=True)
st.sidebar.markdown('<span style="color:red;">e-mail:</span> eddychirinos.unac@gmail.com', unsafe_allow_html=True)
st.sidebar.markdown('<span style="color:red;">[GitHub](https://github.com/EddyGiusepe)</span>', unsafe_allow_html=True)



st.header('🤗 Machine Learning: previsão de preço de carro 🤗')

cars_data = pd.read_csv('./Cardetails.csv')

def get_brand_name(car_name):
    car_name = car_name.split(' ')[0]
    return car_name.strip()

cars_data['name'] = cars_data['name'].apply(get_brand_name)

name = st.selectbox('Selecione a marca do carro', cars_data['name'].unique())
year = st.slider('Ano de fabricação do carro', 1994, 2024)
km_driven = st.slider('N.º de quilómetros percorridos', 11, 200000)
fuel = st.selectbox('Tipo de combustível', cars_data['fuel'].unique())
seller_type = st.selectbox('Tipo de vendedor', cars_data['seller_type'].unique())
transmission = st.selectbox('Tipo de transmissão', cars_data['transmission'].unique())
owner = st.selectbox('tipo de dono', cars_data['owner'].unique())
mileage = st.slider('Quilometragem do carro', 10,40)
engine = st.slider('CC do motor', 700,5000)
max_power = st.slider('Potência máxima', 0,200)
seats = st.slider('N.º de assentos', 5,10)


if st.button("predizer o preço"):
    input_data_model = pd.DataFrame(
            [[name, year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats]],
    columns=['name','year','km_driven','fuel','seller_type','transmission','owner','mileage','engine','max_power','seats'])
    
    input_data_model['owner'].replace(['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'],
                           [1,2,3,4,5], inplace=True)
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4], inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3], inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2], inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],
                          [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                          ,inplace=True)

    car_price = model.predict(input_data_model)

    st.markdown('O preço do carro, previsto, é '+ str(car_price[0]))

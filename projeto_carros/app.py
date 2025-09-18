import streamlit as st

st.sidebar.title("Aluguel de Carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolhao carro ideal para você!")
carros = ["Gol", "BMW", "Corsa", "Toro"]
st.sidebar.selectbox("selecione o modelo do carro:", carros)

st.sidebar.image("logo.png")
st.sidebar. titles(' kamilly carros')


carros = ['BMW', 'Mustang', 'Porsche', 'Fusca', 'Toro']

opcao = st.sidebar.selectbox('escolha o carro que foi alugado', carros)




st.title('Kamilly carros - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'por quantos dias a {opcao} foi alugado?')
km = st.text_input(f' quantos km vc rodou com a {opcao}')


if opcao == 'BMW':
    diaria = 450
elif opcao == 'mustang':
    diaria = 500
elif opcao == 'porsche': 
    diaria = 300
elif opcao == 'fusca':
    diaria = 250
elif opcao == 'toro':
    diaria = 500


if st.button('calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias}dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')
    
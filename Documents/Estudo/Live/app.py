import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_dados

def main():
    st.title("Sistema CRM de vendas - Master Data")
    
    email = st.text_input("Cadatre o email do vendedor")
    data = st.date_input("Data da venda", datetime.now())
    hora = st.time_input("Coloque a hora da venda",datetime.now().time())
    #hora = st.time_input("Coloque a hora da venda",value=time(9,0))
    valor = st.number_input("Coloque o valor da venda", min_value=0.0, format="%2.f")
    quantidade = st.number_input("Coloque a quantidade de vendas", min_value=1, step=1)
    produto = st.selectbox("Selecione o produto", ["Gemini","Chat-GPT", "Llama 3.0"])
    
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            
            venda = Vendas(
                email = email, 
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
                )
            
            st.write(venda)
            salvar_dados(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

    
if __name__ == "__main__":
    main()

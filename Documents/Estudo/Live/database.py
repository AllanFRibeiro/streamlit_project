import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv # busca a varialve setadas na execução da máquina
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def salvar_dados(dados: Vendas):
    """
   Função para salvar informações no banco de dados.
    
    Args:
        email: email do comprador
        data: data da compra
        valor: valor da compra
        produto: nome do produto
        quantidade: quantidade do produto
        produto: categoria do produto    
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port="5432"
        )
        cursor = conn.cursor()
        
        insert_quey = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_quey, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso!!!")
    except Exception as e:
        st.error(f"Erro ao salvar os dados no bando de dados: {e}")
        
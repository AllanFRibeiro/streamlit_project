from datetime import datetime
from typing import Tuple
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "Chat-GPT"
    produto3 = "Llama 3.0"
    
    
class Vendas(BaseModel):
    """
    Modelo de dados para as vendas.
    
    Args:
        email: email do comprador
        data: data da compra
        valor: valor da compra
        produto: nome do produto
        quantidade: quantidade do produto
        produto: categoria do produto    
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

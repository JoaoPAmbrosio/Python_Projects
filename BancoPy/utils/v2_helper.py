from datetime import date
from datetime import datetime


# Para receber uma data padrao americano e retorna-la no formato que constuma-se a ver no BR
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


# Para receber uma data no padrao BR e retorna-la no formato americano
def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
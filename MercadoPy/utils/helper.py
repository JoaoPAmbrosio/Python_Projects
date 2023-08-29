# Retorna valor com virgula e duas casas decimais (1788.59 -> R$ 1,788,59)
def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


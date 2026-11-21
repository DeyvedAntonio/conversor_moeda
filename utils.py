import locale

def formatar_moeda(valor):
    """
    Formata um valor inteiro ou float para moeda brasileira (R$).
    """
    try:
        # Configura o locale para Brasil
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        # Caso o locale não esteja disponível no sistema
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    # Usa formatação monetária do locale
    return locale.currency(valor, grouping=True)

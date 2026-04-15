def validar_no_vacio(valor):
    if valor.strip() == "":
        raise Exception("campo vacío")


def validar_numero_positivo(valor):
    if valor < 0:
        raise Exception("valor negativo")

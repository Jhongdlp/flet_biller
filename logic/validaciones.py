
def validar_cedula_ecuador(cedula):
    """Verifica si una cédula ecuatoriana es válida."""
    if len(cedula) != 10 or not cedula.isdigit():
        return False
    # Verificar el código de provincia
    provincia = int(cedula[0:2])
    if provincia < 1 or provincia > 24:
        return False
    
    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    digito_verificador = int(cedula[9])
    suma = 0
    
    for i in range(9):
        producto = int(cedula[i]) * coeficientes[i]
        if producto >= 10:
            producto -= 9
        suma += producto
    
    resultado = 10 - (suma % 10)
    if resultado == 10:
        resultado = 0
    
    return resultado == digito_verificador


def validar_ruc_ecuador(ruc):
    """Verifica si un RUC ecuatoriano es válido."""
    print(f"RUC recibido: {ruc}")
    if len(ruc) != 13 or not ruc.isdigit():
        print("Error: Longitud o formato incorrecto")
        return False

    # Verificar el tercer dígito (tipo de persona)
    tipo_persona = int(ruc[2])
    print(f"Tipo de persona: {tipo_persona}")
    if tipo_persona not in [0, 1, 2, 3, 4, 5, 6, 9]:
        print("Error: Tipo de persona inválido")
        return False

    # Coeficientes de acuerdo al tipo de persona
    if tipo_persona in [0, 1, 2, 3, 4, 5]:  # Persona natural
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        modulo = 10
        digito_verificador = int(ruc[9])  # Obtener el décimo dígito
    elif tipo_persona == 6:  # Entidad pública
        coeficientes = [3, 2, 7, 6, 5, 4, 3, 2]
        modulo = 11
        digito_verificador = int(ruc[8])  # Obtener el noveno dígito
    elif tipo_persona == 9:  # Sociedad privada o extranjera
        coeficientes = [4, 3, 2, 7, 6, 5, 4, 3, 2]
        modulo = 11
        digito_verificador = int(ruc[9])  # Obtener el décimo dígito
    else:
        print("Error: Tipo de persona inválido")
        return False

    print(f"Coeficientes usados: {coeficientes}")

    # Validación
    suma = 0
    for i in range(len(coeficientes)):
        producto = int(ruc[i]) * coeficientes[i]
        if tipo_persona in [0, 1, 2, 3, 4, 5] and producto >= 10:
            producto -= 9
        suma += producto
    print(f"Suma ponderada: {suma}")

    residuo = suma % modulo
    print(f"Residuo: {residuo}")

    resultado = 0 if residuo == 0 else modulo - residuo
    print(f"Resultado (antes de validar el último dígito): {resultado}")

    # Validación del último dígito
    if resultado != digito_verificador:
        print(f"Error: El dígito verificador no coincide: {resultado} != {digito_verificador}")
        return False

    print("RUC válido")
    return True



def validar_pasaporte_ecuador(pasaporte):
    """Placeholder para validación de pasaporte (flexible para extranjeros)."""
    # Agrega tu lógica aquí si necesitas un formato específico
    return True
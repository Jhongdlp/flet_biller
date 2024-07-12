def validar_ruc_ecuador(ruc):
    """Verifica si un RUC ecuatoriano es válido."""
    print(f"RUC recibido: {ruc}")
    
    # Verificar longitud y formato
    if len(ruc) != 13 or not ruc.isdigit():
        print("Error: Longitud o formato incorrecto")
        return False

    # Verificar el tercer dígito (tipo de persona)
    tipo_persona = int(ruc[2])
    print(f"Tipo de persona: {tipo_persona}")
    if tipo_persona not in [0, 1, 2, 3, 4, 5, 6, 9]:
        print("Error: Tipo de persona inválido")
        return False

    # Determinar coeficientes y modulo según el tipo de persona
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

    # Calcular la suma ponderada
    suma = 0
    for i in range(len(coeficientes)):
        suma += int(ruc[i]) * coeficientes[i]
    print(f"Suma ponderada: {suma}")

    # Calcular el residuo
    residuo = suma % modulo
    print(f"Residuo: {residuo}")

    # Calcular el dígito verificador esperado
    resultado = 0 if residuo == 0 else modulo - residuo
    # En caso de tipo_persona == 9 y resultado == 10, debe ser 0
    if tipo_persona == 9 and resultado == 10:
        resultado = 0
    print(f"Resultado (antes de validar el último dígito): {resultado}")

    # Validar el dígito verificador
    if resultado != digito_verificador:
        print(f"Error: El dígito verificador no coincide: {resultado} != {digito_verificador}")
        return False

    print("RUC válido")
    return True

# Ejemplo de prueba
ruc = "1790012345001"
validar_ruc_ecuador(ruc)

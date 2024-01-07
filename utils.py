def OMS_interpret(IMC):
    if IMC < 16.5:
        return "Maigreur extrême – dénutrition"
    elif IMC < 18.5:
        return "Maigreur"
    elif IMC < 25:
        return "Corpulence normale"
    elif IMC < 30:
        return "Surpoids ou pré-obésité"
    elif IMC < 35:
        return"Obésité modérée (classe I)"
    elif IMC < 40:
        return"Obésité sévère (classe II)"
    else:
        return "Obésité morbide (classe III)"
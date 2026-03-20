def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665

    horascompletas = (total_segundos // 3600)

    print(horascompletas)

    minutosrestantes = (total_segundos - horascompletas * 3600)//60

    print(minutosrestantes)

    segundosrestantes = (total_segundos - horascompletas * 3600 - minutosrestantes * 60)

    print(segundosrestantes)





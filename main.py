from datetime import datetime

def dias_ate_ferias(data_ferias):
    hoje = datetime.now().date()
    dias_restantes = (data_ferias - hoje).days
    return dias_restantes

def main():
    data_ferias = datetime(2023, 9, 7).date()  # (ano, mês, dia)
    dias_restantes = dias_ate_ferias(data_ferias)

    if dias_restantes > 0:
        print(f"Faltam {dias_restantes} dias para as suas férias!")
    elif dias_restantes == 0:
        print("As suas férias são hoje! Aproveite!")
    else:
        print("Suas férias já passaram. Espero que tenham sido ótimas!")

if __name__ == "__main__":
    main()

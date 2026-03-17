mes_num = int(input("Informe o número do mês: "))
meses = [0 ,"janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro" "dezembro"]

trimestre = meses.copy()
trimestre.pop(0)

trima = 0
if mes_num == 1:
    trima = "primeiro"
if mes_num == 2:
    trima = "primeiro"
if mes_num == 3:
    trima = "primeiro"
if mes_num == 4:
    trima = "segundo"
if mes_num == 5:
    trima = "segundo"
if mes_num == 6:
    trima = "segundo"
if mes_num == 7:
    trima = "terceiro"
if mes_num == 8:
    trima = "terceiro"
if mes_num == 9:
    trima = "terceiro"
if mes_num == 10:
    trima = "quarto"
if mes_num == 11:
    trima = "quarto"
if mes_num == 12:
    trima = "quarto"



print(f"O mês de {meses[mes_num]} é do {trima} trimestre do ano")
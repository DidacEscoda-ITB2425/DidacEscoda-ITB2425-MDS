
from datetime import datetime

dia = int(intput("introdueix el dia de neixament"))

mes = int(intput("introdueix el mes de neixament"))

any = int(intput("introdueix el any de neixament"))

if dia > 31:
    print("valor incorrecte")

elif mes > 12:
    print("valor incorrecte")

elif any > 2024:
    print("valor incorrecte")


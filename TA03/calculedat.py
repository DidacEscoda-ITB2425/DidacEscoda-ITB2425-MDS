
from datetime import datetime
try:
    dia = int(input("introdueix el dia de neixament"))
    mes = int(input("introdueix el mes de neixament"))
    any = int(input("introdueix el any de neixament"))
    any_actual = datetime.now().year


    if dia > 31:
        print("valor incorrecte")



    if any <= any_actual:
        if mes >=1 and mes <=12:
            if dia >=1 and dia <=31:
                    edat = any_actual-any
                    if edat >= 16 and edat <=65:
                        print ("pots treballar")
                    else:
                        print("no tens edat per treballar")
    else:
        print("any no valid")
except ValueError:
    print("malament")
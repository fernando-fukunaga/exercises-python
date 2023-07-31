import datetime
from typing import List


def intervalo_entre_datas(data1: str, data2: str) -> List[str]:
    formato_inicial = "%d-%m-%Y"
    formato_final = "%d%m%Y"

    lista_datas = []

    data_calculavel1 = datetime.datetime.strptime(data1, formato_inicial)
    data_calculavel2 = datetime.datetime.strptime(data2, formato_inicial)

    while data_calculavel1 <= data_calculavel2:
        lista_datas.append(data_calculavel1.strftime(formato_final))

        data_calculavel1 += datetime.timedelta(days=1)

    return lista_datas


data1 = "01-06-2023"
data2 = "30-06-2023"
print(intervalo_entre_datas(data1, data2))

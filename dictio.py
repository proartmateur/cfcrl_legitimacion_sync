from typing import List

arr = []
for i in range(0, 101):
    arr.append(str(i))

print(arr[100])

frutas = ["pera", "manzana", "uva", "fresa", "melon", "papaya", "frambuesa", "pátano", "piña", "sandia"]

frutas_mercado = {
    "pera": 3, "manzana": 6, "uva": 20, "fresa": 50, "melon": 15, "papaya": 10, "frambuesa": 50,
    "pátano": 5, "piña": 40, "sandia": 35
}


def find_fruta(nombre: str, frutas: List[str]) -> bool:
    """
    Búsqueda Lineal BigO(n)
    :param nombre: str
    :param frutas: List[str]
    :return: boll
    """
    precios = ["3", "6", "20", "50", "15", "10", "50", "5", "40", "35"]
    count = 0
    for fruta in frutas:
        if nombre == fruta:
            print(count, f"precio de {nombre} es {precios[count]} rupias")
            return True

        count += 1
    return False


def find_fruta_mercado(nombre: str, frutas: dict[str]) -> bool:
    """Búsqueda indexada BigO(1)"""
    print(f"precio de {nombre} es {frutas[nombre]} rupias")


# print(len(frutas))

# find_fruta("frambuesa", frutas)
find_fruta_mercado("frambuesa", frutas_mercado)

dicti = {
    "as":12,
    "b":2,
    "c":3
}

for k in dicti:
    print(k)
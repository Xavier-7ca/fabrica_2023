#PARA STARTAR UMA FUNÇÃO USA O (def)
#função serve para não ficar repetndo código 

def soma(x: int | float, y: int | float) -> int|float:
#soma x + y retorna o resultado
    return x + y

def print_subtracao(x: int | float, y: int | float) -> None:
        print(f"{x-y}")


def soma_sem_parametro() -> int | float:

    x = 5
    y = 5
    return x + y
from BombaCombustivel import BombaCombustivel

class BombaDiesel(BombaCombustivel):
    def __init__(self, valor_litro, quantidade_disponivel):
        super().__init__(valor_litro, quantidade_disponivel)

    def abastecer_por_valor(self, valor):
        if valor <= 0:
            return -1
        litros = valor / self._BombaCombustivel__valor_litro
        if litros > self._BombaCombustivel__quantidade_disponivel:
            return -1
        self._BombaCombustivel__quantidade_disponivel -= litros
        return litros

    def abastecer_por_litro(self, litros):
        if litros <= 0 or litros > self._BombaCombustivel__quantidade_disponivel:
            return -1
        valor = litros * self._BombaCombustivel__valor_litro
        self._BombaCombustivel__quantidade_disponivel -= litros
        return valor

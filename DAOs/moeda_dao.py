from DAOs.dao import DAO
from entidades.moeda import Moeda

#cada entidade terá uma classe dessa, implementação bem simples.
class MoedaDAO(DAO):
    def __init__(self):
        super().__init__('DAOs/pickles/moedas.pkl')

    def add(self, moeda: Moeda):
        if((moeda is not None) and isinstance(moeda, Moeda) and isinstance(moeda.nome, str)):
            super().add(moeda.nome, moeda)

    def update(self, moeda: Moeda):
        if((moeda is not None) and isinstance(moeda, Moeda) and isinstance(moeda.nome, str)):
            super().update(moeda.nome, moeda)

    def get(self, key:str):
            return super().get(key)

    def remove(self, key:str):
            return super().remove(key)
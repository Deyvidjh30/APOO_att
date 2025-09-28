from dao.item_dao import ItemDAO
from model.item import Item

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, descricao: str, quantidade: int):
        novo_item = Item(id=None, descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(novo_item)

    def obterTodosOsItens(self):
        return self.dao.listarTodos()

    def removerItem(self, id_item: int) -> bool:
        return self.dao.remover(id_item)

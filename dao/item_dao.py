from model.item import Item

class ItemDAO:
    def __init__(self):
        self.itens = []
        self._id_counter = 1

    def adicionar(self, item: Item):
        # Define ID automático
        item.id = self._id_counter
        self._id_counter += 1
        self.itens.append(item)

    def listarTodos(self):
        return self.itens
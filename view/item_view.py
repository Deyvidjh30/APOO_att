import streamlit as st
from controller.item_controller import ItemController

class ItemView:
    def __init__(self):
        self.controller = ItemController()

    def render(self):
        st.title("Cadastro de Itens")

        st.subheader("Adicionar novo item")
        with st.form("form_item"):
            descricao = st.text_input("Descrição")
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
            submit = st.form_submit_button("Cadastrar")

            if submit:
                if descricao.strip():
                    self.controller.criarItem(descricao, quantidade)
                    st.success(f"Item '{descricao}' cadastrado com sucesso!")
                else:
                    st.warning("⚠️ A descrição não pode estar vazia.")

        st.subheader("📋 Itens cadastrados")
        itens = self.controller.obterTodosOsItens()

        if itens:
            data = [{"ID": item.id, "Descrição": item.descricao, "Quantidade": item.quantidade} for item in itens]
            st.table(data)
            st.info(f"Total de itens cadastrados: {len(itens)}")
        else:
            st.info("Nenhum item cadastrado ainda.")

import streamlit as st
from controller.item_controller import ItemController

st.title("Cadastro de Itens (Memória)")

controller = ItemController()

# Formulário para o usuário cadastrar itens
st.subheader("Adicionar novo item")
with st.form("form_item"):
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    submit = st.form_submit_button("Cadastrar")

    if submit:
        if descricao.strip():
            controller.criarItem(descricao, quantidade)
            st.success("Item cadastrado com sucesso!")
        else:
            st.warning("Por favor, preencha a descrição.")

# Exibe os itens cadastrados
st.subheader("Itens cadastrados")
itens = controller.obterTodosOsItens()

if itens:
    for item in itens:
        st.write(f"**ID:** {item.id} | **Descrição:** {item.descricao} | **Quantidade:** {item.quantidade}")
else:
    st.info("Nenhum item cadastrado ainda.")
import streamlit as st

st.title("📚 Biblioteca Virtual")

st.write("Bem-vindo à nossa biblioteca online! Confira os livros disponíveis:")

livros = [
    {
        "titulo": "O cachorro Mágico",
        "imagem": "Cachorro Mágico.png.png"
    },
    {
        "titulo": "Coelho Celestial",
        "imagem": "coelho celestial.png"
    },
    {
        "titulo": "Coruja Encantada",
        "imagem": "coruja encantada.png"
    }
]

for livro in livros:
    st.image(livro["imagem"], width=100)
    st.subheader(livro["titulo"])
    
    if st.button(f"Emprestar '{livro['titulo']}'"):
        st.success(f"Você emprestou o livro '{livro['titulo']}'! Aproveite a leitura 📖")

    st.write("---") 

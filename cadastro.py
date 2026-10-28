import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ==================== BANCO DE DADOS ====================
banco = sqlite3.connect("escola76.db")
cursor = banco.cursor()

# --- CORREÇÃO DO ERRO ---
# Removemos a tabela antiga de 2 colunas para o banco aceitar a nova estrutura de 4 colunas
cursor.execute("DROP TABLE IF EXISTS alunos") 

# Cria a tabela correta com as 4 colunas necessárias
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
        nome TEXT, 
        nota REAL,
        curso TEXT,
        idade INTEGER
    )
""")
banco.commit()


# =========================
# FUNÇÕES
# =========================


def cadastrar():
    try:
        nome = entrada_nome.get().strip()
        idade_str = entrada_idade.get().strip()
        nota_str = entrada_nota.get().strip()
        curso = combo_curso.get()

        if nome == "":
            messagebox.showwarning("Atenção", "Digite o nome do aluno!")
            return

        if idade_str == "":
            messagebox.showwarning("Atenção", "Digite a idade do aluno!")
            return

        try:
            idade = int(idade_str)
            if idade <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Digite uma idade válida (número inteiro)!")
            return

        if nota_str == "":
            messagebox.showwarning("Atenção", "Digite a nota do aluno!")
            return

        nota = float(nota_str)

        if nota < 0 or nota > 10:
            messagebox.showwarning("Atenção", "A nota deve estar entre 0 e 10!")
            return

        if curso == "":
            messagebox.showwarning("Atenção", "Escolha um curso!")
            return

        # Agora o banco aceitará os 4 valores perfeitamente
        cursor.execute(
            "INSERT INTO alunos VALUES (?, ?, ?, ?)", (nome, nota, curso, idade)
        )
        banco.commit()

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_nota.delete(0, tk.END)
        combo_curso.current(0)
        listar()

    except ValueError:
        messagebox.showerror("Erro", "Digite uma nota válida!")


def listar():
    caixa_texto.delete("1.0", tk.END)

    cursor.execute("SELECT * FROM alunos")
    todos_alunos = cursor.fetchall()

    if len(todos_alunos) == 0:
        caixa_texto.insert(tk.END, "Nenhum aluno cadastrado.")
    else:
        for aluno in todos_alunos:
            if len(aluno) < 4:
                continue

            nome = aluno[0]
            nota = aluno[1]
            curso = aluno[2]
            idade = aluno[3]

            if nota >= 6:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            caixa_texto.insert(
                tk.END,
                f"Nome: {nome} | "
                f"Idade: {idade} anos | "
                f"Curso: {curso} | "
                f"Nota: {nota:.1f} | "
                f"{situacao}\n",
            )


def limpar():
    entrada_nome.delete(0, tk.END)
    entrada_idade.delete(0, tk.END)
    entrada_nota.delete(0, tk.END)
    combo_curso.current(0)
    caixa_texto.delete("1.0", tk.END)


def resetar_lista():
    confirmar = messagebox.askyesno(
        "Confirmar", "Tem certeza que deseja apagar TODOS os alunos do banco?"
    )

    if confirmar:
        cursor.execute("DELETE FROM alunos")
        banco.commit()
        caixa_texto.delete("1.0", tk.END)
        messagebox.showinfo("Reset", "A lista de alunos foi resetada!")


# =========================
# JANELA
# =========================

janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("600x620")

# =========================
# TÍTULO
# =========================

tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 16, "bold")).pack(pady=15)


# =========================
# NOME
# =========================

tk.Label(janela, text="Nome do aluno:").pack(pady=(5, 5))
entrada_nome = tk.Entry(janela, width=40)
entrada_nome.pack()


# =========================
# IDADE
# =========================

tk.Label(janela, text="Idade:").pack(pady=(10, 5))
entrada_idade = tk.Entry(janela, width=40)
entrada_idade.pack()


# =========================
# NOTA
# =========================

tk.Label(janela, text="Nota:").pack(pady=(10, 5))
entrada_nota = tk.Entry(janela, width=40)
entrada_nota.pack()


# =========================
# CURSO
# =========================

tk.Label(janela, text="Escolha um curso:").pack(pady=(10, 5))
combo_curso = ttk.Combobox(
    janela,
    values=["ADS", "Ciência da Computação", "Sistemas de Informação"],
    state="readonly",
    width=37,
)
combo_curso.current(0)
combo_curso.pack()


# =========================
# BOTÕES
# =========================

tk.Button(janela, text="Cadastrar", width=15, command=cadastrar).pack(pady=10)
tk.Button(janela, text="Listar Alunos", width=15, command=listar).pack(pady=5)
tk.Button(janela, text="Limpar", width=15, command=limpar).pack(pady=5)
tk.Button(janela, text="Resetar Lista", width=15, command=resetar_lista).pack(pady=5)


# =========================
# CAIXA DE TEXTO
# =========================

caixa_texto = tk.Text(janela, width=70, height=12)
caixa_texto.pack(pady=15)

listar()

# =========================
# INICIAR PROGRAMA
# =========================
janela.mainloop()

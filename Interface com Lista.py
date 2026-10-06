import tkinter as tk
from tkinter import ttk, messagebox

# Lista de alunos
alunos = []


# =========================
# FUNÇÕES
# =========================

def cadastrar():
    try:
        nome = entrada_nome.get()
        nota = float(entrada_nota.get())
        curso = combo_curso.get()

        if nome == "":
            messagebox.showwarning(
                "Atenção",
                "Digite o nome do aluno!"
            )
            return

        if nota < 0 or nota > 10:
            messagebox.showwarning(
                "Atenção",
                "A nota deve estar entre 0 e 10!"
            )
            return

        if curso == "":
            messagebox.showwarning(
                "Atenção",
                "Escolha um curso!"
            )
            return

        alunos.append([nome, nota, curso])

        messagebox.showinfo(
            "Sucesso",
            "Aluno cadastrado com sucesso!"
        )

        entrada_nome.delete(0, tk.END)
        entrada_nota.delete(0, tk.END)
        combo_curso.current(0)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite uma nota válida!"
        )


def listar():
    caixa_texto.delete("1.0", tk.END)

    if len(alunos) == 0:
        caixa_texto.insert(
            tk.END,
            "Nenhum aluno cadastrado."
        )
    else:
        for aluno in alunos:
            nome = aluno[0]
            nota = aluno[1]
            curso = aluno[2]

            if nota >= 6:
                situacao = "Aprovado"
            else:
                situacao = "Reprovado"

            caixa_texto.insert(
                tk.END,
                f"Nome: {nome} | "
                f"Curso: {curso} | "
                f"Nota: {nota:.1f} | "
                f"{situacao}\n"
            )


def limpar():
    entrada_nome.delete(0, tk.END)
    entrada_nota.delete(0, tk.END)
    combo_curso.current(0)
    caixa_texto.delete("1.0", tk.END)


def resetar_lista():
    alunos.clear()
    caixa_texto.delete("1.0", tk.END)

    messagebox.showinfo(
        "Reset",
        "A lista de alunos foi resetada!"
    )


# =========================
# JANELA
# =========================

janela = tk.Tk()

janela.title("Cadastro de Alunos")
janela.geometry("600x550")

# =========================
# TÍTULO
# =========================

tk.Label(
    janela,
    text="Cadastro de Alunos",
    font=("Arial", 16, "bold")
).pack(pady=15)


# =========================
# NOME
# =========================

tk.Label(
    janela,
    text="Nome do aluno:"
).pack(pady=(5, 5))

entrada_nome = tk.Entry(
    janela,
    width=40
)

entrada_nome.pack()


# =========================
# NOTA
# =========================

tk.Label(
    janela,
    text="Nota:"
).pack(pady=(10, 5))

entrada_nota = tk.Entry(
    janela,
    width=40
)

entrada_nota.pack()


# =========================
# CURSO
# =========================

tk.Label(
    janela,
    text="Escolha um curso:"
).pack(pady=(10, 5))

combo_curso = ttk.Combobox(
    janela,
    values=[
        "ADS",
        "Ciência da Computação",
        "Sistemas de Informação"
    ],
    state="readonly",
    width=37
)

combo_curso.current(0)
combo_curso.pack()


# =========================
# BOTÕES
# =========================

tk.Button(
    janela,
    text="Cadastrar",
    width=15,
    command=cadastrar
).pack(pady=10)

tk.Button(
    janela,
    text="Listar Alunos",
    width=15,
    command=listar
).pack(pady=5)

tk.Button(
    janela,
    text="Limpar",
    width=15,
    command=limpar
).pack(pady=5)

tk.Button(
    janela,
    text="Resetar Lista",
    width=15,
    command=resetar_lista
).pack(pady=5)


# =========================
# CAIXA DE TEXTO
# =========================

caixa_texto = tk.Text(
    janela,
    width=70,
    height=12
)

caixa_texto.pack(pady=15)


# =========================
# INICIAR PROGRAMA
# =========================

janela.mainloop()

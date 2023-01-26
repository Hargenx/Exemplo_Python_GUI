import tkinter as tk
from typing import Any, Callable

from model import Model

TITULO = "Lista De Tarefas"


class TodoList(tk.Tk):
    def __init__(self, model: Model) -> None:
        super().__init__()
        self.model = model
        self.title(TITULO)
        self.geometry("500x300")
        self.criar_ui()
        self.atualizar_lista_tarefas()

    def criar_ui(self) -> None:
        self.frame = tk.Frame(self, padx=10, pady=10)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.lista_tarefa = tk.Listbox(
            self.frame,
            height=10,
            activestyle="none",
        )
        self.lista_tarefa.bind("<FocusOut>", self.saindo_do_foco)
        self.lista_tarefa.bind("<<ListboxSelect>>", self.tarefa_em_selecao)
        self.lista_tarefa.pack(fill=tk.X)

        self.entrada_principal = tk.Entry(self.frame)
        self.entrada_principal.pack(fill=tk.X)

        self.apagar_botao_tarefa = tk.Button(
            self.frame,
            text="Apagar",
            width=6,
            pady=5,
            state=tk.DISABLED,
        )
        self.apagar_botao_tarefa.pack(side=tk.TOP, anchor=tk.NE)

    def ligar_apagar_tarefa(self, callback: Callable[[tk.Event], None]) -> None:
        self.apagar_botao_tarefa.bind("<Button-1>", callback)

    def ligar_criacao_tarefa(self, callback: Callable[[tk.Event], None]) -> None:
        self.entrada_principal.bind("<Return>", callback)

    def obter_texto_entrada(self) -> str:
        return self.entrada_principal.get()

    def limpar_entrada(self) -> None:
        self.entrada_principal.delete(0, "end")

    @property
    def tarefa_selecionada(self) -> str:
        return self.lista_tarefa.get(self.lista_tarefa.curselection())

    def tarefa_em_selecao(self, event=None) -> None:
        self.apagar_botao_tarefa.config(state=tk.NORMAL)

    def saindo_do_foco(self, event=None) -> None:
        self.lista_tarefa.selection_clear(0, tk.END)
        self.apagar_botao_tarefa.config(state=tk.DISABLED)

    def atualizar_lista_tarefas(self) -> None:
        self.lista_tarefa.delete(0, tk.END)
        for item in self.model.obter_tarefa():
            self.lista_tarefa.insert(tk.END, item)
        self.apagar_botao_tarefa.config(state=tk.DISABLED)
        self.lista_tarefa.yview(tk.END)

from model import Model
from view import TodoList


class Controller:
    def __init__(self, model: Model, view: TodoList) -> None:
        self.model = model
        self.view = view
        self.view.ligar_criacao_tarefa(self.criar_tarefa)
        self.view.ligar_apagar_tarefa(self.apagar_tarefa)

    def criar_tarefa(self, event=None) -> None:
        task = self.view.obter_texto_entrada()
        self.view.limpar_entrada()
        self.model.criar_tarefa(task)
        self.view.atualizar_lista_tarefas()

    def apagar_tarefa(self, event=None) -> None:
        self.model.apagar_tarefa(self.view.tarefa_selecionada)
        self.view.atualizar_lista_tarefas()

    def run(self) -> None:
        self.view.mainloop()

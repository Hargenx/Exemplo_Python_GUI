import sqlite3


class Model:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("tarefa.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tarefas (tarefa TEXT);")

    def criar_tarefa(self, tarefa: str) -> None:
        self.cursor.execute("insert into tarefas values (?)", (tarefa,))
        self.connection.commit()

    def apagar_tarefa(self, tarefa: str) -> None:
        self.cursor.execute("delete from tarefas where tarefa = ?", (tarefa,))
        self.connection.commit()

    def obter_tarefa(self) -> list[str]:
        tarefas: list[str] = []
        for row in self.cursor.execute("select tarefa from tarefas"):
            tarefas.append(row[0])
        return tarefas

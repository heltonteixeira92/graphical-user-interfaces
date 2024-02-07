import flet as ft


class Task(ft.UserControl):
    """Classe que representa uma tarefa na lista de tarefas"""

    def __init__(self, task_name, task_delete, task_status_change=None):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_delete = task_delete
        self.task_status_change = task_status_change

    def build(self):
        # Interface para a exibição da tarefa
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

        # Interface para a edição da tarefa
        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),

                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-DO",
                    on_click=self.save_clicked,
                ),
            ],
        )
        # Retorna um layout de coluna contendo ambas as interfaces
        return ft.Column(controls=[self.display_view, self.edit_view])

    def edit_clicked(self, e):
        # Chamado quando o botão de edição é clicado
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        # Chamado quando o botão de salvamento é clicado
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()


class TodoApp(ft.UserControl):
    """Classe principal da aplicação To-Do"""

    def build(self):
        # Interface Principal da aplicação
        self.new_task = ft.TextField(hint_text="Whats needs to be done??", expand=True)
        self.tasks = ft.Column()

        return ft.Column(
            width=600,
            controls=[
                ft.Row(controls=[
                        self.new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        # Chamado quando o botão de adição é clicado
        task = Task(self.new_task.value, task_delete=self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_delete(self, task):
        # Chamado para excluir uma tarefa
        self.tasks.controls.remove(task)
        self.update()


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = 'ToDo App'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    todo = TodoApp()

    # add application's root control to the page
    page.add(todo)


# Inicia a aplicação
ft.app(target=main)

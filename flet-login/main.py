import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'Signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False

    # Setup our fields
    text_username: ft.TextField = ft.TextField(label='username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: ft.TextField = ft.TextField(label='username', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: ft.Checkbox = ft.Checkbox(label='I agree to stuff', value=False)
    button_submit: ft.ElevatedButton = ft.ElevatedButton(text='Sign up', width=200, disabled=True)

    def validate(e: ft.ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True

    def submit(e: ft.ControlEvent) -> None:
        print('username', text_username.value)
        print('password', text_password.value)

        page.clean()
        page.add(
            ft.Row(
                controls=[ft.Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    # link the function to our UI
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit

    # Render the page sign-up page
    page.add(
        ft.Row(
            controls=[
                ft.Column([
                    text_username,
                    text_password,
                    checkbox_signup,
                    button_submit
                ])
            ]
        )
    )


if __name__ == '__main__':
    ft.app(target=main)

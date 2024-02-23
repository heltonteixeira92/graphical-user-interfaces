import flet as ft


def main(page: ft.Page) -> None:
    page.title = 'My store'

    def route_change(e: ft.RouteChangeEvent) -> None:
        page.views.clear()

        # Home view
        page.views.append(
            ft.View(
                route='/',
                controls=[
                    ft.AppBar(title=ft.Text('Home'), bgcolor='blue'),
                    ft.Text(value='Home', size=30),
                    ft.ElevatedButton(text='Go to sotre', on_click=lambda _: page.go('/store'))
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=26
            )
        )

        # Store view
        if page.route == '/store':
            page.views.append(
                ft.View(
                    route='/store',
                    controls=[
                        ft.AppBar(title=ft.Text('Store'), bgcolor='blue'),
                        ft.Text(value='Store', size=30),
                        ft.ElevatedButton(text='Go back', on_click=lambda _: page.go('/'))
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=26
                )
            )
        page.update()

    def view_pop(e: ft.ViewPopEvent) -> None:
        page.views.pop()
        top_view: ft.View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main)

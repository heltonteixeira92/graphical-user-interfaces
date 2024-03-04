import json

import flet as ft


# Login Page
class Login(ft.UserControl):
    def __init__(self):
        super(Login, self).__init__()
        self.username = ft.TextField(label='username')
        self.password = ft.TextField(label='password')

    def build(self):
        return ft.Container(
            bgcolor='#b1b1b1',
            content=ft.Column([
                ft.Text('Login Account', size=30),
                self.username,
                self.password,
                ft.Row(controls=[
                    ft.ElevatedButton("Login Now",
                                      bgcolor="blue", color="white",
                                      on_click=self.loginbtn
                                      ),
                    ft.ElevatedButton("Register",
                                      bgcolor='blue', color="white",
                                      on_click=lambda _: self.page.go('register'))

                ])])
        )

    def loginbtn(self, e):
        # Write your input to login.json
        # with open('login.json') as file:
        # file = open('login.json')
        # data = json.load(file)
        data = {'users': [{
            'username': 'helton', 'password': '12'
        }]}

        username = self.username.value
        password = self.password.value

        # check login
        for user in data['users']:
            if user['username'] == username and user['password'] == password:
                print('you success login')

                # if success login then create sessions

                data_login = {
                    'value': True,
                    'username': self.username.value
                }

                # create session
                self.page.session.set("login", data_login)
                # redirect to private page if you have this session
                print(self.page.session.get("login"))
                self.page.go("/privatepage")
                # self.page.update()

            else:
                # If wrong show snackbar message
                # print("wrong login")
                self.page.snack_bar = ft.SnackBar(
                    ft.Text('wrong login', size=30)
                )

                self.page.snack_bar.open = True
                self.page.update()


class PrivatePage(ft.UserControl):
    def __init__(self):
        super(PrivatePage, self).__init__()

    def build(self):
        return ft.Container(
            bgcolor="blue20",
            content=ft.Column([
                ft.Text("Welcom to your page again", size=30),
                ft.ElevatedButton("logout now", on_click=self.logout)
            ])

        )

    def logout(self, e):
        self.page.session.clear()
        self.page.go('/')
        self.page.update()


class Register(ft.UserControl):
    def __init__(self):
        super(Register, self).__init__()
        self.username = ft.TextField(label="username")
        self.password = ft.TextField(label="password")

    def build(self):
        return ft.Container(
            bgcolor="#b1b1b1",
            padding=10,
            content=ft.Column([
                ft.Text('Register your Account', size=30),
                self.username,
                self.password,
                ft.ElevatedButton("Register Now",
                                  on_click=self.register)
            ])
        )

    def register(self, e):
        new_user = {
            "username": self.username.value,
            "password": self.password.value
        }

        data = {"users": []}

        data["users"].append(new_user)
        with open("login.json", "w") as file:
            json_string = json.dumps(data)
            file.write(json_string)

        data_login = {
            'value': True,
            'username': self.username.value
        }
        print(data_login)

        self.page.session.set('login', data_login)

        self.page.go('/privatepage')
        # self.page.update()


def main(page: ft.Page):
    login = Login()
    private_page = PrivatePage()
    register = Register()

    def my_route(route):
        # clear all pages
        page.views.clear()
        # append route and page
        page.views.append(
            ft.View(
                "/",
                [login]
            )
        )
        # page.views.append(
        #     ft.View(
        #         "/privatepage",
        #         [private_page]
        #     )
        # )

        # create second page (private page)
        if page.route == "/privatepage":
            print(page.session.get('login'))
            if not page.session.get('login'):
                # login url
                page.go('/')
            else:
                page.views.append(
                    ft.View(
                        "/privatepage",
                        [private_page]
                    )
                )
        elif page.route == 'register':
            page.views.append(
                ft.View(
                    "/register",
                    [register]
                )

            )

    page.on_route_change = my_route
    page.go("/")


# if __name__ == '__main__':
ft.app(target=main)

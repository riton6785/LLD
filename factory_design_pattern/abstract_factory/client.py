from theme_factory import (
    LightThemeFactory,
    DarkThemeFactory
)


class Client:

    @staticmethod
    def render_ui(factory):

        button = factory.create_button()
        checkbox = factory.create_checkbox()

        print(button.render())
        print(checkbox.render())


if __name__ == "__main__":

    print("Light Theme")

    Client.render_ui(
        LightThemeFactory()
    )

    print()

    print("Dark Theme")

    Client.render_ui(
        DarkThemeFactory()
    )

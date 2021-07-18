from models import ButtonFactory


if __name__ == "__main__":
    button_obj = ButtonFactory()
    button = ['image', 'input', 'flash']
    for b in button:
        print(button_obj.create_button(b).get_html())
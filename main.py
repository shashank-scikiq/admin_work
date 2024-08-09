from send_email import send_message
from processData import get_update


def main():
    message = get_update()
    # print("Final Message", message)
    send_message(message)


if __name__ == "__main__":
    main()

from send_email import send_message
from processData import get_update
import os 
import sys


def main():
    message = get_update()
    send_message(message)


if __name__ == "__main__":
    env_vars = ['SAMPLE_SPREADSHEET_ID', 'SAMPLE_RANGE_NAME',
                'SENDER','RECEIVER']
    for env in env_vars:
        if env not in os.environ.keys():
            print(env, " not found in environment variables.")
            sys.exit()
    print("All Envs found. Proceeding.")
    main()

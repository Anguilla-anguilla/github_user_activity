import argparse
from api_get_info import get_user_information


def main():
    parser = argparse.ArgumentParser(prog='activity',
                                     description='Shows recent activity on GitHub')
    parser.add_argument('username', type=str, help='Username')

    args = parser.parse_args()

    if args.username != '':
        get_user_information(args.username)
    else:
        print('Error: no username has found.')


if __name__ == '__main__':
    main()
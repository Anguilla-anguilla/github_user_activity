import json
import urllib.error as err
import urllib.request as req


def get_user_information(username):
    endpoint = f'https://api.github.com/users/{username}/events'
    try:
        responce = req.urlopen(endpoint)
        content = responce.read()
        json_data = json.loads(content)

        if len(json_data) > 0:
            print(f"{username}'s recent activity:")
            print(json_data)
            # for activity in json_data:
            #     print('- ')gi
        else:
            print(f"No activities.")

    except err.URLError as URL_err:
        print(f'URL error: {URL_err}')
    except err.HTTPError as HTTP_err:
        print(f'HTTP error: {HTTP_err}')
    except json.JSONDecodeError as JSON_err:
        print(f'JSON error: {JSON_err}')
    except Exception as exc:
        print(f'Error: {exc}')
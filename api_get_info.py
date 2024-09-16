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
            for event in json_data:
                e_type = event['type']
                repo = event['repo']['name']
                payload = event['payload']
                if e_type == 'CreateEvent':
                    print(f'- created {payload["ref_type"]} for "{repo}" repo')
                elif e_type == 'DeleteEvent':
                    print(f'- deleted {payload["ref_type"]} for "{repo}" repo')
                elif e_type == 'ForkEvent':
                    print(f' fork "{repo}" repo')
                elif e_type == 'IssuesEvent':
                    print(f'- {payload["action"]} issue for "{repo}" repo')
                elif e_type == 'PublicEvent':
                    print(f'- made repository "{repo}" public.')
                elif e_type == 'PullRequestEvent':
                    print(f'- {payload["action"]} pull request for "{repo}" repo')
                elif e_type == 'PushEvent':
                    print(f'- pushed {len(payload["commits"])} commits for "{repo}" repo')
                elif e_type == 'WatchEvent':
                    print(f'- {payload["action"]} "{repo}" repo')

    except err.URLError as URL_err:
        print(f'URL error: {URL_err}')
    except err.HTTPError as HTTP_err:
        print(f'HTTP error: {HTTP_err}')
    except json.JSONDecodeError as JSON_err:
        print(f'JSON error: {JSON_err}')
    except Exception as exc:
        print(f'Error: {exc}')
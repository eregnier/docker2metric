from sys import argv
from os import environ
from json import dumps

from requests import post
from dotenv import load_dotenv

from docker2metric import get_docker_metrics


def main():
    metrics = get_docker_metrics()
    if '--send' in argv:
        url = environ.get("API_EVENT_URL", None)
        if url is None:
            print('Cannot send metrics to API_URL from .env file as it is not defined')
        load_dotenv()
        for metric in metrics:
            result = post(url, json=metric).status_code
            print(
                "{} {} {}".format(
                    "[OK]" if result == 200 else "[KO]", payload["origin"], payload["type"]
                )
            )
    else:
        print(dumps(metrics, indent=2))


if __name__ == '__main__':
    main()

import requests
import pandas as pd


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def remove_first_3_line(file_object):
    if file_object is not None:
        with open("updated_connections.csv", "wb") as updated_file:
            next(file_object)
            next(file_object)
            next(file_object)
            for line in file_object:
                updated_file.write(line)

        return pd.read_csv("updated_connections.csv")

    return pd.read_csv("okkar_connections.csv")

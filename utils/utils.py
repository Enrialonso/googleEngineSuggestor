import json
import os
from string import ascii_lowercase
from datetime import datetime as dt

from utils.config import session_path, input_path, stop_words_path


def store_cookies(cookies: dict) -> None:
    with open(session_path, "w", encoding="utf-8") as file:
        file.write(json.dumps(cookies, indent=4))


def path_exists(session_path: str) -> bool:
    return os.path.exists(session_path)


def get_cookies() -> dict:
    with open(session_path, "r", encoding="utf-8") as file:
        return json.loads(file.read())


def read_input():
    if path_exists(input_path):
        with open(input_path, "r", encoding="utf-8") as file:
            return list(filter(lambda x: x, file.read().split("\n")))
    else:
        raise Exception("Not input file!")


def check_gdpr(page):
    try:
        page.query_selector("text=Acepto").click()
    except Exception:
        print("GDPR not present")


def generate_inputs_search_stop_words(word: str) -> list:
    with open(stop_words_path, "r", encoding="utf-8") as file:
        stop_words = list(filter(lambda x: x, file.read().split("\n")))
    return [f"{word} {stop_word}" for stop_word in stop_words]


def generate_inputs_search(word: str) -> list:
    return [f"{word} {letter}" for letter in ascii_lowercase]


def store_output(list_output):
    with open(f"{os.getcwd()}/output/output_{dt.now().strftime('%Y%M%d%H%M')}.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(list_output))

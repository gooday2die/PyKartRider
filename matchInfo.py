import requests
import apiKey


def get_all_matches(user_id):
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/" + user_id + "/matches").encode("utf-8"),
                     headers={'Authorization': apiKey.key})

    return r.json()
import requests
import apiKey


class Match:
    def __init__(self, json_data):
        self.json_data = json_data
        self.match_id = json_data['matchId']
        self.match_type = json_data['matchType']
        self.character = json_data['character']
        self.start_time = json_data['startTime']
        self.end_time = json_data['endTime']

def get_all_matches(user_id):
    """
    A function that retrieves all matches from a user
    :param user_id: User id to retrive from. User id comes from userInfo
    :return: returns json type of all matches.
    """
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/" + user_id + "/matches").encode("utf-8"),
                     headers={'Authorization': apiKey.key})

    return r.json()

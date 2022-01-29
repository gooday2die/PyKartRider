import requests
from PyKartRider import jsonInfo
from PyKartRider import apiKey


class Match:
    """
    A class for representing a single match
    """

    def __init__(self, json_data):
        """
        Initializer method
        :param json_data: the json to load as match
        """
        print(json_data)
        self.json_data = json_data
        self.match_id = json_data['matchId']
        self.match_type = json_data['matchType']
        self.track = jsonInfo.get_track_info(json_data['trackId'])
        self.character = jsonInfo.get_character_info(json_data['character'])
        self.start_time = json_data['startTime']
        self.end_time = json_data['endTime']
        self.match_rank = json_data['player']['matchRank']
        self.match_retired = json_data['player']['matchRetired']
        self.match_win = json_data['player']['matchWin']
        self.player_count = json_data['playerCount']
        self.kart = jsonInfo.get_kart_info(json_data['player']['kart'])
        self.flying_pet = jsonInfo.get_flying_pet_info(json_data['player']['flyingPet'])
        self.pet = jsonInfo.get_pet_info(json_data['player']['pet'])

    def __repr__(self):
        """
        A repr method for representing this object and class
        :return: returns __repr__ string that
        """
        return ("===== Match ID %s =====\n"
                "Track Name : %s\nStart Time : %s\nEnd Time : %s\nMatch Rank : %s\nMatch Win : %s\n"
                "Player Count : %s\nPlayer Kart : %s\nPlayer Flying Pet : %s\nPlayer Pet : %s\n"
                % (self.match_id, self.track, self.start_time, self.end_time,
                   self.match_rank, self.match_win, self.player_count, self.kart, self.flying_pet, self.pet))

    def get_json_data(self):
        """
        A getter methods.
        :return:
        """
        return self.json_data

    def get_match_id(self):
        return self.match_id

    def get_match_type(self):
        return self.match_win

    def get_character(self):
        return self.character

    def get_start_tile(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def get_match_rank(self):
        return self.match_rank

    def get_match_retired(self):
        return self.match_retired

    def get_match_win(self):
        return self.match_win

    def get_kart(self):
        return self.kart

    def get_pet(self):
        return self.pet

    def get_flying_pet(self):
        return self.flying_pet

    def get_track(self):
        return self.track


def get_all_matches(user_id):
    """
    A function that retrieves all matches from a user
    :param user_id: User id to retrive from. User id comes from userInfo
    :return: returns json type of all matches.
    """
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/" + user_id + "/matches").encode("utf-8"),
                     headers={'Authorization': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTcyODUwNjU5NSIsImF1dGhfaWQiOiIyIiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIiwic2VydmljZV9pZCI6IjQzMDAxMTM5MyIsIlgtQXBwLVJhdGUtTGltaXQiOiI1MDA6MTAiLCJuYmYiOjE2NDMyNzE2NDAsImV4cCI6MTY1ODgyMzY0MCwiaWF0IjoxNjQzMjcxNjQwfQ.2DVXqObm6S77Dy2s6MwPumCfB7-BaXFeufWC_kvBSU0"})

    return r.json()

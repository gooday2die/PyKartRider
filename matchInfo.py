import requests
import apiKey


class Match:
    """
    A class for representing a single match
    """
    def __init__(self, json_data):
        """
        Initializer method
        :param json_data: the json to load as match
        """
        self.json_data = json_data
        self.match_id = json_data['matchId']
        self.match_type = json_data['matchType']
        self.character = json_data['character']
        self.start_time = json_data['startTime']
        self.end_time = json_data['endTime']
        self.match_rank = json_data['player']['matchRank']
        self.match_retired = json_data['player']['matchRetired']
        self.match_win = json_data['player']['matchWin']

    def __repr__(self):
        """
        A repr method for representing this object and class
        :return: returns __repr__ string that
        """
        return("ID : %s / Type : %s / Character : %s / Start Time : %s "
               "/ End Time :%s / Rank : %s / Retired : %s / Win : %s" %
              (self.match_id, self.match_type, self.character, self.start_time, self.end_time,
               self.match_rank, self.match_retired, self.match_win))

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


def get_all_matches(user_id):
    """
    A function that retrieves all matches from a user
    :param user_id: User id to retrive from. User id comes from userInfo
    :return: returns json type of all matches.
    """
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/" + user_id + "/matches").encode("utf-8"),
                     headers={'Authorization': apiKey.key})

    return r.json()

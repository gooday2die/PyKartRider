import requests

from PyKartRider import jsonInfo
from PyKartRider import apiKey

class UserNotFoundException(Exception):
    """
    A class for exception when user is not found
    """
    pass


class UnKnownException(Exception):
    """
    A class for exception when unknown error happened
    """
    pass


def get_user_id(username):
    """
    A function that retrieves user id by username
    :param username: the username to retrieve id from
    :return: tuple type of (id, level)
    """
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/nickname/" + username).encode("utf-8"),
                     headers={'Authorization': apiKey.key})
    if r.status_code == 200:
        user_id = r.json()['accessId']
        user_level = r.json()['level']

        return user_id, user_level

    elif r.status_code == 404:
        raise UserNotFoundException

    else:
        raise UnKnownException


def get_user_name(user_id):
    """
    A function that retrieves username by id
    :param user_id: the user id to retrive name from
    :return: tupe type of (username, level)
    """
    r = requests.get(("https://api.nexon.co.kr/kart/v1.0/users/" + user_id).encode("utf-8"),
                     headers={'Authorization': apiKey.key})
    if r.status_code == 200:
        user_id = r.json()['name']
        user_level = r.json()['level']

        return user_id, user_level

    elif r.status_code == 404:
        raise UserNotFoundException

    else:
        raise UnKnownException

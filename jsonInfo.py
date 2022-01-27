import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


class idNotFoundException(Exception):
    """
    A exception class for id not found
    """
    pass


def get_character_info(item_id):
    """
    A function that gets character name information from item id
    :param item_id: the item id to find
    :return: the String type name of character
    """
    f = open(str(dir_path) + r"/metadata/json/character.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException


def get_flying_pet_info(item_id):
    """
    A function that gets flying pet name information from item id
    :param item_id: the item id to find
    :return: the String type name of flying pet
    """
    f = open(str(dir_path) + r"/metadata/json/flyingPet.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException


def get_game_type_info(item_id):
    """
    A function that gets game type information from item id
    :param item_id: the item id to find
    :return: the String type name of game type
    """
    f = open(str(dir_path) + r"/metadata/json/gameType.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException


def get_kart_info(item_id):
    """
    A function that gets kart name information from item id
    :param item_id: the item id to find
    :return: the String type name of kart
    """
    f = open(str(dir_path) + r"/metadata/json/kart.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException


def get_pet_info(item_id):
    """
    A function that gets pet name information from item id
    :param item_id: the item id to find
    :return: the String type name of pet
    """
    f = open(str(dir_path) + r"/metadata/json/pet.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException


def get_track_info(item_id):
    """
    A function that gets track name information from item id
    :param item_id: the item id to find
    :return: the String type name of track
    """
    f = open(str(dir_path) + r"/metadata/json/track.json", encoding="utf-8")
    data = json.load(f)
    try:
        for i in data:
            if i['id'] == item_id:
                name = i['name']
                return name
    except KeyError:
        raise idNotFoundException

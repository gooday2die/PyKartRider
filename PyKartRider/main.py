import requests

# Press the green button in the gutter to run the script.
import jsonInfo
import matchInfo
import userInfo

if __name__ == '__main__':
    a = userInfo.get_user_id("o양파극혐o")
    matchInfo.get_all_matches('')
    print(jsonInfo.get_character_info("95de437771bb1e094b4f3ef1c1a81574093a01e8d3be037c5a9fe0834dfbffa0"))
    print(jsonInfo.get_flying_pet_info("d4c819cc50543843245e73263d62e76d8283351264e45e5baba6c176efe45b00"))
    print(jsonInfo.get_kart_info("30711352d5c6279e96a5f449e613c5f9f04889f1c3ca6049e600d2b867821af7"))
    print(jsonInfo.get_track_info("5873d5fe128549b597e984c87881e7d0ab632e381073164fe513e902f48a3ccd"))
    print(jsonInfo.get_game_type_info("effd66758144a29868663aa50e85d3d95c5bc0147d7fdb9802691c2087f3416e"))
    print(matchInfo.get_all_matches('1728506595'))
    print(matchInfo.get_all_matches('1728506595')['matches'][0])
    print(matchInfo.get_all_matches('1728506595')['matches'][0]['matches'][0])
    print(len(matchInfo.get_all_matches('1728506595')['matches'][0]['matches'][0]))
    print(matchInfo.Match(matchInfo.get_all_matches('1728506595')['matches'][0]['matches'][0]))


    #matchInfo.Match(matchInfo.get_all_matches('1728506595')[0])

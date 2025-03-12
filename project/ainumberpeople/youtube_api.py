
import requests
import os
import pprint
import time
import gemini_api
import sound_api
from dotenv import load_dotenv

load_dotenv()

def get_chat_id(api_key, live_id):
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {"key": api_key, "part": "liveStreamingDetails", "id": live_id}
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        json = res.json()
        return json["items"][0]["liveStreamingDetails"].get("activeLiveChatId")
    except (requests.exceptions.RequestException, KeyError, IndexError) as e:
        pprint.pprint(f"チャットID取得エラー: {e}")
        return None

def get_latest_comment(api_key, chat_id, page_token=None):
    url = "https://www.googleapis.com/youtube/v3/liveChat/messages"
    params = {"key": api_key, "part": "snippet", "liveChatId": chat_id, "maxResults": 2}
    if page_token:
        params["pageToken"] = page_token
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
        resource = res.json()
        comments = [item["snippet"]["textMessageDetails"]["messageText"] for item in resource.get("items", [])]
        return comments[-1] if comments else None, resource.get("nextPageToken")
    except requests.exceptions.RequestException as e:
        pprint.pprint(f"コメント取得エラー: {e}")
        return None, None

def main():
    api_key = os.getenv('YOUTUBE_API_KEY')
    live_id = "QfUlYtbZPkY"
    chat_id = get_chat_id(api_key, live_id)
    if not chat_id:
        pprint.pprint("チャットIDを取得できませんでした。")
        return
    pprint.pprint(f"チャットID: {chat_id}")
    page_token = None
    while True:
        comment, page_token = get_latest_comment(api_key, chat_id, page_token)
        if comment:
            reply = gemini_api.getReply(comment)
            sound_api.play_reply(comment, reply)
            pprint.pprint(f"新しいコメント: {comment}")
        time.sleep(10)

if __name__ == "__main__":
    main()


# https://www.youtube.com/live/fP1AkPHrqU0
#{'id': 'fP1AkPHrqU0',
#  'key': 'AIzaSyDdV6J0WXO-F3pR_IGPJR4-CgKTT5ce3Dg',
#  'part': 'liveStreamingDetails'}
# {'etag': 'VjIwaVIv8qfaKSPgRYsd2FnMABw',
#  'items': [{'etag': 'f0qWVWPL3txlP2MqiwZKqh6-qhU',
#             'id': 'fP1AkPHrqU0',
#             'kind': 'youtube#video',
#             'liveStreamingDetails': {'activeLiveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                                      'actualStartTime': '2025-03-11T06:07:49Z',
#                                      'concurrentViewers': '1',
#                                      'scheduledStartTime': '2025-03-11T06:07:02Z'}}],
#  'kind': 'youtube#videoListResponse',
#  'pageInfo': {'resultsPerPage': 1, 'totalResults': 1}}



# https://www.googleapis.com/youtube/v3/liveChat/messages

#     {'id': 'fP1AkPHrqU0',
#  'key': 'AIzaSyDdV6J0WXO-F3pR_IGPJR4-CgKTT5ce3Dg',
#  'part': 'liveStreamingDetails'}
# {'etag': 'VjIwaVIv8qfaKSPgRYsd2FnMABw',
#  'items': [{'etag': 'f0qWVWPL3txlP2MqiwZKqh6-qhU',
#             'id': 'fP1AkPHrqU0',
#             'kind': 'youtube#video',
#             'liveStreamingDetails': {'activeLiveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                                      'actualStartTime': '2025-03-11T06:07:49Z',
#                                      'concurrentViewers': '1',
#                                      'scheduledStartTime': '2025-03-11T06:07:02Z'}}],
#  'kind': 'youtube#videoListResponse',
#  'pageInfo': {'resultsPerPage': 1, 'totalResults': 1}}
# チャットID: Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA
# {'etag': 'x2MO4Nz7Z53fZ-zcYrj4pn_ZVXI',
#  'items': [{'etag': 'Jbp1SCfteKu1W0PV0bGgciIVXsc',
#             'id': 'LCC.EhwKGkNKel85cG12Z1l3REZjalR3Z1FkSTlzT3ln',
#             'kind': 'youtube#liveChatMessage',
#             'snippet': {'authorChannelId': 'UCJBX5HSan1AYqRWhjHd7wEw',
#                         'displayMessage': 'こんにちは',
#                         'hasDisplayContent': True,
#                         'liveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                         'publishedAt': '2025-03-11T06:10:48.988481+00:00',
#                         'textMessageDetails': {'messageText': 'こんにちは'},
#                         'type': 'textMessageEvent'}},
#            {'etag': 'Qq3A0K6rELHVieI0B3F3hcAbMUM',
#             'id': 'LCC.EhwKGkNJU2JzWnl2Z1l3REZjVER3Z1FkeEtNUzNn',
#             'kind': 'youtube#liveChatMessage',
#             'snippet': {'authorChannelId': 'UCJBX5HSan1AYqRWhjHd7wEw',
#                         'displayMessage': '綺麗',
#                         'hasDisplayContent': True,
#                         'liveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                         'publishedAt': '2025-03-11T06:10:54.135284+00:00',
#                         'textMessageDetails': {'messageText': '綺麗'},
#                         'type': 'textMessageEvent'}},
#            {'etag': 'wWt0SJxwT2dBXaPNIrB9LqjpDwM',
#             'id': 'LCC.EhwKGkNKTEwtSi12Z1l3REZTRVNyUVlkS2o4RFdR',
#             'kind': 'youtube#liveChatMessage',
#             'snippet': {'authorChannelId': 'UCJBX5HSan1AYqRWhjHd7wEw',
#                         'displayMessage': '今日\u3000天気がいいね',
#                         'hasDisplayContent': True,
#                         'liveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                         'publishedAt': '2025-03-11T06:11:01.596217+00:00',
#                         'textMessageDetails': {'messageText': '今日\u3000天気がいいね'},
#                         'type': 'textMessageEvent'}},
#            {'etag': 'yps2OXnaUGSJIZQd0ANxBCDsuFY',
#             'id': 'LCC.EhwKGkNQSzMxcVd2Z1l3REZVYkh3Z1FkMndBNGVR',
#             'kind': 'youtube#liveChatMessage',
#             'snippet': {'authorChannelId': 'UCJBX5HSan1AYqRWhjHd7wEw',
#                         'displayMessage': 'どこ',
#                         'hasDisplayContent': True,
#                         'liveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                         'publishedAt': '2025-03-11T06:11:13.618342+00:00',
#                         'textMessageDetails': {'messageText': 'どこ'},
#                         'type': 'textMessageEvent'}},
#            {'etag': 'JW7cQDODuArGjB-R8rwgxkqjraU',
#             'id': 'LCC.EhwKGkNPNzFvcTJ2Z1l3REZjWEx3Z1FkcFdjb2tB',
#             'kind': 'youtube#liveChatMessage',
#             'snippet': {'authorChannelId': 'UCJBX5HSan1AYqRWhjHd7wEw',
#                         'displayMessage': '今、何歳ですか',
#                         'hasDisplayContent': True,
#                         'liveChatId': 'Cg0KC2ZQMUFrUEhycVUwKicKGFVDSkJYNUhTYW4xQVlxUldoakhkN3dFdxILZlAxQWtQSHJxVTA',
#                         'publishedAt': '2025-03-11T06:11:29.551676+00:00',
#                         'textMessageDetails': {'messageText': '今、何歳ですか'},
#                         'type': 'textMessageEvent'}}],
#  'kind': 'youtube#liveChatMessageListResponse',
#  'nextPageToken': 'GLyio62vgYwDIKv32-CzgYwD',
#  'pageInfo': {'resultsPerPage': 5, 'totalResults': 5},
#  'pollingIntervalMillis': 2009}
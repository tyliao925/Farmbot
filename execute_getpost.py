
from auth import get_headers, get_token_encoded, get_token_unencoded
import requests
import json
from datetime import datetime, timedelta


token_unencoded = get_token_unencoded()
iss = token_unencoded['iss']
token_encoded = get_token_encoded()

def get_events():
    url = f'https:{iss}/api/farm_events'
    headers = {'Authorization': 'Bearer ' + token_encoded,
               'content-type': 'application/json'}
    response = requests.get(url, headers=get_headers())
    print(json.dumps(response.json(), indent=2))
    return response.json()

def post_events(data):
    url = f'https:{iss}/api/farm_events'
    headers = {'Authorization': 'Bearer ' + token_encoded,
               'content-type': 'application/json'}
    response = requests.post(url, headers=get_headers(), data=json.dumps(data))
    print(json.dumps(response.json(), indent=2))
    if response.status_code == 201:
        print("Farm event created successfully!")
        print("Response data:", response.json())
    else:
        print("Failed to create farm event.")
        print("Status code:", response.status_code)
        print("Response:", response.text)

def get_sequence():
    url = f'https:{iss}/api/sequences'
    headers = {'Authorization': 'Bearer ' + token_encoded,
               'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    print(json.dumps(response.json(), indent=2))
    return response.json()
#{
#     "id": 212602,
#     "created_at": "2024-07-14T23:05:00.133Z",
#     "updated_at": "2024-07-14T23:05:00.228Z",
#     "args": {
#       "version": 20180209,
#       "locals": {
#         "kind": "scope_declaration",
#         "args": {},
#         "body": [
#           {
#             "kind": "variable_declaration",
#             "args": {
#               "label": "Location 1",
#               "data_value": {
#                 "kind": "coordinate",
#                 "args": {
#                   "x": 300,
#                   "y": 200,
#                   "z": 0
#                 }
#               }
#             }
#           }
#         ]
#       }
#     },
#     "color": "gray",
#     "folder_id": null,
#     "forked": false,
#     "name": "New Sequence 16",
#     "pinned": false,
#     "copyright": null,
#     "description": null,
#     "sequence_versions": [],
#     "sequence_version_id": null,
#     "kind": "sequence",
#     "body": [
#       {
#         "kind": "move",
#         "args": {},
#         "body": [
#           {
#             "kind": "axis_overwrite",
#             "args": {
#               "axis": "x",
#               "axis_operand": {
#                 "kind": "identifier",
#                 "args": {
#                   "label": "Location 1"
#                 }
#               }
#             }
#           },
#           {
#             "kind": "axis_overwrite",
#             "args": {
#               "axis": "y",
#               "axis_operand": {
#                 "kind": "identifier",
#                 "args": {
#                   "label": "Location 1"
#                 }
#               }
#             }
#           },
#           {
#             "kind": "axis_overwrite",
#             "args": {
#               "axis": "z",
#               "axis_operand": {
#                 "kind": "identifier",
#                 "args": {
#                   "label": "Location 1"
#                 }
#               }
#             }
#           }
#         ]
#       }
#     ]
#   },


# current_time = datetime.now()
# start_time = (current_time + timedelta(minutes=5)).isoformat()
# end_time = (current_time + timedelta(minutes=1)).isoformat()
#
# data = {
#     "start time": start_time,
#     "end time": end_time,
#     "repeat": 1,
#     "time_unit": "never",
#     "executable_id": 212602,
#     "executable_type": "Sequence",
# }
#
# post_events(data)

def get_device():
    url = f'https:{iss}/api/device'
    headers = {'Authorization': 'Bearer ' + token_encoded,
               'content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    print(json.dumps(response.json(), indent=2))
    return response.json()['id']
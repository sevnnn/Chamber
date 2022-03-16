from auth import Auth # I have yeeted this from Valorant App Developers Discord, full credit goes to NichyX#2390 (ID: 213584350812438528)
import requests
import json

# EDIT THIS BEFORE RUNNING THE CODE
mention_for = [""]
mention_who = ""
login = ""
password = ""
webhook = ""
# EDIT THIS BEFORE RUNNING THE CODE

data = Auth({"username": login, "password": password}).authenticate()

prices_dict = {}
r = requests.get("https://pd.eu.a.pvp.net/store/v1/offers/", headers=data[1])
for offer in r.json()['Offers']:
    prices_dict[offer['OfferID']] = offer["Cost"]['85ad13f7-3d1b-5128-9eb2-7cd8ee0b5741']

names_dict = {}
images_dict = {}
r = requests.get("https://valorant-api.com/v1/weapons/skins")
for skin in r.json()["data"]:
    names_dict[skin["levels"][0]["uuid"]] = skin["displayName"]
    images_dict[skin["levels"][0]["uuid"]] = skin["displayIcon"]

offers = []
mention = False
r = requests.get(f"https://pd.eu.a.pvp.net/store/v2/storefront/{data[0]}", headers=data[1])
for o in r.json()["SkinsPanelLayout"]["SingleItemOffers"]:
    if o in mention_for:
        mention = True
    offers.append(o)

payload = {"content": None, "embeds":[]}
for e in offers:
    elem = {"title": names_dict[e], "description": f"{prices_dict[e]} VP", "image": {"url": images_dict[e]}}
    payload["embeds"].append(elem)
if mention:
    payload["content"] = mention_who
headers = {"Content-Type": "application/json"}

r = requests.post(webhook, data=json.dumps(payload), headers=headers)
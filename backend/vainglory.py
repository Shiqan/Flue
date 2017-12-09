import os
import json
import falcon
from .vgapi import VaingloryApi

api_key = os.environ.get('API_KEY', None)
api = VaingloryApi(api_key)

class Players(object):

    def on_get(self, req, resp, name, region):
        player = api.players([name], region)

        resp.body = json.dumps(player, ensure_ascii=False)
        resp.status = falcon.HTTP_200

class Matches(object):

    def on_get(self, req, resp, name, region):
        matches = api.matches(region, player=[name])
        resp.body = json.dumps(matches, ensure_ascii=False)
        resp.status = falcon.HTTP_200

import msgpack
import falcon
import os

from vgapi import VaingloryApi

api_key = os.environ.get('API_KEY', None)
api = VaingloryApi(api_key)

class Players(object):

    def on_get(self, req, resp, name, region):
        player = api.players([name], region)

        resp.data = msgpack.packb(player, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200

class Matches(object):

    def on_get(self, req, resp, name, region):
        player = api.matches(region, player=[name])

        resp.data = msgpack.packb(player, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200

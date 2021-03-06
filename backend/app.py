import os
import falcon
from waitress import serve
from falcon_cors import CORS

from .vainglory import Players, Matches

port = int(os.environ.get('PORT', 8081))
cors = CORS(allow_all_origins=True)
api = application = falcon.API(middleware=[cors.middleware])

players = Players()
matches = Matches()
api.add_route('/api/player/{region}/{name}', players)
api.add_route('/api/matches/{region}/{name}', matches)

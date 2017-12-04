import os
import falcon
from waitress import serve
from falcon_cors import CORS

from vainglory import Players, Matches

cors = CORS(allow_all_origins=True, allow_origins_list=['http://localhost.com:8081'])


api = application = falcon.API(middleware=[cors.middleware])

players = Players()
matches = Matches()
api.add_route('/api/player/{region}/{name}', players)
api.add_route('/api/matches/{region}/{name}', matches)

port = int(os.environ.get('PORT', 33507))
serve(api, host='0.0.0.0', port=port)

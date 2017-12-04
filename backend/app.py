import os
import falcon
from waitress import serve
from falcon_cors import CORS

from vainglory import Players, Matches

port = int(os.environ.get('PORT', 8081))
cors = CORS(allow_all_origins=True, allow_origins_list=['http://localhost.com:{port}'.format(port=port)])
api = application = falcon.API(middleware=[cors.middleware])

players = Players()
matches = Matches()
api.add_route('/api/player/{region}/{name}', players)
api.add_route('/api/matches/{region}/{name}', matches)

if __name__ == "__main__":
    serve(api, port=port)

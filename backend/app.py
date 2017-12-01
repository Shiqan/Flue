import falcon
from waitress import serve

from vainglory import Players, Matches

api = application = falcon.API()

players = Players()
matches = Matches()
api.add_route('/api/player/{region}/{name}', players)
api.add_route('/api/matches/{region}/{name}', matches)

serve(api, host='0.0.0.0', port=8080)

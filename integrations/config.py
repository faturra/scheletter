from .logic_config import get_user_server_address, get_user_npsn, get_user_token

server_address = get_user_server_address
npsn = get_user_npsn
api_token = get_user_token
base_url = 'https://' + server_address + '/WebService/'
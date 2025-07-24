import json
from datetime import datetime
from user_agents import parse as ua_parse

LOG_FILE = 'user_logs.json'

def log_user_info(request):
    ip = request.remote_addr
    ua = ua_parse(request.headers.get('User-Agent', ''))

    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'ip': ip,
        'device': ua.device.family,
        'os': ua.os.family,
        'browser': ua.browser.family
    }

    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

def read_logs():
    try:
        with open(LOG_FILE, 'r') as f:
            return [json.loads(line) for line in f.readlines()]
    except FileNotFoundError:
        return []

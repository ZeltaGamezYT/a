# main.py on your T‑Deck

import network
from MicroWebSrv2 import *
import urequests

# -- Wi-Fi setup (change SSID/PASSWORD) --
def do_connect(ssid, pwd):
    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        sta.active(True)
        sta.connect(ssid, pwd)
        while not sta.isconnected():
            pass
    print('Network config:', sta.ifconfig())

do_connect('YOUR_SSID', 'YOUR_PASS')

# -- Set up web server --
mws = MicroWebSrv2()

# Navigation history state
history = {'back': [], 'forward': [], 'current': ''}

@mws.route('/', methods=['GET'])
def index_route(mwsrv, req):
    html = """<!DOCTYPE html><html><body>
    <input id="url" placeholder="Enter URL" style="width:60%"/>
    <button onclick="nav('go')">Go</button>
    <button onclick="nav('back')">Back</button>
    <button onclick="nav('forward')">Forward</button>
    <button onclick="nav('reload')">Reload</button>
    <div id="view" style="width:100%; height:80vh; overflow:auto; border:1px solid #444;"></div>
    <script>
      function nav(cmd) {
        const url = document.getElementById('url').value;
        fetch(`/nav?cmd=${cmd}&url=${encodeURIComponent(url)}`)
          .then(r => r.text()).then(html => {
            document.getElementById('view').innerHTML = html;
          });
      }
    </script>
    </body></html>"""
    req.Response.ReturnOk(html, contentType="text/html")

@mws.route('/nav')
def nav_handler(mwsrv, req):
    params = req.GetQueryParams()
    cmd = params.get('cmd')
    url = params.get('url')
    global history

    if cmd == 'go' and url:
        history['back'].append(history['current'])
        history['current'] = url
        history['forward'].clear()
    elif cmd == 'back' and history['back']:
        history['forward'].append(history['current'])
        history['current'] = history['back'].pop()
    elif cmd == 'forward' and history['forward']:
        history['back'].append(history['current'])
        history['current'] = history['forward'].pop()
    # 'reload' keeps current URL

    # Fetch fully rendered content from Headless‑Render‑API
    api_url = f"https://service.headless-render-api.com/{history['current']}"
    try:
        resp = urequests.get(api_url, headers={"X-Prerender-Token": "YOUR_TOKEN_HERE"})
        html = resp.text
    except Exception as e:
        html = f"<h3>Error loading page:</h3><pre>{e}</pre>"

    req.Response.ReturnOk(html, contentType="text/html")

# Start the server
mws.StartManaged()

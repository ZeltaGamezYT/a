# main.py – T‑Deck Mini Browser (Tulip CC)

import tulip
import tuliprequests
import cryptolib as cl
# — Wi‑Fi Connection —
tulip.wifi("WildflowerHaus", "wannagetaway")

api_key_aes256 = E0100869D8B156D0DAC19EA334DD2F348139441DE520184B7CACF2674C618CD448E638A5A330B49371968B5E7E2D028E82E15A48ADA95C96D9DB44B946530CB1683C2A69A62657BFCC2E27362DD2B3823AC6F52983F44AA41199221ED770A18665A009DEC0E961AF40665663DD054958E3910C5E1F1DE023F03B847D9A4CD302889106C67F9125D16B2A2116B32D7C23C9DAD4B4691839B01C2489E8B8A137B595390A83B2A796501EA1331BA7106960
cl.aes.__init__(input("What is the decryption key?>"),2)
api_key = ""
cl.aes.decrypt(api_key_aes256,api_key)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + api_key,
}
while prompt != "quit":
    prompt = input("You:")
    if prompt == "quit":
        break
    json_data = {
        'model': 'gpt-5',
        'input': prompt,
    }
    
    response = tr.post('https://api.openai.com/v1/responses', headers=headers, json=json_data)
    print("ChatGPT: " + response)
    
    
print("conversation ended")
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{\n    "model": "gpt-5",\n    "input": "Write a short bedtime story about a unicorn."\n  }'
#response = requests.post('https://api.openai.com/v1/responses', headers=headers, data=data)

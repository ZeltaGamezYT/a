# main.py – T‑Deck Mini Browser (Tulip CC)

import tulip
import tuliprequests

# — Wi‑Fi Connection —
tulip.wifi("WildflowerHaus", "wannagetaway")

# — Navigation State —
history = {'back': [], 'forward': [], 'current': ''}

# — Draw the UI Frame (URL bar and instructions) —
def draw_ui():
    tulip.bg_png("bg.png", 0, 0)  # optional background image
    tulip.sprite_move(0, 0, 0)  # optional sprite control
    tulip.text("URL: " + history['current'], 0, 0, 1)
    tulip.text("[<] Back  [>] Forward  [R] Reload  [G] Go", 0, 12, 1)

# — Fetch & Show Page —
def load_page():
    if not history['current']:
        return
    try:
        resp = tuliprequests.get("https://my-renderer.com/render?url=" + history['current'])
        html = resp.text
        tulip.text(html[:500], 0, 24, 1, wrap=True)
    except Exception as e:
        tulip.text("Error: " + str(e), 0, 24, 1)

# — Main Event Loop —
def run_browser():
    draw_ui()
    while True:
        touch = tulip.touch()
        if not touch:
            continue
        x, y = touch
        if 0 <= x < 50 and 12 <= y < 24 and history['back']:
            history['forward'].append(history['current'])
            history['current'] = history['back'].pop()
            load_page()
        elif 60 <= x < 110 and 12 <= y < 24 and history['forward']:
            history['back'].append(history['current'])
            history['current'] = history['forward'].pop()
            load_page()
        elif 120 <= x < 160 and 12 <= y < 24:
            load_page()
        elif 170 <= x < 210 and 12 <= y < 24:
            # Prompt for URL entry
            new_url = tulip.input("Enter URL:")
            if new_url:
                history['back'].append(history['current'])
                history['current'] = new_url
                history['forward'].clear()
                load_page()
        draw_ui()

if __name__ == "__main__":
    run_browser()

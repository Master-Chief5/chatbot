# 🟡 The Backrooms — First-Person Game

A fully in-browser, **first-person 3D Backrooms** survival game. Walk the endless
mono-yellow rooms with WASD or touch, collect **Almond Water**, keep your sanity,
avoid the thing in the halls, and spend what you collect on **permanent upgrades**.

- 🎮 **Play file:** [`index.html`](index.html) — pure WebGL (Three.js), **no install, no API key**.
- 📱 **Works on mobile** — on-screen joystick + look/run/torch buttons.
- 💾 **Upgrades persist** in your browser (localStorage), so you keep them between runs.

> There's also a chat-driven **text-adventure** version in [`streamlit_app.py`](streamlit_app.py)
> (the original AI game-master mode, needs an OpenAI key).

## Controls

| | Move | Look | Sprint | Drink Almond Water | Flashlight | Upgrades |
|---|---|---|---|---|---|---|
| **Desktop** | WASD / arrows | mouse (click to lock) | Shift | E | F | Esc |
| **Mobile** | left thumb stick | right side drag | RUN button | on-screen prompt | TORCH button | ☰ MENU |

## Upgrades (spend Almond Water 🥛)

Fleet Feet (speed) · Deep Lungs (stamina) · Marathoner (sprint efficiency) ·
Steady Mind (sanity) · Pure Almond (restore) · Flashlight · Sixth Sense (bottle glow).

## Play it

### Easiest — just open the file
Download `index.html` and open it in any modern browser. Needs internet the first
time to load Three.js from a CDN.

### Get a shareable mobile link (free)

**GitHub Pages:** repo → Settings → Pages → deploy from this branch → your game is at
`https://<user>.github.io/<repo>/`.

**Or any static host** (Vercel / Netlify / Cloudflare Pages): point it at this repo;
`index.html` is the entry point. No build step.

## Run the text-adventure version

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Extending it

The game is one self-contained file with clearly separated sections (save/progression,
world generation, textures, renderer, pickups, entity, player, input, game loop, HUD,
audio). See [`PROMPT.md`](PROMPT.md) for a ready-to-paste prompt to request new features.

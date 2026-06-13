# 🟡 The Backrooms — a text-adventure horror game

You've no-clipped out of reality into the Backrooms: an endless maze of damp,
mono-yellow rooms lit by buzzing fluorescent lights. An AI game master narrates
your descent and reacts to whatever you type. Stay quiet, manage your **sanity**
and **health**, find **Almond Water**, and look for a way out.

Built on [Streamlit](https://streamlit.io) with OpenAI as the game master.

### Features

- Free-text actions — type anything ("listen", "hide under the desk", "run").
- Live **Level / Sanity / Health / Items** status panel.
- Atmospheric liminal-yellow styling.
- Permadeath with a "New descent" button to start over.

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

3. Paste your [OpenAI API key](https://platform.openai.com/account/api-keys) and
   begin your descent.

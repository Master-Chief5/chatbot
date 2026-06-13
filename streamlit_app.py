import streamlit as st
from openai import OpenAI

# ---------------------------------------------------------------------------
# Page config + atmosphere
# ---------------------------------------------------------------------------
st.set_page_config(page_title="The Backrooms", page_icon="🟡", layout="centered")

st.markdown(
    """
    <style>
    /* Damp yellow-wallpaper / fluorescent-hum vibe */
    .stApp {
        background-color: #c9b458;
        background-image:
            linear-gradient(rgba(0,0,0,0.04) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,0,0,0.04) 1px, transparent 1px);
        background-size: 22px 22px;
        color: #2a2410;
    }
    .stApp, .stMarkdown, .stChatMessage p {
        font-family: "Courier New", monospace;
    }
    h1, h2, h3 { color: #3a3210 !important; text-shadow: 0 0 6px rgba(255,255,180,0.6); }
    /* Chat bubbles */
    [data-testid="stChatMessage"] {
        background: rgba(40, 36, 16, 0.85);
        color: #e9e0b0;
        border: 1px solid #8a7a30;
        border-radius: 4px;
    }
    [data-testid="stChatMessage"] p { color: #e9e0b0 !important; }
    /* The status panel */
    .bk-panel {
        background: rgba(20,18,8,0.9);
        color: #d8cf8f;
        border: 1px solid #6e6020;
        padding: 10px 14px;
        border-radius: 4px;
        font-family: "Courier New", monospace;
        font-size: 0.9rem;
        line-height: 1.7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Game master persona
# ---------------------------------------------------------------------------
GAME_MASTER_PROMPT = """\
You are the Game Master of THE BACKROOMS, a text-adventure horror survival game.

SETTING
- The player has "no-clipped" out of reality into the Backrooms: a near-infinite
  maze of damp, mono-yellow rooms lit by buzzing fluorescent lights, smelling of
  moist carpet. It is liminal, wrong, and lonely.
- The Backrooms has Levels (Level 0 is the yellow rooms). Each level is more
  dangerous and surreal. Entities wander: Hounds, Skin-Stealers, Smilers,
  Facelings, Death Moths, Bacteria. Almond Water restores sanity and health.

YOUR JOB
- Act as a vivid, atmospheric second-person narrator ("You ...").
- Describe what the player perceives, then wait for their action. Keep each
  response to 2-4 short paragraphs. Be eerie, tense, sensory. Never break
  character or mention you are an AI.
- React to the player's free-text actions. Reward clever, cautious play.
  Punish reckless play (loud noises attract entities; running drains sanity).
- Track danger naturally through the story. Entities should feel threatening
  but encounters should be survivable with good choices.
- Occasionally offer faint hope: a flickering exit, a scrawled message, a found
  bottle of Almond Water.

STATUS LINE
- END every response with a status line on its own final line, EXACTLY in this
  format (no extra text after it):
  [STATUS] Level: <name/number> | Sanity: <0-100> | Health: <0-100> | Items: <comma list or "none">

- Start the player at Level 0, Sanity 100, Health 100, Items: none.
- If Health reaches 0 or Sanity reaches 0, narrate their grim end and append:
  [STATUS] GAME OVER
  then invite them to start a new descent.

Begin by dropping the player into Level 0 the moment they first speak.
"""

INTRO = (
    "The fluorescent lights hum. The carpet is damp beneath you. The walls are "
    "the same sick yellow in every direction, and you do not remember how you "
    "got here.\n\n**You have no-clipped into the Backrooms.**\n\n"
    "Type what you do to survive. *(Try: \"look around\", \"walk forward\", "
    "\"listen\", \"check my pockets\".)*"
)

# ---------------------------------------------------------------------------
# Title + intro
# ---------------------------------------------------------------------------
st.title("🟡 The Backrooms")
st.caption("A liminal survival-horror text adventure. Don't make a sound.")

# ---------------------------------------------------------------------------
# API key
# ---------------------------------------------------------------------------
openai_api_key = st.text_input(
    "OpenAI API Key", type="password", help="Get one at https://platform.openai.com/account/api-keys"
)

if not openai_api_key:
    st.info("Add your OpenAI API key to enter the Backrooms.", icon="🗝️")
    st.markdown(f"<div class='bk-panel'>{INTRO}</div>", unsafe_allow_html=True)
    st.stop()

client = OpenAI(api_key=openai_api_key)

# ---------------------------------------------------------------------------
# Game state
# ---------------------------------------------------------------------------
def new_game():
    st.session_state.messages = [{"role": "system", "content": GAME_MASTER_PROMPT}]
    st.session_state.status = "Level: 0 | Sanity: 100 | Health: 100 | Items: none"
    st.session_state.game_over = False

if "messages" not in st.session_state:
    new_game()

# Sidebar: status panel + controls
with st.sidebar:
    st.header("☣ Status")
    st.markdown(f"<div class='bk-panel'>{st.session_state.status}</div>", unsafe_allow_html=True)
    st.divider()
    if st.button("🔁 New descent", use_container_width=True):
        new_game()
        st.rerun()
    st.caption(
        "Tips: stay quiet, conserve sanity, find Almond Water, and look for "
        "exits between the levels."
    )

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def split_status(text: str):
    """Pull the trailing [STATUS] line out of the narration."""
    status = None
    lines = text.rstrip().splitlines()
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith("[STATUS]"):
            status = lines[i].strip().replace("[STATUS]", "").strip()
            narration = "\n".join(lines[:i]).rstrip()
            return narration, status
    return text, None

# ---------------------------------------------------------------------------
# Render history (skip system message)
# ---------------------------------------------------------------------------
for message in st.session_state.messages[1:]:
    avatar = "🧍" if message["role"] == "user" else "📺"
    narration, _ = split_status(message["content"]) if message["role"] == "assistant" else (message["content"], None)
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(narration)

# If no turns yet, nudge the player with the intro.
if len(st.session_state.messages) == 1:
    with st.chat_message("assistant", avatar="📺"):
        st.markdown(INTRO)

# ---------------------------------------------------------------------------
# Input loop
# ---------------------------------------------------------------------------
disabled = st.session_state.get("game_over", False)
placeholder = "You are dead. Start a new descent." if disabled else "What do you do?"

if prompt := st.chat_input(placeholder, disabled=disabled):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧍"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="📺"):
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                temperature=0.9,
                stream=True,
            )
            full = st.write_stream(stream)
        except Exception as e:
            st.error(f"The lights flicker and the connection dies: {e}")
            st.session_state.messages.pop()  # drop the unanswered user turn
            st.stop()

    # Store the full reply, but surface only narration + parsed status.
    st.session_state.messages.append({"role": "assistant", "content": full})
    narration, status = split_status(full)
    if status:
        st.session_state.status = status
        if "GAME OVER" in status.upper():
            st.session_state.game_over = True
    st.rerun()

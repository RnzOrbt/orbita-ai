import io
import wave
from pathlib import Path

from flask import Flask, request, Response
from piper import PiperVoice

try:
    from piper import SynthesisConfig
except Exception:
    SynthesisConfig = None

# Path to the downloaded voice model (not stored in this repo)
MODEL = str(Path.home() / "piper" / "en_GB-alan-medium.onnx")

# Tune these to change how the voice sounds
LENGTH_SCALE = 0.92   # below 1 = quicker and more energetic, above 1 = slower
NOISE_SCALE = 0.85    # higher = more varied, expressive tone
NOISE_W_SCALE = 1.0   # higher = more varied rhythm
VOLUME = 1.0

voice = PiperVoice.load(MODEL)

syn_config = None
if SynthesisConfig is not None:
    try:
        syn_config = SynthesisConfig(
            volume=VOLUME,
            length_scale=LENGTH_SCALE,
            noise_scale=NOISE_SCALE,
            noise_w_scale=NOISE_W_SCALE,
        )
    except TypeError:
        syn_config = None

app = Flask(__name__)


def make_wav(text):
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        if hasattr(voice, "synthesize_wav"):
            if syn_config is not None:
                voice.synthesize_wav(text, wf, syn_config=syn_config)
            else:
                voice.synthesize_wav(text, wf)
        else:
            voice.synthesize(text, wf)
    return buf.getvalue()


@app.route("/", methods=["GET", "POST"])
def speak():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        text = data.get("text", "")
    else:
        text = request.args.get("text", "")
    text = (text or "").strip()
    if not text:
        return Response("no text", status=400)
    return Response(make_wav(text), mimetype="audio/wav")


if __name__ == "__main__":
    # Bound to localhost only; nginx proxies /tts to it.
    app.run(host="127.0.0.1", port=5000, threaded=False)

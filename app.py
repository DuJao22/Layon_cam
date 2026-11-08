import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
import secrets, string

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="threading")

rooms = {}

def make_code():
    alphabet = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(6))

@app.get("/")
def index():
    return render_template("index.html")

@socketio.on("create_room")
def create_room():
    code = make_code()
    while code in rooms:
        code = make_code()
    rooms[code] = {"camera": None, "viewer": None}
    join_room(code)
    rooms[code]["camera"] = request.sid
    emit("room_created", {"code": code})

@socketio.on("join_room")
def on_join(data):
    code = str(data.get("code", "")).strip().upper()
    if code not in rooms:
        emit("join_error", {"message": "Código não encontrado. Crie uma nova sala na câmera."})
        return
    join_room(code)
    role = data.get("role")
    if role == "viewer":
        rooms[code]["viewer"] = request.sid
        emit("joined", {"role": "viewer"})
        camera_sid = rooms[code].get("camera")
        if camera_sid:
            emit("peer_ready", {"role": "viewer"}, to=camera_sid)
    elif role == "camera":
        rooms[code]["camera"] = request.sid
        emit("joined", {"role": "camera"})
        if rooms[code].get("viewer"):
            emit("peer_ready", {"role": "viewer"}, to=request.sid)
    else:
        emit("join_error", {"message": "Perfil inválido."})

@socketio.on("signal")
def relay_signal(data):
    code = str(data.get("code", "")).strip().upper()
    if code in rooms:
        emit("signal", data.get("payload"), room=code, include_self=False)

@socketio.on("remote_record")
def remote_record(data):
    code = str(data.get("code", "")).strip().upper()
    if code in rooms:
        emit("remote_record", {"action": data.get("action")}, room=code, include_self=False)

@socketio.on("disconnect")
def on_disconnect():
    for code, room in list(rooms.items()):
        if room.get("camera") == request.sid:
            room["camera"] = None
        if room.get("viewer") == request.sid:
            room["viewer"] = None
        if not room.get("camera") and not room.get("viewer"):
            rooms.pop(code, None)

if __name__ == "__main__":
    # Para teste na mesma rede. HTTPS é necessário para acesso à câmera/microfone
    # em outros dispositivos; veja README para túnel HTTPS ou hospedagem.
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)

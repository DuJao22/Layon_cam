# Repository Guidelines

## Project Structure & Module Organization

This repository is a small Flask and Socket.IO web application. `app.py` contains the server routes, in-memory room coordination, and signaling events. `templates/index.html` contains the user interface and browser-side WebRTC, recording, and Socket.IO logic. `static/manifest.json` and `static/sw.js` support PWA installation. `requirements.txt` pins the Python dependencies, and `README_INSTALACAO.txt` documents setup, HTTPS requirements, and usage. There is no separate test or asset directory currently.

## Build, Test, and Development Commands

Use Python 3.10 or newer and a virtual environment for local development:

```sh
python -m venv .venv
. .venv/bin/activate       # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python app.py
```

The server listens on `0.0.0.0:5000`; open it locally for basic checks. Camera and microphone access from other devices requires HTTPS, as described in `README_INSTALACAO.txt`. No build, lint, or automated test command is configured.

## Coding Style & Naming Conventions

Follow the existing Python style: four-space indentation, `snake_case` for functions and variables, and clear Socket.IO event names such as `create_room` and `peer_ready`. Keep browser code consistent with the existing HTML file’s JavaScript conventions and use descriptive DOM IDs. Keep dependencies explicit in `requirements.txt`; do not add generated environments or secrets to the repository.

## Testing Guidelines

There is no test framework or test suite yet. For changes, run `python app.py` and manually verify the affected flow in two browser sessions: room creation and joining, signaling/video, and remote recording where relevant. Check browser console errors and confirm the HTTPS behavior when testing camera or microphone access. If adding automated tests, place them in a dedicated `tests/` directory and document the command here.

## Commit & Pull Request Guidelines

Git history is not available in this checkout, so no repository-specific commit convention can be confirmed. Use short, imperative commit subjects (for example, `Handle viewer disconnects`). Pull requests should explain the user-visible change, list manual or automated verification performed, link related issues when applicable, and include screenshots for interface changes.

## Security & Configuration Tips

This is an MVP: rooms are held in memory, and the server currently allows cross-origin Socket.IO connections. Do not expose it publicly without authentication and suitable access controls. Keep `SECRET_KEY` and deployment configuration out of committed files; use HTTPS for camera access and review the security limitations in `README_INSTALACAO.txt` before deployment.

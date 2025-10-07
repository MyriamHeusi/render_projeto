from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html",
                           title="Projeto Sprint 5 — Myriam",
                           name="Myriam Martins Heusi da Silva",
                           tagline="Analista de Dados & BI | Flask + Render",
                           cta_label="Ver JSON da API",
                           cta_href="/api")

@app.get("/api")
def api():
    return jsonify({"ok": True, "msg": "Hello, Render!", "author": "Myriam"})

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

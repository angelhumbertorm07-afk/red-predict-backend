from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

partidos = [
    {
        "id": 1, "partido": "Canadá vs Sudáfrica", "local": "Canadá", "visitante": "Sudáfrica",
        "liga": "mundial", "fecha": "Dieciseisavos - 28 Jun", "hora": "13:00",
        "sede": "Estadio Los Ángeles", "proximamente": False, "fechaEstreno": None,
        "gana_local": 52, "empate": 27, "gana_visitante": 21,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","⚪","🔴"],
        "esValor": False, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 21}, {"marcador": "1 - 0", "probabilidad": 18}]
    },
    {
        "id": 2, "partido": "Brasil vs Japón", "local": "Brasil", "visitante": "Japón",
        "liga": "mundial", "fecha": "Dieciseisavos - 28 Jun", "hora": "11:00",
        "sede": "Estadio Houston", "proximamente": False, "fechaEstreno": None,
        "gana_local": 65, "empate": 20, "gana_visitante": 15,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","⚪","🟢"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 24}, {"marcador": "3 - 1", "probabilidad": 13}]
    },
    {
        "id": 3, "partido": "Alemania vs Paraguay", "local": "Alemania", "visitante": "Paraguay",
        "liga": "mundial", "fecha": "Dieciseisavos - 28 Jun", "hora": "14:30",
        "sede": "Estadio Boston", "proximamente": False, "fechaEstreno": None,
        "gana_local": 62, "empate": 22, "gana_visitante": 16,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🔴","🟢"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 22}, {"marcador": "3 - 0", "probabilidad": 15}]
    },
    {
        "id": 4, "partido": "Países Bajos vs Marruecos", "local": "Países Bajos", "visitante": "Marruecos",
        "liga": "mundial", "fecha": "Dieciseisavos - 28 Jun", "hora": "19:00",
        "sede": "Estadio Monterrey", "proximamente": False, "fechaEstreno": None,
        "gana_local": 54, "empate": 26, "gana_visitante": 20,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🟢","⚪"],
        "esValor": True, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 1", "probabilidad": 19}, {"marcador": "1 - 0", "probabilidad": 17}]
    },
    {
        "id": 5, "partido": "Costa de Marfil vs Noruega", "local": "Costa de Marfil", "visitante": "Noruega",
        "liga": "mundial", "fecha": "Dieciseisavos - 29 Jun", "hora": "11:00",
        "sede": "Estadio Dallas", "proximamente": False, "fechaEstreno": None,
        "gana_local": 40, "empate": 28, "gana_visitante": 32,
        "rachaLocal": ["🟢","⚪","🟢"], "rachaVisita": ["🟢","🟢","🟢"],
        "esValor": True, "confianzaIA": 3,
        "top_marcadores": [{"marcador": "1 - 1", "probabilidad": 20}, {"marcador": "1 - 2", "probabilidad": 15}]
    },
    {
        "id": 6, "partido": "Francia vs Suecia", "local": "Francia", "visitante": "Suecia",
        "liga": "mundial", "fecha": "Dieciseisavos - 29 Jun", "hora": "15:00",
        "sede": "Estadio Nueva York / Nueva Jersey", "proximamente": False, "fechaEstreno": None,
        "gana_local": 60, "empate": 24, "gana_visitante": 16,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🔴","🟢"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 22}, {"marcador": "2 - 1", "probabilidad": 16}]
    },
    {
        "id": 7, "partido": "México vs Ecuador", "local": "México", "visitante": "Ecuador",
        "liga": "mundial", "fecha": "Dieciseisavos - 29 Jun", "hora": "19:00",
        "sede": "Estadio Ciudad de México", "proximamente": False, "fechaEstreno": None,
        "gana_local": 55, "empate": 26, "gana_visitante": 19,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🔴","🟢"],
        "esValor": True, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 22}, {"marcador": "1 - 0", "probabilidad": 19}]
    },
    {
        "id": 8, "partido": "Inglaterra vs RD Congo", "local": "Inglaterra", "visitante": "RD Congo",
        "liga": "mundial", "fecha": "Dieciseisavos - 30 Jun", "hora": "10:00",
        "sede": "Estadio Atlanta", "proximamente": False, "fechaEstreno": None,
        "gana_local": 68, "empate": 20, "gana_visitante": 12,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","⚪","🔴"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "3 - 0", "probabilidad": 20}, {"marcador": "2 - 0", "probabilidad": 22}]
    },
    {
        "id": 9, "partido": "Bélgica vs Senegal", "local": "Bélgica", "visitante": "Senegal",
        "liga": "mundial", "fecha": "Dieciseisavos - 30 Jun", "hora": "14:00",
        "sede": "Estadio Seattle", "proximamente": False, "fechaEstreno": None,
        "gana_local": 52, "empate": 27, "gana_visitante": 21,
        "rachaLocal": ["⚪","⚪","🟢"], "rachaVisita": ["🔴","🟢","🟢"],
        "esValor": True, "confianzaIA": 3,
        "top_marcadores": [{"marcador": "1 - 0", "probabilidad": 19}, {"marcador": "2 - 1", "probabilidad": 15}]
    },
    {
        "id": 10, "partido": "Estados Unidos vs Bosnia y Herzegovina", "local": "EE. UU.", "visitante": "Bosnia y Herz.",
        "liga": "mundial", "fecha": "Dieciseisavos - 30 Jun", "hora": "18:00",
        "sede": "Estadio San Francisco", "proximamente": False, "fechaEstreno": None,
        "gana_local": 56, "empate": 25, "gana_visitante": 19,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","⚪","🔴"],
        "esValor": False, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 21}, {"marcador": "1 - 0", "probabilidad": 18}]
    },
    {
        "id": 11, "partido": "España vs Austria", "local": "España", "visitante": "Austria",
        "liga": "mundial", "fecha": "Dieciseisavos - 1 Jul", "hora": "13:00",
        "sede": "Estadio Los Ángeles", "proximamente": False, "fechaEstreno": None,
        "gana_local": 60, "empate": 24, "gana_visitante": 16,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🟢","⚪"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 23}, {"marcador": "2 - 1", "probabilidad": 15}]
    },
    {
        "id": 12, "partido": "Portugal vs Croacia", "local": "Portugal", "visitante": "Croacia",
        "liga": "mundial", "fecha": "Dieciseisavos - 1 Jul", "hora": "17:00",
        "sede": "Estadio Toronto", "proximamente": False, "fechaEstreno": None,
        "gana_local": 50, "empate": 27, "gana_visitante": 23,
        "rachaLocal": ["🟢","⚪","🟢"], "rachaVisita": ["🔴","🟢","🔴"],
        "esValor": True, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 1", "probabilidad": 18}, {"marcador": "1 - 0", "probabilidad": 17}]
    },
    {
        "id": 13, "partido": "Suiza vs Argelia", "local": "Suiza", "visitante": "Argelia",
        "liga": "mundial", "fecha": "Dieciseisavos - 1 Jul", "hora": "21:00",
        "sede": "Estadio Vancouver", "proximamente": False, "fechaEstreno": None,
        "gana_local": 50, "empate": 27, "gana_visitante": 23,
        "rachaLocal": ["🟢","🟢","⚪"], "rachaVisita": ["🟢","🟢","🟢"],
        "esValor": True, "confianzaIA": 3,
        "top_marcadores": [{"marcador": "1 - 1", "probabilidad": 20}, {"marcador": "2 - 1", "probabilidad": 15}]
    },
    {
        "id": 14, "partido": "Australia vs Egipto", "local": "Australia", "visitante": "Egipto",
        "liga": "mundial", "fecha": "Dieciseisavos - 2 Jul", "hora": "12:00",
        "sede": "Estadio Dallas", "proximamente": False, "fechaEstreno": None,
        "gana_local": 46, "empate": 28, "gana_visitante": 26,
        "rachaLocal": ["🟢","🟢","⚪"], "rachaVisita": ["🟢","⚪","🟢"],
        "esValor": True, "confianzaIA": 3,
        "top_marcadores": [{"marcador": "1 - 0", "probabilidad": 19}, {"marcador": "1 - 1", "probabilidad": 18}]
    },
    {
        "id": 15, "partido": "Argentina vs Cabo Verde", "local": "Argentina", "visitante": "Cabo Verde",
        "liga": "mundial", "fecha": "Dieciseisavos - 2 Jul", "hora": "16:00",
        "sede": "Estadio Miami", "proximamente": False, "fechaEstreno": None,
        "gana_local": 75, "empate": 16, "gana_visitante": 9,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","🟢","⚪"],
        "esValor": False, "confianzaIA": 5,
        "top_marcadores": [{"marcador": "3 - 0", "probabilidad": 22}, {"marcador": "2 - 0", "probabilidad": 20}]
    },
    {
        "id": 16, "partido": "Colombia vs Ghana", "local": "Colombia", "visitante": "Ghana",
        "liga": "mundial", "fecha": "Dieciseisavos - 2 Jul", "hora": "19:30",
        "sede": "Estadio Kansas City", "proximamente": False, "fechaEstreno": None,
        "gana_local": 52, "empate": 27, "gana_visitante": 21,
        "rachaLocal": ["🟢","🟢","🟢"], "rachaVisita": ["🟢","⚪","🔴"],
        "esValor": False, "confianzaIA": 4,
        "top_marcadores": [{"marcador": "2 - 0", "probabilidad": 21}, {"marcador": "1 - 0", "probabilidad": 18}]
    },
    {
        "id": 17, "partido": "Octavos de Final - Partido 1", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 5 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "5 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 18, "partido": "Octavos de Final - Partido 2", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 5 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "5 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 19, "partido": "Octavos de Final - Partido 3", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 6 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "6 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 20, "partido": "Octavos de Final - Partido 4", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 6 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "6 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 21, "partido": "Octavos de Final - Partido 5", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 7 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "7 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 22, "partido": "Octavos de Final - Partido 6", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 7 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "7 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 23, "partido": "Octavos de Final - Partido 7", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 8 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "8 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 24, "partido": "Octavos de Final - Partido 8", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Octavos - 8 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "8 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 25, "partido": "Cuartos de Final - Partido 1", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Cuartos - 11 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "11 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 26, "partido": "Cuartos de Final - Partido 2", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Cuartos - 11 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "11 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 27, "partido": "Cuartos de Final - Partido 3", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Cuartos - 12 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "12 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 28, "partido": "Cuartos de Final - Partido 4", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Cuartos - 12 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "12 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 29, "partido": "Semifinal - Partido 1", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Semifinal - 15 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "15 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 30, "partido": "Semifinal - Partido 2", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Semifinal - 16 Jul", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "16 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 31, "partido": "Tercer Lugar", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Tercer Lugar - 19 Jul", "hora": "Por definir",
        "sede": "Estadio Miami", "proximamente": True, "fechaEstreno": "19 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 32, "partido": "FINAL - Copa Mundial 2026", "local": "Por definir", "visitante": "Por definir",
        "liga": "mundial", "fecha": "Final - 19 Jul", "hora": "15:00",
        "sede": "Estadio Nueva York / Nueva Jersey", "proximamente": True, "fechaEstreno": "19 Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 33, "partido": "Liga MX - Jornada 1", "local": "Por definir", "visitante": "Por definir",
        "liga": "ligamx", "fecha": "Apertura 2026", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 34, "partido": "Liga MX - Jornada 2", "local": "Por definir", "visitante": "Por definir",
        "liga": "ligamx", "fecha": "Apertura 2026", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Jul 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 35, "partido": "Liga MX - Jornada 3", "local": "Por definir", "visitante": "Por definir",
        "liga": "ligamx", "fecha": "Apertura 2026", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Ago 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 36, "partido": "Liga MX - Jornada 4", "local": "Por definir", "visitante": "Por definir",
        "liga": "ligamx", "fecha": "Apertura 2026", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Ago 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 37, "partido": "Champions - Jornada 1", "local": "Por definir", "visitante": "Por definir",
        "liga": "champions", "fecha": "Fase de Grupos 2026/27", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Sep 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 38, "partido": "Champions - Jornada 2", "local": "Por definir", "visitante": "Por definir",
        "liga": "champions", "fecha": "Fase de Grupos 2026/27", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Oct 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 39, "partido": "Champions - Jornada 3", "local": "Por definir", "visitante": "Por definir",
        "liga": "champions", "fecha": "Fase de Grupos 2026/27", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Oct 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
    {
        "id": 40, "partido": "Champions - Jornada 4", "local": "Por definir", "visitante": "Por definir",
        "liga": "champions", "fecha": "Fase de Grupos 2026/27", "hora": "Por definir",
        "sede": "Por definir", "proximamente": True, "fechaEstreno": "Nov 2026",
        "gana_local": 0, "empate": 0, "gana_visitante": 0,
        "rachaLocal": [], "rachaVisita": [], "esValor": False, "confianzaIA": 0, "top_marcadores": []
    },
]

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/api/predicciones', methods=['GET'])
def get_predicciones():
    return jsonify(partidos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
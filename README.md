# Discord Bot + Flask API Webhook

Este proyecto combina un **bot de Discord** con un **servidor Flask**, permitiendo tanto escuchar mensajes en Discord como exponer una API para enviar mensajes a canales usando HTTP.

---

## 📽️ Demo en video

Mira una demostración rápida del funcionamiento del bot y la API:  
👉 https://youtu.be/2y8vZM5-_i0

---

## 🛠️ Tecnologías usadas

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/) – para interactuar con la API de Discord
- Flask – para exponer un API web (HTTP REST)

---

## 🚀 Funcionalidades

- Escucha mensajes en un canal de Discord.
- Responde automáticamente a mensajes como `"hola"`.
- Permite enviar mensajes a un canal vía una API POST (`/send_message`).

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd webhookDiscord
```

2. Crea un entorno virtual:

```bash
python3 -m venv ambiente
source ambiente/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Uso

1. Abre y configura tu archivo `app.py` con tu token de bot de Discord.

2. Corre el script:

```bash
python app.py
```

Verás en la consola:  
`Bot conectado como MyBotEscucha#1234`

3. En tu canal de Discord, escribe:

```
hola
```

Y el bot responderá:

```
¡Hola! Recibí tu mensaje.
```

4. Para enviar mensajes vía HTTP, haz un `POST` a:

```
http://localhost:5000/send_message
```

Con cuerpo JSON:

```json
{
  "channel_id": "TU_CHANNEL_ID",
  "content": "Hola desde Flask!"
}
```

---

## 📎 Recomendaciones

- No compartas tu token público (guárdalo en un `.env` si lo vas a subir a producción).
- Usa `ngrok` si necesitas exponer tu API Flask a servicios externos.
- Para ambientes reales, usa un servidor WSGI como Gunicorn.

---

## 🔐 Seguridad

Asegúrate de proteger tu endpoint `/send_message` si lo expones públicamente (por ejemplo, usando tokens o autenticación).

---

## 🧑‍💻 Autor

Creado por [TuNombre]  
Contacto: [TuCorreo o GitHub]

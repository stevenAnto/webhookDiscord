from flask import Flask, request
import discord
import threading
import asyncio

app = Flask(__name__)

# Configura intents para poder leer mensajes
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = "PON_TU_TOKEN_AQUI"

# Evento cuando el bot esté listo
@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

# Evento cuando se recibe un mensaje
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # 👇 Esta línea te muestra el mensaje recibido en la terminal
    print(f"[{message.channel}] {message.author}: {message.content}")
    if message.content.lower() == "hola":
        await message.channel.send("¡Hola! Recibí tu mensaje.")

# Endpoint simple para que Flask reciba POST y el bot envíe mensaje
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    channel_id = int(data.get('channel_id'))
    content = data.get('content')

    channel = client.get_channel(channel_id)
    if channel:
        # Usamos asyncio para enviar el mensaje de forma async
        asyncio.create_task(channel.send(content))
        return {"status": "Mensaje enviado"}
    else:
        return {"error": "Canal no encontrado"}, 404

# Función para correr Flask en un hilo separado
def run_flask():
    app.run(host="0.0.0.0", port=5000)

# Función para correr el bot de Discord
def run_discord_bot():
    asyncio.run(client.start(TOKEN))

if __name__ == "__main__":
    # Correr Flask en un hilo y el bot en el hilo principal
    threading.Thread(target=run_flask).start()
    run_discord_bot()
from flask import Flask
from threading import Thread

app=Flask('')

@app.route('/')

def main():
  return "Lub Dub"

def run():
  app.run(host="0.0.0.0", port=8080)

def heartbeat():
  server = Thread(target=run)
  server.start()
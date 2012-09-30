from flask import Flask, jsonify, request, abort
import logging, random
app = Flask(__name__)

@app.route("/evaluate")
def evaluate():
  text = request.args.get('text', '')
  if text:
    score = evaluate(text)
    return jsonify({'score': score, 'text': text})
  else:
    abort(400)

def evaluate(text):
  return random.randint(0,100)

if __name__ == "__main__":
  app.debug = True
  app.run()

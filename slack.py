from flask import Flask, jsonify, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/slack/slash', methods=['GET', 'POST'])
def slack_event():
  global state, context

  payload = request.values
  print(payload)

  if payload:
    text = payload.get('text')

    # While state is not EXIT, talk to the user.
    if state != 'END':
      state, data, output1 = on_input(state, text, context)

      # Enter the new state.
      output2 = on_enter_state(state, context)

      return jsonify({
        'response_type': 'in_channel',
        'text': '\n'.join([x for x in [output1, output2] if x is not None])
      })

  return ''

if __name__ == '__main__':
  app.run()

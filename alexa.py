from flask import Flask, jsonify, request
from bot import on_enter_state, on_input

app = Flask(__name__)

state = 'NO QUERY'
context = {}

@app.route('/alexa', methods=['POST', 'GET'])
def alexa():
  global state, context
  output = ''
  payload = request.get_json()
  print(payload)

  request_type = None
  if payload['request']:
    request_type = payload['request']['type']

  try:
    request_query = payload['request']['intent']['slots']['query']['value']
  except KeyError:
    request_query = ''

  # We are starting, so we should reset the state
  if request_type == 'LaunchRequest':
    state, context = 'NO QUERY', {}
    print('Launched, resetting state')

  elif request_type == 'IntentRequest':
    print(f'Processing {request_query} with ({state}, {context})')

    # Intents will have some input, so we need to process it
    # Change the conversation state based on the message from the user
    state, context, output1 = on_input(state, request_query, context)
    if output1:
      output += output1 + '\n'
    print(f'Result ({state}, {context})')

    # The special 'END' state here should reset the bot, so that the
    # next slash command is back at the start.
    if state == 'END':
      state, context = 'NO QUERY', {}
      return alexa_response("Thanks for the chat!", shouldEndSession=True)

  # Do something based on the state
  print(f'Starting on enter ({state}, {context})')
  output += on_enter_state(state, context)

  # Build our response
  print(f'Giving response {output}')
  return alexa_response(output)

def alexa_response(text, shouldEndSession=False):
  return jsonify({
    'version': '0.1',
    'response': {
      'outputSpeech': {
        'type': 'SSML',
        'ssml': f"""<speak><voice name="Russell">{text}</voice></speak>"""
      },
      'shouldEndSession': shouldEndSession
    }
  })

if __name__ == '__main__':
  app.run()

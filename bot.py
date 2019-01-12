from conversations import *


"""
Common states
"""

def no_query_on_enter_state(context):
  return 'How can I help?'

def no_query_on_input(text, context):
  # No data provided
  if text.lower().endswith('plant seeds'):
    return 'HOW TO PLANT', {}, None

  # Seed data provided
  elif text.lower().endswith('plant tomato seeds'):
    return 'HOW TO PLANT SEED', {'seed': 'tomato'}, None

  # If we don't know what they're talking about, go to no query
  else:
    return 'NO QUERY', {}, 'I don\'t know that command yet!\nOne day I will suggest some things you can do.' # todo


"""
Register states
"""

def on_enter_state(state, context):
  if state == 'NO QUERY':
    return no_query_on_enter_state(context)

  elif state == 'HOW TO PLANT':
    return snag.how_to_plant_on_enter_state(context)

  elif state == 'HOW TO PLANT SEED':
    return snag.how_to_plant_seed_on_enter_state(context)

  else:
    return 'END', {}, 'Bye!'

def on_input(state, text, context):
  # If they're trying to quit, then quit.
  if text == 'quit':
    return 'END', {}, 'Bye!'

  # Otherwise, do the state thing.
  if state == 'NO QUERY':
    return no_query_on_input(text, context)

  elif state == 'HOW TO PLANT':
    return snag.how_to_plant_on_input(text, context)

  elif state == 'HOW TO PLANT SEED':
    # End state: go back to no query
    return no_query_on_input(text, context)

  else:
    return 'END', {}, 'Bye!'

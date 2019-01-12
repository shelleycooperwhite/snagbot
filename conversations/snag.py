# How to plant
def how_to_plant_on_enter_state(data):
  return 'What are you planting?'

def how_to_plant_on_input(text, data):
  if text in SEED_TYPES:
    return 'HOW TO PLANT SEED', {'seed': text}, None

  # If we don't understand, let them know and try this state again.
  else:
    return 'HOW TO PLANT', {}, 'Hmm, I don\'t know about that type of seed.'


# How to plant
# + Seed type
def how_to_plant_seed_on_enter_state(data):
  seed = data['seed']
  return 'Here are the instructions for planting ' + seed + '! blah blah blah etc'

def how_to_plant_seed_on_input(data):
  return 'NO QUERY', {}, None

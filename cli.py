from bot import on_enter_state, on_input

state = 'NO QUERY'
context = None

while state != 'END':
  output = on_enter_state(state, context)
  if output:
    print(output)

  text = input('> ')
  state, context, output = on_input(state, text, context)
  if output:
    print(output)

def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"


  return shape



astericks = {'rows': 4, 'cols': 4, 'char': '*'}
zeros = {'rows': 3, 'cols': 9, 'char': '0'}
print(draw_shape(astericks))
print(draw_shape(zeros)) 
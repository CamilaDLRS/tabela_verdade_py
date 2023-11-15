import ttg;

table = ttg.Truths(['p', 'q'], ['p => q', '~p or q'], ints=False);
print(table);


while True:
  formula = input('Entre com a formula: ');
  formula = formula.lower;

  print('\formula = ', formula, '\n\n');
  resp = input();



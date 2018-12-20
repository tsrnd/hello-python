def capitalizeVowelsRegExp(input):
      substitutions = {
    'a' :  'A',
    'e' :  'E',
    'i' :  'I',
    'o' :  'O',
    'u' :  'U',
    'y' :  'Y',
  }
  for before, after in substitutions.items():
    print(substitutions.item)
    input =  input.replace(before, after)
  return input

from collections import OrderedDict
""" Ordered Dictionary rewrite """

glossary = OrderedDict()

glossary['PEP'] = 'This is a guide which tells python programmers,\
 how to style their python code the current standard is PEP 8'
glossary['list'] = 'Is a dynamic data structure in python'
glossary['tuples'] = 'Are Immutable data structure'
glossary['Dictionary'] = 'Is a dynamic data structure which stores\
            key-value pairs'

for key, values in glossary.items():
    print(key + ": " + values)

glossary = {
    'variable': 'Something that is a changable value',
    'float': 'A number with a decimal point',
    'tuples': 'A sort of list',
    'dictionary': 'A collection of key-value pairs'
}

# For key and value in sorted set of dictionary: print
for k, v in sorted(set(glossary.items())):
    print(f"A {k.title()} means: {v}.")

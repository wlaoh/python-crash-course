glossary = {
    'if statements': 'conditional statements, conditional expressions and conditional constructs are features of a programming language, which perform different computations or actions depending on whether a programmer-specified boolean condition evaluates to true or false.',
    'loops': 'A loop is a sequence of statements which is specified once but which may be carried out several times in succession.',
    'variable': 'a variable or scalar is a storage location (identified by a memory address) paired with an associated symbolic name (an identifier), which contains some known or unknown quantity of information referred to as a value.',
    'dictionary': 'an abstract data type composed of a collection of (key, value) pairs, such that each possible key appears at most once in the collection',
    'list': 'an abstract data type that represents a countable number of ordered values, where the same value may occur more than once',
}

for term, definition in glossary.items():
    print(term.title() + ': \n\t' + definition)
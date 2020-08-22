# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design untill none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been completed:")
for completed_model in completed_models:
    print(completed_model)

# Printing the now empty unprinted_designs list.
print(unprinted_designs)

# Now the same thing, but using functions.
print("\nAnd now the same thing, but using functions\n")

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design untill none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_models(completed_models):
    """ Display all completed models."""
    print("\nThe following models have been completed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Adding [:] to the unprinted_designs (below) makes it so that the list that
# is used is a copy of the original list, leaving that list intact.
print_models(unprinted_designs[:], completed_models)
show_models(completed_models)

# Print the unprinted_designs list to show that tis time it is still intact.
print(unprinted_designs)

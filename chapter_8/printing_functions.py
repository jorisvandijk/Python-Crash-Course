import printing_model_functions as pmf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Adding [:] to the unprinted_designs (below) makes it so that the list that
# is used is a copy of the original list, leaving that list intact.
pmf.print_models(unprinted_designs[:], completed_models)
pmf.show_models(completed_models)

# Print the unprinted_designs list to show that tis time it is still intact.
print(unprinted_designs)

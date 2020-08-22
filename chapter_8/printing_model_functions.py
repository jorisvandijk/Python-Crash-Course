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

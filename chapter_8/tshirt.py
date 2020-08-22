def make_shirt(size='large', text='I love Python!'):
    """Make a shirt."""
    print(f"You've made a {size} shirt, with the following text: "
            f"{text.upper()}.")

make_shirt('large', 'hello world')
make_shirt(size='small', text='smile!')
make_shirt()
make_shirt(size='small')
make_shirt(size='medium', text='spoon')

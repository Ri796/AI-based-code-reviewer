import ast

# Parse a more complex Python code snippet
code = """
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
"""

tree = ast.parse(code)
print(ast.dump(tree, indent=2))

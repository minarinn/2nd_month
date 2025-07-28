from blessed import Terminal

term = Terminal()

fruits = ["apple", "banana", "cherry", "grape", "mango", "orange", "peach"]
colors = [term.red, term.green, term.orange, term.deepskyblue3, term.mediumpurple, term.cyan3, term.blanchedalmond]

for fruit, color in zip(fruits, colors):
    print(color + fruit + term.normal)
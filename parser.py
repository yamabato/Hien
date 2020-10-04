from lark import Lark

with open("grammer.txt",mode="r") as f:
    rule = f.read()

program = """

i[int] <- f(1,12,a);

"""

parser = Lark(rule, start="program", parser="lalr")
tree = parser.parse(program)
print(tree.pretty())

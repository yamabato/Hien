from lark import Lark

with open("grammer.txt",mode="r") as f:
    rule = f.read()

program = """

loop 10{
};

"""

parser = Lark(rule, start="program", parser="lalr")
tree = parser.parse(program)

from lark import Lark

with open("grammer.txt",mode="r") as f:
    rule = f.read()

program = """

i[int] <- $counter;
loop 100{
    i[int] <- $counter + 1;

    switch {
        case i % 15 ==0 {
        }
        case i % 5 == 0 {
        }
        case i % 3 == 0 {
        }
        else{
        }
    };
};

"""

parser = Lark(rule, start="program", parser="lalr")
tree = parser.parse(program)
print(tree.pretty())
print(tree.children)

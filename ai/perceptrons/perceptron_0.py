x1 = Input()
x2 = Input()
node_3 = Percept([],)
node_4 = Percept([],)
node_5 = Percept([],)

node_3.set_inputs()
node_4.set_inputs()
node_5.set_inputs()

xor = node_5

for a in range(2):
    for b in range(2):
        x1.set_value(a)
        x2.set_value(b)
        print(a,b,xor.eval())

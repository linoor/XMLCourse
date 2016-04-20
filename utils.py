def generate(root_node, gen_fun, filename):
    with open(filename, 'w') as xml:
        xml.write("<{0}>".format(root_node))
        for i in range(10):
            xml.write(gen_fun())
        xml.write("</{0}>".format(root_node))
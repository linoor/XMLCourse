def generate(root_node, template, data, filename):
    with open(filename, 'w') as xml:
        xml.write("<{0}>".format(root_node))
        for i in range(10):
            xml.write(template.format(data))
            xml.write("</{0}>".format(root_node))
from random import randint

from faker import Factory

from utils import generate

fake = Factory.create('pl_PL')

if __name__ == '__main__':
    template = """
<appartement id="{id}">
    <address>{address}</address>
    <city>{city}</city>
    <area>{area}</area>
    <rooms>{rooms}</rooms>
    <year>{year}</year>
    <price>{price}</price>
</appartement>
"""

    root_node = 'appartement'
    generate(root_node, template, {
        'id': 1,
        'address': fake.address(),
        'city': fake.city(),
        'year': randint(1970, 2000),
        'rooms': randint(2, 10),
        'area': randint(40, 150),
        'price': randint(100000, 1000000)
    }, 'test.xml')

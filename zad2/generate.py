from random import randint

from faker import Factory

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
fake = Factory.create('pl_PL')

with open('appartements.xml', 'w') as xml:
    xml.write("<appartements>")
    for i in range(10):
        xml.write(template.format(id=i, address=fake.address(), city=fake.city(), year=randint(1970, 2000),
                                  rooms=randint(2, 10), area=randint(40, 150), price=randint(100000, 1000000)))
    xml.write("</appartements>")

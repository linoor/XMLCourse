from random import randint

from faker import Factory

from utils import generate

fake = Factory.create('pl_PL')

if __name__ == '__main__':
    template = """
    <samochod>
        <marka>{marka}</marka>
        <model>{model}</model>
        <rocznik>{rocznik}</rocznik>
        <num_kat>{num_kat}</num_kat>
        <cena>{cena}</cena>
    </samochod>
    """

    def gen_fun():
        return template.format(**{
            'marka': fake.text()[:10],
            'model': fake.text()[:10],
            'rocznik': randint(1970, 2000),
            'num_kat': randint(1000, 2000),
            'cena': randint(10000, 50000)
        })

    generate('cennik', gen_fun, 'ceny.xml')

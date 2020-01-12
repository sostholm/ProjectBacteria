from mongoengine import connect

from models import Microbe, Probiotic

connect('ProjectProbiotic', host='mongomock://mongo', alias='default')

def init_db():
    microbe = Microbe(name="Microbe")
    microbe.save()

    probiotic = Probiotic(name='Probiotic')
    probiotic.save()

    bl = Microbe(
        m_type      ='bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Lactis'
    )

    bl = Microbe(
        m_type      ='bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Breve'
    )

    bl = Microbe(
        m_type      ='bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Longum'
    )

    bl = Microbe(
        m_type      ='bacteria',
        species     ='Lactobacillus',
        subspecies  ='Acidophilus'
    )


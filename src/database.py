from mongoengine import connect

from models import Microbe, Probiotic

connect('ProjectProbiotic', host='mongomock://pine64', alias='default')

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

    bb = Microbe(
        m_type      ='bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Breve'
    )

    blong = Microbe(
        m_type      ='bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Longum'
    )
    
    ba = Microbe(
        m_type      ='bacteria',
        species     ='Lactobacillus',
        subspecies  ='Acidophilus'
    )

    bl.save()
    bb.save()
    blong.save()
    ba.save()

    pb = Microbe(
        name        ='MadeUp',
        microbes    = [bl, bb, blong, ba]
    )
    pb.save()

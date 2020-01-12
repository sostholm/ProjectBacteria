from mongoengine import connect

from models import Microbe, Probiotic

connect('ProjectProbiotic', host='mongodb://pine64:27017')

def init_db():
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

    pb = Probiotic(
        name        ='MadeUp',
        microbes    = [bl, bb, blong, ba]
    )
    pb.save()

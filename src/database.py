from mongoengine import connect
import os

from models import Microbe, Probiotic

connect('ProjectProbiotic', host=f'mongodb://{os.environ["mongo-db"]}:27017')

def init_db():
    bl = Microbe(
        domain      ='Bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Lactis'
    )

    bb = Microbe(
        domain      ='Bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Breve'
    )

    blong = Microbe(
        domain      ='Bacteria',
        species     ='Bifidobacterium',
        subspecies  ='Longum'
    )
    
    ba = Microbe(
        domain      ='Bacteria',
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

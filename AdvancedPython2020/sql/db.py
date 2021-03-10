from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, TIME
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///DINERS.db', echo=True)


#  canteen table
class Canteen(Base):
    __tablename__ = 'canteen'

    ID = Column(Integer, primary_key=True)
    ProviderID = Column(Integer, ForeignKey('provider.ID'))
    Name = Column(VARCHAR)
    Location = Column(VARCHAR)
    time_open = Column(TIME)
    time_closed = Column(TIME)
    relation = relationship("Provider", back_populates="canteen")


#  provider table
class Provider(Base):
    __tablename__ = 'provider'

    ID = Column(Integer, primary_key=True)
    ProviderName = Column(VARCHAR)


Provider.canteen = relationship("Canteen", order_by=Canteen.ID, back_populates="relation")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
try:
    c1 = Canteen(Name='bitStop KOHVIK', Location='Raja 4c', time_open="09:30", time_closed="16:00")

    session.add(c1)

    session.add_all([
        Canteen(Name='Economics- and social science building canteen', Location='Akadeemia tee 3', time_open='08:30',
                time_closed='18:30'),
        Canteen(Name='Libary canteen', Location='Akadeemia tee 1/Ehitajate tee 7', time_open='08:30',
                time_closed='19:00'),
        Canteen(Name='Main building Deli cafe', Location='Ehitajate tee 5 U01 building', time_open='09:00',
                time_closed='16:30'),
        Canteen(Name='Main building Daily lunch restaurant', Location='Ehitajate tee 5 U01 building', time_open='09:00',
                time_closed='16:30'),
        Canteen(Name='U06 building canteen', Location='U06 building', time_open='09:00', time_closed='16:00'),
        Canteen(Name='Natural Science building canteen', Location='Akadeemia tee 15 SCI building', time_open='09:00',
                time_closed='16:00'),
        Canteen(Name='ICT building canteen', Location='Raja 15/Mäepealse 1', time_open='09:00', time_closed='16:00'),
        Canteen(Name='Sports building canteen', Location='Männiliiva 7 S01 building', time_open='11:00',
                time_closed='20:00'),
        Provider(ProviderName='Bitstop Kohvik OÜ'),
        Provider(ProviderName='Rahva Toit'),
        Provider(ProviderName='Baltic Restaurants Estonia AS'),
        Provider(ProviderName='TTÜ Sport')

    ]
    )

    #  query for canteens which are open 16.15-18.00
    result = session.query(Canteen).filter(Canteen.time_closed > '18:00')
    #  query for canteens which are serviced by Rahva Toit
    result2 = session.query(Canteen).filter(Provider.ProviderName == 'Rahva Toit')
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

print()
for row in result:
    print("Canteens which are open 16.15-18.00 \n", "Canteen: ", row.Name, "\nLocation: ", row.Location,
          "\nTime open: ", row.time_open, "\nTime closed: ", row.time_closed)

for row in result2:
    print("Canteens which are serviced by Rahva Toit\n", "Provider: ", row.ProviderName, "\nCanteen: ", row.Name,
          "\nLocation: ", row.Location, "\nTime open: ", row.time_open, "\nTime closed: ", row.time_closed)

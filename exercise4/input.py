from model import  db, Puppy, Toys, Owner

tommy = Puppy('tommy', 'golden retriever')
jerry = Puppy('jerry', 'hufflepuff')

db.session.add_all([tommy, jerry])
db.session.commit()
print(Puppy.query.all())

owner1 = Owner('Pique', tommy.id)
toy1 = Toys('dd', tommy.id)
toy2 = Toys('Veg', tommy.id)

db.session.add_all([owner1, toy1, toy2])
db.session.commit()

print(Puppy.query.all())

tommy.report_toys()
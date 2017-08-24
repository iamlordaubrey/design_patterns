from observer import Subscriber, Publisher

pub = Publisher(['lunch', 'dinner'])

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register('lunch', bob)
pub.register('dinner', alice)
pub.register('lunch', john)
pub.register('dinner', john)

pub.dispatch("lunch", "It's lunch time")
pub.dispatch("dinner", "Dinner is served")

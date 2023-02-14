import random

R_EATING = 'I like eating eletric energy'

def unknown():
    response = ['Could you please re-phrase that', '...', 'Sounds about right',
                'What does that mean?'][random.randrange(4)]
    return response
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    all_python_dev = [worker["name"] for worker in DATA if worker ["language"] == "python"]
    print(all_python_dev)

    all_platzy_workers = [worker['name'] for worker in DATA if worker ['organization'] == 'Platzi']
    print(all_platzy_workers) 

    legal_age = [worker["name"] for worker in DATA if worker['age'] > 18]
    print(legal_age)
    
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    print(adults)

    # old_people = list(map(lambda worker: {**worker,  **{'old': worker['age']> 70}}, DATA ))
    # print(old_people) *py 3.5 a 3.8

    old_people = list(map(lambda worker: worker | {'old': worker['age']> 70}, DATA ))
    # Py 3.9 hacia arriba simbolo pipe | es un concatenador de diccionarios
    print(old_people)

    """Ejercicios"""
    all_python_dev = list(filter(lambda worker : worker["language"] == 'python', DATA))
    all_python_dev =list(map(lambda worker: worker['name'], all_python_dev))
    print(all_python_dev)

    all_platzi_workers = list(filter(lambda worker : worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker : worker['name'], all_platzi_workers))
    print(all_platzi_workers)

    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(adults)

    old_people = [worker | {'old': worker['age']> 70} for worker in DATA ]
    print(old_people)



if __name__ == '__main__':
    run()



import pandas as pd


def update(data: pd.DataFrame):
    new_data = data.copy(deep=True)
    new_data['average'] = (new_data['maths'] + new_data['physics'] + new_data['computer science']) / 3
    new_data = new_data.sort_values(['average', 'name'], ascending=[False, True])
    return new_data


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Сидоров', 'Петров', 'Иванов', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)

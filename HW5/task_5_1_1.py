pupils_list = [{'firstname': 'Masha',
                'group': '42',
                'physics': '1',
                'informatics': '4',
                'history': '3',
                },
               {'firstname': 'Masha1',
                'group': '42',
                'physics': '7',
                'informatics': '9',
                'history': '1',
                },
               {'firstname': 'Masha2',
                'group': '42',
                'physics': '7',
                'informatics': '6',
                'history': '1',
                },
               {'firstname': 'Masha3',
                'group': '42',
                'physics': '4',
                'informatics': '4',
                'history': '1',
                },
               {'firstname': 'Masha4',
                'group': '42',
                'physics': '5',
                'informatics': '6',
                'history': '0',
                },
               {'firstname': 'Masha5',
                'group': '42',
                'physics': '7',
                'informatics': '3',
                'history': '3',
                },
               {'firstname': 'Masha6',
                'group': '42',
                'physics': '7',
                'informatics': '3',
                'history': '2',
                },
               {'firstname': 'Masha7',
                'group': '42',
                'physics': '7',
                'informatics': '3',
                'history': '8',
                },
               {'firstname': 'Masha8',
                'group': '42',
                'physics': '4',
                'informatics': '3',
                'history': '2',
                },
               {'firstname': 'Masha9',
                'group': '42',
                'physics': '4',
                'informatics': '3',
                'history': '2',
                },
               {'firstname': 'Masha10',
                'group': '42',
                'physics': '4',
                'informatics': '3',
                'history': '2',
                },
               ]
# Declare variables
lessons_name = ['physics', 'informatics', 'history']
qty_lessons_name = len(lessons_name)
sum_dict = {}
qty_pupils = len(pupils_list)
# First task (average in each class)
for every_dict in list(pupils_list):
    for key in list(every_dict.keys()):
        if key in lessons_name:
            if every_dict[key].isdigit() == 0:
                print(f'Bad data type in {key} value. Bad input is "{every_dict[key]}"')
                continue
            lesson_name = f'{key}_AVG'
            check_to_first_update = sum_dict.get(lesson_name)
            if check_to_first_update is None:
                sum_dict.update({lesson_name: int(every_dict[key])})
            else:
                sum_dict.update({lesson_name: (sum_dict.get(lesson_name) + int(every_dict[key]))})

for key in list(sum_dict.keys()):
    sum_dict.update({key:sum_dict[key]/qty_pupils})
print(sum_dict)


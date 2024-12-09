# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


#print("Общие участники среди двух групп:", participants_first_group.intersection(participants_second_group))

def find_common_participants(group1, group2, n=','):
 first = set(group1.split(n))
 second = set(group2.split(n))
 common_participants = first.intersection(second)
 return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, n='|')
print(common_participants)

participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

print (find_common_participants(participants_first_group_comma, participants_second_group_comma))
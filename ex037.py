from datetime import date
atual = date.today().year
nascimento = int(input('que ano você nasceu?: '))
idade = atual - nascimento
print(f'o atleta tem {idade} anos')
if idade <= 9:
    print('esta na categoria MIRIM!')
elif 9 <= idade <= 14:
    print('esta na categoria INFANTIL!')
elif 14 <= idade <= 19:
    print('esta na categoria JUNIOR!')
elif 19 <= idade <= 25:
    print('esta na categoria SENIOR!')
else:
    print('esta na categoria MASTER!')
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count(), "\n")  # noqa: T001
    passcards = Passcard.objects.all()
    #print(*passcards, sep="\n")
    some_person = passcards[10]
    print(f"owener_name: {some_person.owner_name}")
    print(f"passcode: {some_person.passcode}")
    print(f"created_at: {some_person.created_at}")
    print(f"is_active: {some_person.is_active}")
    print()
    print(f"Всего пропусков: {len(passcards)}")
    print(f"Активных пропусков: {len(list(filter(lambda x: x.is_active, passcards)))}")
    print()
    active_passcards = Passcard.objects.filter(is_active=True)
    print(f"Всего пропусков: {len(passcards)}")
    print(f"Активных пропусков: {len(active_passcards)}")


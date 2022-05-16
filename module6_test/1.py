sorted_birthdays_per_week = {key: value for key,
                             value in sorted(birthdays_per_week.items())}
for k, v in sorted_birthdays_per_week.items():
    print(k + ': ' + ','.join(v))

station_names = input()
if '(' in station_names:
    station_name = station_names[:station_names.index('(')]
    print(station_name)
    print(station_names[station_names.index('('):][1:-1])
else:
    print(station_names)
    print('-')
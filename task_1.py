time_date= '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time_date.split(",")

total_minutes = 0

for t in time_values:
    units = t.split()

    for unit in units:
        if "h" in unit:
            total_minutes += int(unit.replace('h',''))*60
        elif "m" in unit:
            total_minutes += int(unit.replace("m",''))
        elif "s" in unit:
            total_minutes += int(unit.replace('s',''))//60

print(total_minutes)
        
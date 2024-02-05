"""
    figure out the end time of an event.
    assuming 24 hour clock.
"""
print("\n\n")
start_hour = int(input("Starting time (hours): "))
start_mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

dura_hours = dura // 60
dura_mins = dura % 60


end_mins = start_mins + dura_mins
increment_hour = end_mins // 60
end_mins = end_mins % 60
end_hour = start_hour + dura_hours + increment_hour
print(f"End time: {end_hour}:{end_mins}")

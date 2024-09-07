import shutil
import psutil


# Function to check disk usage, returns True if more than 20% is free, False otherwise
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


# Function to check CPU usage, returns True if usage is less than 75%, False otherwise
def check_cpu_usage():
    cpu = psutil.cpu_percent(1)
    return cpu < 75


# Function to get event date for sorting
def get_event_date(event):
    return event.date


# Function to track current users on machines based on events
def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


# Function to generate report of users logged into machines
def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))


# Class representing an event with date, type, machine name, and user
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


# List of events to process
events = [
    Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

# Check system health before processing events
if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR: System resources are low!")
else:
    # Proceed with event processing if system is healthy
    machines = current_users(events)
    generate_report(machines)

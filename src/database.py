import csv
# from deadlined_reminders import DeadLinedReminder, DateReminder


def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text, date, ReminderClass):
    if not issubclass(ReminderClass, ):
        raise TypeError('Invalid Reminder Class')

    with open('reminders.csv', 'a+', newline='\n') as file:
        reminder = ReminderClass(text, date)
        writer = csv.writer(file)
        writer.writerow(reminder)

        #DeadLinedReminder()


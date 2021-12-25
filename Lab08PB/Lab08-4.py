#Lab08-4 (Time)

def read_hour():
    hour = int(input("Enter hour: "))
    return hour

def read_minute():
    minute = int(input("Enter minute: "))
    return minute

def read_second():
    second = int(input("Enter second: "))
    return second

def to_second(hour, minute, second):
    convert_second = (hour * 3600) + (minute * 60) + second
    return convert_second

def time_elapsed(start, finish):
    total = finish - start
    hour = total // 3600
    minute = total // 60 % 60
    second = total % 60
    result = "{:d} hours {:d} minutes {:d} seconds." .format(hour, minute, second)
    return result
    
def read_time():
    print(">> ", end='')
    hour = read_hour()
    print(">> ", end='')
    minute = read_minute()
    print(">> ", end='')
    second = read_second()
    return to_second(hour, minute, second)

print("Start time:")
start_time = read_time()
print("Finish time:")
finish_time = read_time()
print("Elapsed time is", time_elapsed(start_time, finish_time))

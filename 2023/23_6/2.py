with open('23_6/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()

    times = {40829166: 277133813491063}

    result = 1
    for time in times:
        temp = 0
        for i in range(1, time):
            remaining_time = time - i
            speed = i

            if remaining_time * speed > times[time]:
                temp += 1
            
        result *= temp

    print(result)
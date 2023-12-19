def main():
    times_dist = {46828479: 347152214061471}  
    finish_speeds = []
    for i in times_dist.items():
        finish_speeds.append(race(i))
    total = 1
    for speeds in finish_speeds:
        total = len(speeds) * total
    print(total)


def race(time_dist):
    race_times = []
    race_length_mm = time_dist[0]
    time_remaining_mm = race_length_mm
    for i in range(1, time_remaining_mm):
        time_remaining_mm = race_length_mm - i
        if (i * time_remaining_mm) > time_dist[1]:
            race_times.append((i * time_remaining_mm))
    return race_times


if __name__ == "__main__":
    main()
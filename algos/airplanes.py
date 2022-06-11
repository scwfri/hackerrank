#!/usr/bin/env python
"""
arrival and departure times for airport
schedules remain the same across all days
determine the number of gates an airport should have so no plane spends time waiting for a gate
arr = [9:30, 11:15, 16:30]
dep = [11:45, 11:30, 16:45]

arr sorted by time
dep arr is sorted by corresponding arr array (plane 'i' arrives at arr[i] and departs at dep[i]
"""


def test(arr, dep):
    arr = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in arr]
    dep = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in dep]
    dep = sorted(dep)
    current_planes = 0
    current_departure_position = 0
    max_arrival = 1

    for i in range(len(arr)):
        arr_time = arr[i]
        max_arrival = max(max_arrival, current_planes)
        current_planes += 1

        for j in range(current_departure_position, len(dep)):
            if dep[j] < arr_time:
                current_departure_position = j
                current_planes -= 1
            else:
                break

    return max_arrival


def mine(arr, dep):
    arr = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in arr]
    dep = [int(t.split(":")[0]) * 60 + int(t.split(":")[1]) for t in dep]

    gates_occupied = []
    max_size = 0
    for idx, arrival in enumerate(arr):
        if not gates_occupied:
            gates_occupied.append(idx)
        else:
            for j in gates_occupied:
                if dep[j] > arr[idx]:
                    gates_occupied.append(idx)
                    break

        print(gates_occupied)
        max_size = max(max_size, len(gates_occupied))

    return max_size


if __name__ == "__main__":
    arr = ["9:30", "10:45", "11:00", "11:15", "16:30"]
    dep = ["11:45", "12:00", "12:30", "11:30", "16:45"]
    print(test(arr, dep))
    print(mine(arr, dep))

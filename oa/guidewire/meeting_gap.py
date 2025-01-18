def parse_meeting_time(meeting):
    day_map = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    day, time_range = meeting.split()
    start_time, end_time = time_range.split('-')

    start_minutes = day_map[day] * 24 * 60 + int(start_time[:2]) * 60 + int(start_time[3:])

    if end_time == "24:00":
        end_minutes = (day_map[day] + 1) * 24 * 60
    else:
        end_minutes = day_map[day] * 24 * 60 + int(end_time[:2]) * 60 + int(end_time[3:])
    return start_minutes, end_minutes


def solution(S):
    meetings = S.splitlines()
    time_intervals = []

    for meeting in meetings:
        start, end = parse_meeting_time(meeting)
        time_intervals.append((start, end))

    time_intervals.sort()

    time_intervals.insert(0, (0, 0))  # Monday 00:00
    time_intervals.append((7 * 24 * 60, 7 * 24 * 60))  # Sunday 24:00

    max_sleep = 0
    for i in range(1, len(time_intervals)):
        gap = time_intervals[i][0] - time_intervals[i - 1][1]
        max_sleep = max(max_sleep, gap)

    return max_sleep

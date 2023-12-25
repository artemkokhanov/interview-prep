def get_total_execution_time(n, logs):
    stack = []
    exec_times = [0] * n
    prev_timestamp = 0
    for log in logs:
        func_id, action, timestamp = log.split(":")
        func_id, timestamp = int(func_id), int(timestamp)
        if action == "start":
            if stack:
                exec_times[stack[-1]] += timestamp - prev_timestamp
            stack.append(func_id)
            prev_timestamp = timestamp
        else:
            # .pop() and +1 because it is an "end" action
            exec_times[stack.pop()] += timestamp - prev_timestamp + 1
            prev_timestamp = timestamp + 1
    return exec_times


if __name__ == "__main__":
    result = get_total_execution_time(3, ["0:start:0", "2:start:4", "2:end:5", "1:start:7", "1:end:10", "0:end:11"])
    assert result, [6, 4, 2]

import os
import re
from datetime import time, date, datetime, timedelta
from collections import defaultdict
from helper.input_output import file


class Sleep:
    date = date(1500, 1, 13)
    start_time = time(hour=0)
    end_time = time(hour=0)

    def __init__(self):
        self.minute_set = set()

    def get_start(self):
        return self.start_time

    def set_start(self, start_time):
        self.start_time = start_time

    def get_end(self):
        return self.end_time

    def set_end(self, end_time):
        self.end_time = end_time

    def get_duration(self):
        return self.end_time.minute - self.start_time.minute

    def get_minutes_asleep(self):
        if len(self.minute_set) == 0:
            for minute in range(self.start_time.minute, self.end_time.minute):
                self.minute_set.add(minute)
        return self.minute_set


class Guard:
    id = 0
    total_sleep = 0

    def __init__(self, id):
        self.id = id
        self.sleeps = set()

    def get_id(self):
        return self.id

    def add_sleep(self, sleep):
        self.sleeps.add(sleep)
        self.total_sleep += sleep.get_duration()

    def get_sleeps(self):
        return self.sleeps

    def get_most_slept_minute(self):
        sleep_dict = defaultdict(int)
        for sleep in self.sleeps:
            for minute in sleep.get_minutes_asleep():
                sleep_dict[minute] += 1
        best_minute = -1
        best_count = -1
        for minute in sleep_dict.keys():
            if best_count < sleep_dict[minute]:
                best_minute = minute
                best_count = sleep_dict[minute]
        return best_minute

    def get_total_sleep(self):
        return self.total_sleep


def parse_time_log(entry_list):
    guard_by_id = dict()
    days_guard_id = dict()
    date_time_list = []
    dated_entry_dict = dict()

    for entry in entry_list:
        date_matcher = re.match("\[(\d{4})-(\d{2})-(\d{2})\s(\d{2}):(\d{2})\]\s(.+)", entry)
        if date_matcher is None:
            raise ValueError(f"Could not match against {entry}")
        date_time = datetime(int(date_matcher.group(1)), int(date_matcher.group(2)), int(date_matcher.group(3)),
                             int(date_matcher.group(4)), int(date_matcher.group(5)))
        date_time_list.append(date_time)
        dated_entry_dict[date_time] = date_matcher.group(6)

    date_time_list.sort()
    last_sleep = Sleep()
    for date_time in date_time_list:
        entry = dated_entry_dict[date_time]
        guard_matcher = re.search("\#(\d+)", entry)

        if guard_matcher is not None:
            guard_id = int(guard_matcher.group(1))
            if guard_id not in guard_by_id:
                new_guard = Guard(guard_id)
                guard_by_id[guard_id] = new_guard
            if date_time.hour == 23:  # Guard started early. Set day to next day
                days_guard_id[date_time.date() + timedelta(days=1)] = guard_id
            else:
                days_guard_id[date_time.date()] = guard_id
        elif "sleep" in entry:
            last_sleep.set_start(date_time.time())
        elif "wake" in entry:
            last_sleep.set_end(date_time.time())
            guard_by_id[days_guard_id[date_time.date()]].add_sleep(last_sleep)
            last_sleep = Sleep()
    return guard_by_id


filename = os.path.join(os.path.dirname(__file__), 'day4_input.txt')
entries, guard_list = file.load_file_list_function(filename, str.rstrip, parse_time_log)
current_guard = None
for guard_key in guard_list.keys():
    if current_guard is None:
        current_guard = guard_list[guard_key]
    elif current_guard.get_total_sleep() <= guard_list[guard_key].get_total_sleep():
        current_guard = guard_list[guard_key]

print(f"Award for most sleepy guard goes to #{current_guard.get_id()} who slept for {current_guard.get_total_sleep()}"
      f" minutes and was asleep most often at {current_guard.get_most_slept_minute()}")
print(f"That makes this part's answer {current_guard.get_id() * current_guard.get_most_slept_minute()}")

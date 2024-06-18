intervals = [(7, 9), (2, 4), (5, 8)]

def interval_overlapping_check(intervals):

    intervals.sort(key=lambda x : x[1])
    end = 0
    removals = 0

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            removals += 1
    
    return removals

print(interval_overlapping_check(intervals))


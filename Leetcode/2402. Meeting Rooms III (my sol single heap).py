class Solution:

    # my own solution with a single heap
    # solved Insert Interval, Merge Interval, Non-overlapping Intervals & Meeting Rooms II in one sitting before doing this to get myself primed (first three for the start/end time comparisons, last one for minheap usage)
    # a better solution exists using two minheaps that allows me to skip the loop at line 33, but I will get to that one later

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort meeting times by start values (this is probably already done)
        meetings.sort(key = lambda pair: pair[0]) 

        # key:value of meeting_end_time:room_number
        used_rooms = []
        # (meetings[0][1] is endtime of meeting 1, 0 is 0th (lowest) free room)
        heapq.heappush(used_rooms, (meetings[0][1], 0))

        # counter for free room
        free_room_counter = 1

        # counter for number of meetings held in ith room
        meeting_counter = {}
        for i in range(n):
            meeting_counter[i] = 0
        # first room is in use by initialization
        meeting_counter[0] = 1

        for meeting in meetings[1:]:

            # if start_time is at or after the meeting that is ending the soonest (used_rooms[0][0])
            if meeting[0] >= used_rooms[0][0]:

                # the lowest meeting end_time is not necessarily the lowest index. look through the rest of the (end_time, room_index) pairs to find lowest index where occupied end_time is <= current start_time
                soonest_end_index = 0
                for index in range(1, len(used_rooms)):
                    # this needs to account for whether new index's end time is lower than current meeting's start time as well as the room number is lower than the last found soonest index
                    if used_rooms[index][0] <= meeting[0] and used_rooms[index][1] < used_rooms[soonest_end_index][1]:
                        soonest_end_index = index

                # free up said room and assign it to the current meeting
                if soonest_end_index == 0:
                    # if the lowest available room is 0th index, a simple heappop operation is fine
                    soonest_end_time, free_room = heapq.heappop(used_rooms)
                else:
                    # if the index is not zero, we need to remove said index from the array and heapify the whole thing again.
                    soonest_end_time, free_room = used_rooms[soonest_end_index]
                    used_rooms.pop(soonest_end_index)
                    # leetcode submission does accept if I don't use line 47, but it does not seem like a good idea to leave that out
                    heapq.heapify(used_rooms)

                # same logic as line 14
                heapq.heappush(used_rooms, (meeting[1], free_room))
                meeting_counter[free_room] += 1
                
            # if existing meeting has not ended and we do have free rooms remaining
            elif free_room_counter < n:
                # assign lowest free room to current meeting and then incrementing it
                heapq.heappush(used_rooms, (meeting[1], free_room_counter))
                meeting_counter[free_room_counter] += 1
                free_room_counter += 1
                
            # if current meeting needs to wait / is delayed
            else:
                # find the meeting (and associated room) that is ending the soonest
                soonest_end_time, free_room = heapq.heappop(used_rooms)
                # find the updated end_time of current meeting since it was delayed. soonest ongoing meeting ending time minus the current meeting start time is the delay amount in unit time
                delay = soonest_end_time - meeting[0]
                # the addition of 'delay' to account for the updated start and end times since the meeting had to wait
                heapq.heappush(used_rooms, (delay + meeting[1], free_room))
                meeting_counter[free_room] += 1
        
        # find highest meeting room frequency
        highest = 0
        for room in meeting_counter:
            if meeting_counter[room] > meeting_counter[highest]:
                highest = room

        return highest
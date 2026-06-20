import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Sort the custom objects directly by their start time
        intervals.sort(key=lambda x: x.start)
        
        # Min-heap to track the end times of ongoing meetings
        rooms = []
        
        for meeting in intervals:
            # If a room is free (oldest end time <= current start time), reuse it
            if rooms and meeting.start >= rooms[0]:
                heapq.heapreplace(rooms, meeting.end)
            else:
                # Otherwise, allocate a new room
                heapq.heappush(rooms, meeting.end)
                
        return len(rooms)
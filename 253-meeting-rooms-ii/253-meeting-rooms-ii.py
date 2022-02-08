class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        meeting = []
        
        for i in intervals:
            meeting.append((i[0], 1)) # meeting start, room needed +1
            meeting.append((i[1], -1)) # meeting end, one more room available, room in use -1
            
        ongoing = 0
        room = 0
        
        for _, delta in sorted(meeting):
            ongoing += delta
            room = max(room, ongoing)
        
        return room
            
        
# 扫描线，把所有的时间排序，按照开始时间升序，开始时间相同结束时间升序的方式进行排序，如果时间相同，结束时间在前，
# 扫描一遍，当扫描到开始时间，就会多一个房间，当扫描到结束时间就少一个房间，这样扫描到i时候就是i时间所需要的最少的房间
# 我们的房间数量要满足所有时间的需求，所以答案就是对所有时间所需要的最少房间取最大值，这样就能满足所有时间的开会需求了。
# http://us.jiuzhang.com/solution/meeting-rooms-ii/
# 九章扫描线
 # Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
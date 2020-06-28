"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

 

Example 1:



Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0


Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        # per minute movement
        per_minute_degrees_m_hand = 6
        per_hour_degrees_h_hand = 30
        per_minutes_degrees_h_hand = 0.5

        # find degree from 12 o clock position for both
        min_deg = minutes * per_minute_degrees_m_hand
        hour = 0 if hour == 12 else hour
        hour_deg = hour * per_hour_degrees_h_hand + minutes * per_minutes_degrees_h_hand
        result = abs(min_deg - hour_deg)
        if result > 180:
            result = 360 - result
        return result

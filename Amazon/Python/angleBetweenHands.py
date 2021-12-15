
"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        degrees_per_minute = 360/60
        degrees_per_hour = 360/12
        
        hour_degrees = ((hour % 12) + (minutes/60)) * 30
        minutes_degrees = minutes * 6
        
        val = abs(hour_degrees-minutes_degrees)
        
        return  min(val,360-val)

if __name__ == "__main__":
    hours =  1
    minutes = 57
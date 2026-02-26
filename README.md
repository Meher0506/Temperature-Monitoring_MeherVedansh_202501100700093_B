# Temperature-Monitoring_MeherVedansh_202501100700093_B
Case Study-02 "Temperature Monitoring System"

**Problem Statement :-**
- Build a Python code to display messages according to the temperature received from an assumed IoT system.
- Accept max and min limit temperature.
- Generate random values for temperature at every 2 second interval.
- Compare with the limits to display appropriate value.

**Approach :-**
- Take the min and max temp limit from user.
- Generate a random temp between 0 & 100.
- if the temp is higher or lower than the limit, give the output.

**Sample Output :-**
Enter minimum temperature limit: 25
Enter maximum temperature limit: 45

Starting Temperature Monitoring...

Current Temperature: 19°C
Alert: Temperature is too low
------------------------------
Current Temperature: 5°C
Alert: Temperature is too low
------------------------------
Current Temperature: 52°C
Alert: Temperature is too high
------------------------------

import random
import time

# Accept minimum and maximum temperature limits
min_temp = float(input("Enter minimum temperature limit: "))
max_temp = float(input("Enter maximum temperature limit: "))

print("\nStarting Temperature Monitoring...\n")

# Continuous monitoring loop
while True:
    
    # Generate random temperature between 0 and 100
    temperature = random.randint(0, 100)
    
    print(f"Current Temperature: {temperature}°C")
    
    # Compare temperature with limits
    if temperature > max_temp:
        print("Alert: Temperature is too high")
        
    elif temperature < min_temp:
        print("Alert: Temperature is too low")
        
    else:
        print("Temperature is within acceptable limit")
    
    print("------------------------------")
    
    # Wait for 2 seconds
    time.sleep(2)

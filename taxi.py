def calculate_fare(distance, base_fare=50, per_km_rate=10):
    return base_fare + (distance * per_km_rate)

# Input: distances for each trip
trips = [5, 10, 3]  # in km

total_fare = 0

# Calculate and print fare per trip
for i, distance in enumerate(trips, start=1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

# Print total fare
print(f"Total Fare: ${total_fare}")

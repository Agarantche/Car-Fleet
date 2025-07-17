class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Combine car position and speed, then sort by position in descending order.
        # This allows processing cars from the one closest to the target backward.
        carsData = sorted([(position[i], speed[i]) for i in range(len(position))], key=lambda x: x[0], reverse=True)

        # Stack to store the arrival times of the leading car of each fleet.
        fleetArrivalTimes = []

        for currentPos, currentSpeed in carsData:
            # Calculate the time it takes for the current car to reach the target.
            # Using float() ensures floating-point division.
            timeToTarget = float(target - currentPos) / currentSpeed

            # If the stack is empty (no fleets yet) or the current car's arrival time
            # is strictly greater than the last fleet's arrival time, it forms a new fleet.
            # Otherwise, it joins the existing fleet ahead of it.
            if not fleetArrivalTimes or timeToTarget > fleetArrivalTimes[-1]:
                fleetArrivalTimes.append(timeToTarget)

        # The number of elements in the stack represents the total number of distinct car fleets.
        return len(fleetArrivalTimes)

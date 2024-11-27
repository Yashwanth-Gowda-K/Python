import time

class TrafficLight:
    def __init__(self, color="Red"):
        self.color = color
    
    def change_color(self, new_color):
        print(f"Changing light to {new_color}")
        self.color = new_color

class TrafficControlSystem:
    def __init__(self):
        self.lights = {
            'North': TrafficLight(),
            'East': TrafficLight(),
            'South': TrafficLight(),
            'West': TrafficLight()
        }
        self.sensors = {
            'North': 0,  # Initial traffic sensor count for North (cars detected)
            'East': 0,   # Initial traffic sensor count for East
            'South': 0,  # Initial traffic sensor count for South
            'West': 0    # Initial traffic sensor count for West
        }
    
    def detect_traffic(self):
        # Simulate traffic detection with random values (in a real system, this would come from sensors)
        for direction in self.sensors:
            self.sensors[direction] = random.randint(0, 10)  # Simulating traffic detection
    
    def control_traffic(self):
        while True:
            # Detect traffic
            self.detect_traffic()
            print(f"Traffic Sensors (Cars Detected): {self.sensors}")
            
            # Decision logic based on traffic
            if self.sensors['North'] > self.sensors['South']:
                self.lights['North'].change_color("Green")
                self.lights['South'].change_color("Red")
            else:
                self.lights['South'].change_color("Green")
                self.lights['North'].change_color("Red")
            
            if self.sensors['East'] > self.sensors['West']:
                self.lights['East'].change_color("Green")
                self.lights['West'].change_color("Red")
            else:
                self.lights['West'].change_color("Green")
                self.lights['East'].change_color("Red")
            
            # Wait for the next cycle (e.g., every 5 seconds)
            time.sleep(5)

if __name__ == "__main__":
    import random
    
    # Initialize the traffic control system
    system = TrafficControlSystem()
    
    # Start the traffic light control
    system.control_traffic()

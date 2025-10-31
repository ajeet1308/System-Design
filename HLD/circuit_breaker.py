import time
import random

class CircuitBreaker:
    # Define the states of the CircuitBreaker
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

    def __init__(self, failure_threshold=5, recovery_timeout=10, success_threshold=3):
        # Initialize the circuit breaker with thresholds and timeouts
        self.state = self.CLOSED  # Initial state is CLOSED
        self.failure_count = 0  # Number of consecutive failures
        self.success_count = 0  # Number of successful attempts in HALF_OPEN state
        self.failure_threshold = failure_threshold  # Threshold for failures to open the circuit
        self.recovery_timeout = recovery_timeout  # Time to wait before transitioning from OPEN to HALF_OPEN
        self.success_threshold = success_threshold  # Number of successes required to close the circuit again
        self.last_failure_time = 0  # Timestamp when the last failure occurred

    def call(self):
        """Simulate a call to the protected service."""
        if self.state == self.OPEN:
            # If the circuit is OPEN, immediately fail the request and return failure
            if time.time() - self.last_failure_time < self.recovery_timeout:
                print("Circuit is OPEN. Request is blocked.")
                return False
            else:
                print("Circuit is OPEN but recovery timeout expired. Transitioning to HALF_OPEN.")
                self.state = self.HALF_OPEN

        if self.state == self.HALF_OPEN:
            # In HALF_OPEN state, allow a few requests to pass through for testing
            success = self._simulate_service_call()
            if success:
                self.success_count += 1
                print("Request succeeded in HALF_OPEN state.")
                if self.success_count >= self.success_threshold:
                    print("Enough successful requests. Transitioning to CLOSED state.")
                    self.state = self.CLOSED
                    self.success_count = 0  # Reset success count
            else:
                print("Request failed in HALF_OPEN state.")
                self.state = self.OPEN
                self.last_failure_time = time.time()  # Record the failure time
                self.success_count = 0  # Reset success count
            return success

        if self.state == self.CLOSED:
            # In CLOSED state, try to call the service and monitor for failures
            success = self._simulate_service_call()
            if success:
                print("Request succeeded.")
                self.failure_count = 0  # Reset failure count
            else:
                self.failure_count += 1
                print("Request failed.")
                if self.failure_count >= self.failure_threshold:
                    print("Failure threshold reached. Opening circuit.")
                    self.state = self.OPEN
                    self.last_failure_time = time.time()  # Record the failure time
            return success

    def _simulate_service_call(self):
        """Simulate the service call with random success/failure."""
        # Here, we simulate the outcome of a service call.
        # Let's assume 80% chance of success and 20% of failure
        return random.random() < 0.5

    def get_state(self):
        """Return the current state of the Circuit Breaker."""
        return self.state

    def reset(self):
        """Reset the circuit breaker back to the CLOSED state."""
        print("Resetting Circuit Breaker.")
        self.state = self.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = 0


# Example usage:

# Create a CircuitBreaker instance
cb = CircuitBreaker(failure_threshold=3, recovery_timeout=5, success_threshold=2)

# Simulate some calls
for _ in range(10):
    cb.call()
    time.sleep(1)  # Simulate a delay between requests

# Check the current state
print("Current Circuit Breaker State:", cb.get_state())

# Reset the circuit breaker
cb.reset()

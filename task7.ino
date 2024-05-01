// Water Flow Sensor Arduino Code

const int flowSensorPin = 8;  // Connect the output pin of the water flow sensor to digital pin 2
unsigned int flowRate;        // Variable to store the flow rate

void setup() {
  Serial.begin(9600);        // Initialize serial communication at 9600 baud rate
  pinMode(flowSensorPin, INPUT_PULLUP); // Set the flow sensor pin as input with internal pull-up resistor
}

void loop() {
  flowRate = pulseIn(flowSensorPin, HIGH);  // Measure the time between pulses (HIGH state) from the flow sensor

  // Convert the pulse time to flow rate (adjust the constant value to match your sensor)
  int mLPerSec = (flowRate / 7.5);  // 7.5 is a constant value based on the sensor specifications

  // Print the flow rate to the serial monitor
  Serial.println(mLPerSec);

  delay(1000);  // Delay for 1 second before the next reading
}
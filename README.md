# Temperature-Converter
The Temperature Converter project is designed to facilitate the conversion of temperatures between three commonly used scales: Celsius, Fahrenheit, and Kelvin. This tool is particularly useful for scientific, educational, and practical applications where temperature conversion is frequently required
ore Functionality:
User Input:

The user selects the temperature scale of the input value (Celsius, Fahrenheit, or Kelvin).
The user enters the temperature value they wish to convert.
Temperature Conversion:

Based on the selected scale, the input temperature is converted to the other two scales using specific mathematical formulas:

Celsius to Fahrenheit: (C * 9 / 5) + 32
Celsius to Kelvin    : C + 273.15

Fahrenheit to Celsius: (5 / 9) * (F - 32)
Fahrenheit to Kelvin : C + 273.15
  
Kelvin to Celsius    : K - 273.15
Kelvin to Fahrenheit : (C * 9 / 5) + 32

User Interface:
HTML Form: A simple web form allows users to select the temperature scale and input the temperature value.
Result Display: After submission, the converted temperatures are displayed on the same page.

Technical Implementation:
Backend: Implemented using Flask, a lightweight web framework in Python.
Frontend: Basic HTML for structure and inline CSS for styling, ensuring a user-friendly interface.

Routes:
Home Route (/): Displays the input form.
Convert Route (/convert): Processes the form submission, performs conversions, and returns the results.

Use Cases:
Educational Tools: Helping students learn and understand temperature conversions.
Scientific Research: Assisting researchers who need to convert temperature readings.
Daily Use: Providing a handy tool for anyone needing to convert temperatures for cooking, weather, or other daily activities.

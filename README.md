# GUI RAMMeasuring Tool version 1.0.0

This is a Python-based desktop application designed to monitor real-time RAM usage, including detailed memory statistics and a graphical representation of RAM usage. The application is built using **Tkinter** for the GUI and **Matplotlib** for the dynamic graph.

<img width="516" alt="image" src="https://github.com/user-attachments/assets/5f758c86-3b89-46cb-9e13-2aa979d4f5d9">

---

## Features

- **Real-Time RAM Monitoring**: Tracks RAM usage and displays updated statistics every second.
- **Mini Graph**: Visualizes RAM usage percentage in real-time.
- **Detailed RAM Information**:
  - Total RAM
  - Used RAM
  - Available RAM
  - Cached Memory (if supported)
  - Buffer Memory (if supported)
  - Swap Memory (Total, Used, and Percentage)
- **Warning System**: Alerts the user when RAM usage exceeds a configurable threshold.
- **Cross-Platform Compatibility**: Works on Windows, Linux, and macOS.

---

## Requirements

### Python Version
- Python 3.6 or later is required.

### Python Libraries
Install the required libraries using the following command:
```bash
pip install psutil matplotlib
```

---

## How to Use

1. Clone or download this repository.
2. Ensure the required libraries are installed (see **Requirements** above).
3. Run the application:
   ```bash
   python main.py
   ```
4. View real-time RAM usage details and warnings in the GUI.

---

## Screenshots

### Main Interface
- Displays real-time RAM usage in a graph and detailed statistics.

### Warning Example
- A red warning appears if RAM usage exceeds the specified threshold.

---

## Configuration

- **Warning Threshold**: By default, a warning is triggered if RAM usage exceeds 80%. To change this, modify the `WARNING_THRESHOLD` constant in the script:
  ```python
  WARNING_THRESHOLD = 90  # Set warning level to 90%
  ```

---

## Compatibility

The tool has been tested on:
- Windows 10/11
- Ubuntu 20.04+
- macOS Monterey

---

## Future Enhancements

- Add support for logging usage data to a file.
- Include CPU and Disk monitoring alongside RAM statistics.
- Customizable themes for the GUI.

---

## License

This project is open-source and licensed under the MIT License. Feel free to modify and distribute the code as per the license terms.

---

## Author

Developed by 47cyber.  
If you have questions or suggestions, feel free to contact me at support@47cyber.com.

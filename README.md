# my-lan-dashboard

## Overview
my-lan-dashboard is a web application designed for mapping devices on a home network. It provides an intuitive interface for users to scan their network, view connected devices, and manage device information.

## Features
- **Network Scanning**: Manually scan the network to detect connected devices and their MAC addresses.
- **Device Management**: Store and manage information about devices, including vendor, hostname, and last access date.
- **Custom Fields**: Add user-defined fields for IP release type, connection type, and device type.
- **Real-time Updates**: View the latest information about devices connected to the network.

## Project Structure
```
my-lan-dashboard
├── backend
│   ├── app.py                # Main entry point for the backend application
│   ├── scan.py               # Network scanning logic
│   ├── db
│   │   └── models.py         # Database models for device information
│   ├── routes
│   │   └── devices.py        # API routes for managing devices
│   ├── utils
│   │   └── network.py        # Utility functions for network operations
│   └── requirements.txt      # Python dependencies for the backend
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the frontend application
│   ├── src
│   │   ├── App.jsx           # Main component of the React application
│   │   ├── components
│   │   │   ├── DeviceList.jsx # Component to display a list of devices
│   │   │   ├── DeviceForm.jsx # Component for adding new devices
│   │   │   └── ScanButton.jsx  # Component to trigger network scan
│   │   └── services
│   │       └── api.js        # Functions for making API calls to the backend
│   ├── package.json          # Configuration file for npm
│   └── README.md             # Documentation for the frontend part of the project
├── docker-compose.yml        # Service definitions for Docker
└── README.md                 # General documentation for the entire project
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-lan-dashboard
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```

4. Run the application using Docker:
   ```
   docker-compose up
   ```

## Usage
- Access the application in your web browser at `http://localhost:3000`.
- Use the provided interface to scan your network and manage device information.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.
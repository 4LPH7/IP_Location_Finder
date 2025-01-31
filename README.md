---

# IP Location Finder

![Banner](https://img.shields.io/badge/Version-1.2-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Python](https://img.shields.io/badge/Python-3.6%2B-yellow)

IP Location Finder is a Python-based command-line tool that allows you to retrieve detailed information about an IP address, including its geographical location, ISP, timezone, and more. It uses the [ip-api.com](http://ip-api.com) API to fetch the data.

---

## Features

- **IP Information**: Retrieve detailed information about any IP address.
- **Geolocation**: Get the country, region, city, and coordinates of the IP.
- **ISP Details**: Fetch the ISP and organization associated with the IP.
- **Google Maps Link**: Generate a Google Maps link for the IP's location.
- **User-Friendly**: Simple and intuitive command-line interface.
- **Colorful Output**: Output is color-coded for better readability.

---

## Installation

### Prerequisites

- Python 3.6 or higher.
- `requests` library (included in the script).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ip-location-finder.git
   cd ip-location-finder
   ```

2. **Run the Script**:
   ```bash
   python IPLocation.py --ip 8.8.8.8
   ```

---

## Usage

### Basic Usage

To get information about an IP address, use the `--ip` or `-I` option followed by the IP address:

```bash
python IPLocation.py --ip 8.8.8.8
```

### Help Menu

To display the help menu, use the `--help` or `-h` option:

```bash
python IPLocation.py --help
```

### Example Output

```
────────────────── IP LOCATION INFORMATION ──────────────────

    [+] COUNTRY ::: United States
    [+] COUNTRY CODE ::: US
    [+] REGION ::: California
    [+] REGION NAME ::: California
    [+] CITY ::: Mountain View
    [+] ZIP ::: 94035
    [+] LAT ::: 37.386
    [+] LON ::: -122.0838
    [+] TIME ZONE ::: America/Los_Angeles
    [+] ISP ::: Google LLC
    [+] ORG ::: Google LLC
    [+] AS ::: AS15169 Google LLC
    [+] IP ::: 8.8.8.8

    [+] GOOGLE MAP ::: https://www.google.com/maps/@37.386,-122.0838,13z

─────────────────────────────────────────────────────────────
```

---

## Options

| Option       | Description                          |
|--------------|--------------------------------------|
| `-h`, `--help` | Display the help menu.              |
| `-I`, `--ip`   | Fetch information for a specific IP. |

---

## API Used

This tool uses the [ip-api.com](http://ip-api.com) API to fetch IP information. Please note that the free version of the API has a limit of 45 requests per minute.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## Acknowledgments

- Thanks to [ip-api.com](http://ip-api.com) for providing the IP geolocation API.
- Inspired by various open-source IP lookup tools.

---


### Show your support

Give a ⭐ if you like this website!

<a href="https://buymeacoffee.com/arulartadg" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-violet.png" alt="Buy Me A Coffee" height= "60px" width= "217px" ></a>

---

Enjoy using **IP Location Finder**! 🌍

---

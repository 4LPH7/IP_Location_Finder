import sys
import requests
import ipaddress


class Config:
    """Configuration class for color codes and messages"""
    COLORS = {
        'lblue': '\033[96m',
        'red': '\033[91m',
        'grn': '\033[32m',
        'ylw': '\033[93m',
        'reset': '\033[0m'
    }

    @property
    def banner(self):
        """Returns a stylized banner for the application."""
        return f"""
{self.COLORS['lblue']}╔════════════════════════════════════════════════════════╗
{self.COLORS['lblue']}║                                                        ║
{self.COLORS['lblue']}║   {self.COLORS['red']}██╗  ██████╗      {self.COLORS['grn']}IP Location Finder                 {self.COLORS['lblue']}║
{self.COLORS['lblue']}║   {self.COLORS['red']}██║  ██╔══██╗     {self.COLORS['grn']}Coded By {self.COLORS['ylw']}4RU7                  {self.COLORS['lblue']}    ║
{self.COLORS['lblue']}║   {self.COLORS['red']}██║  ██████╔╝     {self.COLORS['grn']}GitHub ID {self.COLORS['red']}:: {self.COLORS['ylw']}4LPH7         {self.COLORS['lblue']}        ║
{self.COLORS['lblue']}║   {self.COLORS['red']}██║  ██╔═══╝      {self.COLORS['ylw']}Version {self.COLORS['red']}1.2                    {self.COLORS['lblue']}    ║
{self.COLORS['lblue']}║   {self.COLORS['red']}██║  ██║                                  {self.COLORS['lblue']}           ║
{self.COLORS['lblue']}║   {self.COLORS['red']}╚═╝  ╚═╝                                  {self.COLORS['lblue']}           ║
{self.COLORS['lblue']}║                                                        ║
{self.COLORS['lblue']}╚════════════════════════════════════════════════════════╝
{self.COLORS['reset']}"""

    @property
    def help_message(self):
        """Returns a formatted help message for the application."""
        return f"""
{self.COLORS['red']}╔════════════════════════════════════════════════════════╗
{self.COLORS['red']}║ {self.COLORS['ylw']}Usage: {self.COLORS['grn']}python IPLocation.py [OPTION] ...          {self.COLORS['red']}     ║
{self.COLORS['red']}║ {self.COLORS['ylw']}To get IP information                          {self.COLORS['red']}        ║
{self.COLORS['red']}║                                                        ║
{self.COLORS['red']}║ {self.COLORS['grn']}Mandatory arguments:                          {self.COLORS['red']}         ║
{self.COLORS['red']}║ {self.COLORS['red']}-h, --help {self.COLORS['ylw']}Display this help and exit            {self.COLORS['red']}      ║
{self.COLORS['red']}║ {self.COLORS['red']}-I, --ip   {self.COLORS['ylw']}Get information for a specific IP     {self.COLORS['red']}      ║
{self.COLORS['red']}║                                                        ║
{self.COLORS['red']}║ {self.COLORS['ylw']}Example:                                   {self.COLORS['red']}            ║
{self.COLORS['red']}║ {self.COLORS['grn']}python IPLocation.py {self.COLORS['red']}--ip {self.COLORS['ylw']}8.8.8.8         {self.COLORS['red']}             ║
{self.COLORS['red']}╚════════════════════════════════════════════════════════╝
{self.COLORS['reset']}"""


class IPLocator:
    """Handles IP location data retrieval"""
    API_URL = 'http://ip-api.com/json/'

    def __init__(self, ip):
        self.ip = ip

    def get_data(self):
        """Fetch and validate IP data from API"""
        try:
            response = requests.get(f'{self.API_URL}{self.ip}', timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get('status') != 'success':
                raise ValueError(f"API Error: {data.get('message', 'Unknown error')}")

            return data
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Connection failed: {str(e)}") from e


class OutputFormatter:
    """Handles output formatting and display"""

    def __init__(self, config):
        self.config = config
        self.colors = config.COLORS

    def show_banner(self):
        """Display the program banner"""
        print(self.config.banner)

    def show_help(self):
        """Display help message"""
        self.show_banner()
        print(self.config.help_message)

    def display_results(self, data):
        """Display formatted results"""
        fields = [
            ('COUNTRY', 'country'),
            ('COUNTRY CODE', 'countryCode'),
            ('REGION', 'region'),
            ('REGION NAME', 'regionName'),
            ('CITY', 'city'),
            ('ZIP', 'zip'),
            ('LAT', 'lat'),
            ('LON', 'lon'),
            ('TIME ZONE', 'timezone'),
            ('ISP', 'isp'),
            ('ORG', 'org'),
            ('AS', 'as'),
            ('IP', 'query'),
        ]

        google_map = f"https://www.google.com/maps/@{data.get('lat', '')},{data.get('lon', '')},13z"

        print(f"\n{self.colors['grn']}{' IP LOCATION INFORMATION ':-^60}{self.colors['reset']}\n")
        for display_name, key in fields:
            value = data.get(key, 'N/A')
            print(
                f"    {self.colors['grn']}[{self.colors['red']}+{self.colors['grn']}] {self.colors['lblue']}{display_name} {self.colors['red']}::: {self.colors['ylw']}{value}")

        print(
            f"\n    {self.colors['grn']}[{self.colors['red']}+{self.colors['grn']}] {self.colors['lblue']}GOOGLE MAP {self.colors['red']}::: {self.colors['ylw']}{google_map}")
        print(f"\n{self.colors['grn']}{'-' * 60}{self.colors['reset']}\n")


def validate_ip(ip):
    """Validate IP address format"""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def main():
    """Main program execution"""
    config = Config()
    formatter = OutputFormatter(config)

    if len(sys.argv) == 1:
        formatter.show_help()
        return

    if sys.argv[1] in ['-h', '--help']:
        formatter.show_help()
        return

    if sys.argv[1] in ['-I', '--ip']:
        if len(sys.argv) < 3:
            print(f"\n{config.COLORS['red']}Error: Missing IP address{config.COLORS['reset']}")
            formatter.show_help()
            return

        ip = sys.argv[2]
        if not validate_ip(ip):
            print(f"\n{config.COLORS['red']}Error: Invalid IP address format{config.COLORS['reset']}")
            return

        try:
            locator = IPLocator(ip)
            data = locator.get_data()
            formatter.display_results(data)
        except Exception as e:
            print(f"\n{config.COLORS['red']}Error: {str(e)}{config.COLORS['reset']}")
    else:
        print(f"\n{config.COLORS['red']}Error: Invalid argument{config.COLORS['reset']}")
        formatter.show_help()


if __name__ == "__main__":
    main()

from crewai_tools import tool
from typing import Optional
from datetime import datetime



@tool("SkyScanner tool")
def skyscanner(
    departure: str, destination: str, date: int, return_date: Optional[int] = ''
) -> str:
    """
    Generates a SkyScanner URL for flights between departure and destination on the specified date.

    :param departure: The IATA code for the departure airport (e.g., 'sof' for Sofia)
    :param destination: The IATA code for the destination airport (e.g., 'ber' for Berlin)
    :param date: The date of the flight in the format 'yymmdd'
    :return_date: Only for two-way tickets. The date of return flight in the format 'yymmdd'
    :return: The SkyScanner URL for the specified flight search
    """
    today_int = int(datetime.today().strftime('%Y%m%d'))

    # Error when date or return_date is in the past
    if date < today_int or return_date < today_int: 
        raise ValueError("Flight dates must be in the future.")
    
    # Error when return_date is not provided - should be blank but instead has /0 which makes the whole URL invalid
    return f"https://www.skyscanner.net/transport/flights/{departure}/{destination}/{date}/{return_date if return_date else ''}?currency=USD"

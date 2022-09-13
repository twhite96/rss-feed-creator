import typer
from enum import Enum
from typing import List, Optional

class ApprovedVaccine(str, Enum):
    pfizer = "pfizer"
    moderna = "moderna"
    astrazeneca = "astrazeneca"
    janssen = "janssen"
    sinovac = "sinovac"

def main(
    name: str = typer.Option(..., help="Your Name"),
    birth: str = typer.Option(..., help="Your birthday in YYYY-MM-DD format", callback=validate_date),
    manufacturer: Optional[List[ApprovedVaccine]] = typer.Option(..., help="The vaccine manufacturer", case_sensitive=False),
    date: Optional[List[str]] = typer.Option(..., help="The date of vaccination", callback=validate_date)
):
    """Generate your vaccination QR code."""
    # same logic as Click example
    print(name, birth, manufacturer, date)

if __name__ == "__main__":
<<<<<<< Updated upstream
    typer.run(main)n
=======
    typer.run(main)
>>>>>>> Stashed changes

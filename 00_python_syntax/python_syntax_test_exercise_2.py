#!/usr/bin/env python3


def create_profile() -> None:
    """Create a city profile"""
    city: str = "Luanda"
    zip_code: int = 100244
    is_coastal: bool = True
    if is_coastal:
        print(f"The city {city} with zip code {zip_code} is coastal")
    else:
        print(f"The city {city} with zip code {zip_code} is not coastal")


create_profile()

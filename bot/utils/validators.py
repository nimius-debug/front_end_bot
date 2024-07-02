import re

BTC_ADDRESS_REGEX = re.compile(r'^(1|3|bc1|tb1)[a-zA-HJ-NP-Z0-9]{25,39}$')

def is_valid_btc_address(address: str) -> bool:
    return bool(BTC_ADDRESS_REGEX.match(address))

# Add any other validation functions here
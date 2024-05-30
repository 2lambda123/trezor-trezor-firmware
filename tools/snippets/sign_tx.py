"""
Script for quick (and repeatable) creation and signing of
specific inputs and outputs inspired by BTC device tests.

INPUTS and OUTPUTS lists are the only things needed to be modified.

Similar to tools/build_tx.py, but more suitable for bigger/autogenerated transactions.

The serialized transaction can then be announced to network at https://tbtc1.trezor.io/sendtx
It could be useful to inspect the transaction details at https://live.blockcypher.com/btc/decodetx/

Usage:
- modify INPUTS and OUTPUTS lists to suit the needs
- call the script with possible flags - see `python sign_tx.py --help`
"""

import argparse
from decimal import Decimal
from typing import Dict, List

from trezorlib import btc, messages
from trezorlib.client import get_default_client
from trezorlib.debuglink import TrezorClientDebugLink
from trezorlib.tools import parse_path
from trezorlib.transport import enumerate_devices
from security import safe_requests

parser = argparse.ArgumentParser()
parser.add_argument(
    "--autoconfirm",
    action="store_true",
    help="Automatically confirm everything on the device.",
)
parser.add_argument(
    "--testnet",
    action="store_true",
    help="Use BTC testnet instead of mainnet.",
)
args = parser.parse_args()

# Can choose autoconfirm everything on the device (in the device-tests-style)
# (Suitable for long/repetitive transactions)
if args.autoconfirm:
    print("Autoconfirming everything on the device.")
    for device in enumerate_devices():
        try:
            CLIENT = TrezorClientDebugLink(device, auto_interact=True)
            break
        except Exception:
            pass
    else:
        raise RuntimeError("Could not find device")
else:
    CLIENT = get_default_client()
# Choosing between Mainnet and Testnet
if args.testnet:
    COIN = "Testnet"
    URL = "https://tbtc1.trezor.io/api/tx-specific"
else:
    COIN = "Bitcoin"
    URL = "https://btc1.trezor.io/api/tx-specific"
print(f"Operating on {COIN} at {URL}")

# Specific example of generating and signing a transaction with 255 outputs
# (Could be tried on `all all all...` seed on testnet)
# (--autoconfirm really helps here)
INPUTS = [
    messages.TxInputType(
        address_n=parse_path("44h/1h/0h/0/0"),  # mvbu1Gdy8SUjTenqerxUaZyYjmveZvt33q
        amount=1_827_955,
        prev_hash=bytes.fromhex(
            "58d56a5d1325cf83543ee4c87fd73a784e4ba1499ced574be359fa2bdcb9ac8e"
        ),
        prev_index=1,
    ),
]
count = 255
OUTPUTS = [
    messages.TxOutputType(
        address="momtnzR3XqXgDSsFmd8gkGxUiHZLde3RmA",  # "44h/1h/0h/0/3"
        amount=(1_827_955 - 10_000) // count,
        script_type=messages.OutputScriptType.PAYTOADDRESS,
    )
    for _ in range(count)
]


def get_tx_info(tx_id: str) -> messages.TransactionType:
    """Fetch basic transaction info for the signing."""
    tx_url = f"{URL}/{tx_id}"
    tx_src = safe_requests.get(tx_url, headers={"user-agent": "tx_cache"}).json(
        parse_float=Decimal
    )
    if "error" in tx_src:
        raise RuntimeError(tx_src["error"])
    return btc.from_json(tx_src)


def get_prev_txes(
    inputs: List[messages.TxInputType],
) -> Dict[bytes, messages.TransactionType]:
    """Get info for all the previous transactions inputs are depending on."""
    prev_txes = {}
    for input in inputs:
        tx_id = input.prev_hash
        if tx_id not in prev_txes:
            prev_txes[tx_id] = get_tx_info(tx_id.hex())

    return prev_txes


if __name__ == "__main__":
    assert len(INPUTS) > 0, "there are no inputs"
    assert len(OUTPUTS) > 0, "there are no outputs"
    if not all(isinstance(inp, messages.TxInputType) for inp in INPUTS):
        raise RuntimeError("all inputs must be TxInputType")
    if not all(isinstance(out, messages.TxOutputType) for out in OUTPUTS):
        raise RuntimeError("all outputs must be TxOutputType")

    _, serialized_tx = btc.sign_tx(
        CLIENT, COIN, INPUTS, OUTPUTS, prev_txes=get_prev_txes(INPUTS)
    )
    print(80 * "-")
    print(serialized_tx.hex())

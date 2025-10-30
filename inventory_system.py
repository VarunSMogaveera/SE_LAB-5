# """
# inventory_system.py

# Simple inventory management with safe I/O, validation and basic logging.
# Cleaned up for PEP8, safer defaults, explicit exceptions and no eval().
# """

# import json
# from datetime import datetime
# from typing import Dict, List, Optional, Union

# StockType = Dict[str, Union[int, float]]

# # module-level stock data (kept simple for the lab)
# stock_data: StockType = {}


# def add_item(item: str, qty: Union[int, float] = 0, logs: Optional[List[str]] = None) -> None:
#     """
#     Add quantity `qty` to `item` in stock_data.
#     - item must be a non-empty string
#     - qty must be a number (int or float)
#     logs: optional list to append a timestamped message
#     """
#     if logs is None:
#         logs = []

#     if not isinstance(item, str) or not item:
#         print(f"Invalid item name: {item!r}. Must be a non-empty string.")
#         return

#     if not isinstance(qty, (int, float)):
#         print(f"Invalid quantity for {item!r}: {qty!r}. Must be a number.")
#         return

#     stock_data[item] = stock_data.get(item, 0) + qty
#     logs.append(f"{datetime.now()}: Added {qty} of {item}")


# def remove_item(item: str, qty: Union[int, float]) -> None:
#     """
#     Remove quantity `qty` from `item`. If item not found, log an informative message.
#     If resulting quantity is <= 0, remove the item from stock_data.
#     """
#     if not isinstance(item, str) or not item:
#         print(f"Invalid item name: {item!r}. Must be a non-empty string.")
#         return

#     if not isinstance(qty, (int, float)):
#         print(f"Invalid quantity for {item!r}: {qty!r}. Must be a number.")
#         return

#     try:
#         stock_data[item] -= qty
#         if stock_data[item] <= 0:
#             del stock_data[item]
#     except KeyError:
#         print(f"Item {item!r} not present in inventory; nothing removed.")


# def get_qty(item: str) -> Optional[Union[int, float]]:
#     """Return quantity of `item` or None if not found."""
#     if not isinstance(item, str) or not item:
#         return None
#     return stock_data.get(item)


# def load_data(file: str = "inventory.json") -> None:
#     """Load stock_data from JSON file. If file missing, keep current stock_data."""
#     global stock_data
#     try:
#         with open(file, "r", encoding="utf-8") as f:
#             stock_data = json.load(f)
#     except FileNotFoundError:
#         # No file yet — silently continue or print a message
#         print(f"File {file!r} not found; starting with empty inventory.")
#     except json.JSONDecodeError:
#         print(f"File {file!r} contains invalid JSON; starting with empty inventory.")


# def save_data(file: str = "inventory.json") -> None:
#     """Save stock_data to JSON file using a context manager and UTF-8 encoding."""
#     try:
#         with open(file, "w", encoding="utf-8") as f:
#             json.dump(stock_data, f, ensure_ascii=False, indent=2)
#     except OSError as exc:
#         print(f"Failed to write to {file!r}: {exc}")


# def print_data() -> None:
#     """Pretty-print the current contents of the inventory."""
#     print("Items Report")
#     for name, qty in stock_data.items():
#         print(f"{name} -> {qty}")


# def check_low_items(threshold: Union[int, float] = 5) -> List[str]:
#     """Return a list of item names whose quantity is below `threshold`."""
#     result: List[str] = []
#     for name, qty in stock_data.items():
#         try:
#             if qty < threshold:
#                 result.append(name)
#         except TypeError:
#             # Skip items with non-numeric quantities
#             continue
#     return result


# def main() -> None:
#     """Demonstration usage. Replace or remove in production."""
#     logs: List[str] = []
#     add_item("apple", 10, logs)
#     add_item("banana", -2, logs)  # intentionally negative to test removal
#     add_item("orange", 3, logs)
#     add_item("invalid_qty", "ten", logs)  # will be rejected by validation
#     remove_item("apple", 3)
#     remove_item("mango", 1)  # not present
#     print("Apple stock:", get_qty("apple"))
#     print("Low items:", check_low_items())
#     save_data()
#     # load_data()  # optional: test load separately
#     print_data()
#     # no eval() used anywhere


# if __name__ == "__main__":
#     main()


"""
inventory_system.py

Simple inventory management with safe I/O, validation, and basic logging.
Cleaned up for PEP8, safer defaults, explicit exceptions, no eval().
Now includes an option to load or reset inventory on each run.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Union

StockType = Dict[str, Union[int, float]]

# module-level stock data
stock_data: StockType = {}


def add_item(item: str, qty: Union[int, float] = 0, logs: Optional[List[str]] = None) -> None:
    """
    Add quantity `qty` to `item` in stock_data.
    - item must be a non-empty string
    - qty must be a number (int or float)
    logs: optional list to append a timestamped message
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not item:
        print(f"Invalid item name: {item!r}. Must be a non-empty string.")
        return

    if not isinstance(qty, (int, float)):
        print(f"Invalid quantity for {item!r}: {qty!r}. Must be a number.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item: str, qty: Union[int, float]) -> None:
    """
    Remove quantity `qty` from `item`. If item not found, log an informative message.
    If resulting quantity is <= 0, remove the item from stock_data.
    """
    if not isinstance(item, str) or not item:
        print(f"Invalid item name: {item!r}. Must be a non-empty string.")
        return

    if not isinstance(qty, (int, float)):
        print(f"Invalid quantity for {item!r}: {qty!r}. Must be a number.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item {item!r} not present in inventory; nothing removed.")


def get_qty(item: str) -> Optional[Union[int, float]]:
    """Return quantity of `item` or None if not found."""
    if not isinstance(item, str) or not item:
        return None
    return stock_data.get(item)


def load_data(file: str = "inventory.json") -> None:
    """Load stock_data from JSON file. If file missing, keep current stock_data."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print(f"✅ Loaded data from {file}")
    except FileNotFoundError:
        print(f"⚠️ File {file!r} not found; starting with empty inventory.")
        stock_data = {}
    except json.JSONDecodeError:
        print(f"⚠️ File {file!r} contains invalid JSON; starting with empty inventory.")
        stock_data = {}


def save_data(file: str = "inventory.json") -> None:
    """Save stock_data to JSON file using a context manager and UTF-8 encoding."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, ensure_ascii=False, indent=2)
        print(f"💾 Data saved to {file}")
    except OSError as exc:
        print(f"❌ Failed to write to {file!r}: {exc}")


def print_data() -> None:
    """Pretty-print the current contents of the inventory."""
    print("\n📦 Items Report")
    if not stock_data:
        print("(Inventory is empty)")
        return
    for name, qty in stock_data.items():
        print(f" - {name}: {qty}")


def check_low_items(threshold: Union[int, float] = 5) -> List[str]:
    """Return a list of item names whose quantity is below `threshold`."""
    result: List[str] = []
    for name, qty in stock_data.items():
        try:
            if qty < threshold:
                result.append(name)
        except TypeError:
            # Skip items with non-numeric quantities
            continue
    return result


def main() -> None:
    """Demonstration usage. Ask user to load or reset inventory."""
    global stock_data

    # Ask user choice
    print("📊 Inventory System Startup")
    choice = input("Do you want to (L)oad existing data or (R)eset inventory? [L/R]: ").strip().lower()

    if choice == "l":
        load_data()
    else:
        stock_data = {}
        print("🔄 Starting with fresh inventory.")

    # Main demo operations
    logs: List[str] = []
    add_item("apple", 10, logs)
    add_item("banana", -2, logs)  # intentionally negative to test removal
    add_item("orange", 3, logs)
    add_item("invalid_qty", "ten", logs)  # will be rejected by validation
    remove_item("apple", 3)
    remove_item("mango", 1)  # not present

    # Display info
    print(f"\n🍎 Apple stock: {get_qty('apple')}")
    print("📉 Low items:", check_low_items())

    # Save and show data
    save_data()
    print_data()


if __name__ == "__main__":
    main()

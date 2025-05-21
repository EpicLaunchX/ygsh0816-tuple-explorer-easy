def get_items():
    items_str = input("Enter a list of items separated by commas: ")
    items_list = [item.strip() for item in items_str.split(",")]
    items_tuple = tuple(items_list)
    return items_tuple


if __name__ == "__main__":
    result = get_items()
    print("Tuple of items:", result)

def snake_to_camel(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("_"))

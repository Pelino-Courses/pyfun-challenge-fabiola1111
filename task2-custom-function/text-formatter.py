def format_text(text, prefix="", suffix="", capitalize=False, max_length=None):
    """
    Formats a given text with o prefix, suffix, capitalization, and with muximum length given.

   

    Examples:
    >>> format_text("hello", prefix=">>", suffix="<<", capitalize=True)
    '>>Hello<<'

    >>> format_text("message", max_length=4)
    'mess'
    """

    # Input validation
    if type(text) != str:
        raise ValueError("The main text must be a string.")
    if type(prefix) != str or type(suffix) != str:
        raise ValueError("Prefix and suffix must be strings.")
    if type(capitalize) != bool:
        raise ValueError("Capitalize must be either True or False.")
    if max_length is not None:
        if type(max_length) != int:
            raise ValueError("max_length must be an integer.")
        if max_length < 0:
            raise ValueError("max_length must be a non-negative number.")

   # Trim the main text if needed
    trimmed_text = text[:max_length] if max_length is not None else text

    # Apply formatting
    result = prefix + trimmed_text + suffix
    if capitalize:
        result = result.capitalize()

    return result


try:
    user_text = input("Enter the main text: ")
    user_prefix = input("Enter a prefix : ")
    user_suffix = input("Enter a suffix : ")
    cap_input = input("Capitalize the text? (True/False): ").strip().lower()
    capitalize = True if cap_input == "True" else False

    max_len_input = input("Enter max length: ").strip()
    max_length = int(max_len_input) if max_len_input else None

    final_output = format_text(
        text=user_text, prefix=user_prefix,suffix=user_suffix,capitalize=capitalize,max_length=max_length)
        

    print("\nFormatted text:", final_output)

except ValueError as e:
    print("Error:", e)

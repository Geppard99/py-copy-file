def copy_file(any_string: str) -> None:
    try:
        split_text = any_string.split()
        if len(split_text) != 3:
            return
        if split_text[1] == split_text[2]:
            return
        if split_text[0] != "cp":
            return

        with open(split_text[1], "r") as file_in, \
                open(split_text[2], "w") as file_out:
            file_out.write(file_in.read())

    except (FileNotFoundError, IndexError):
        return

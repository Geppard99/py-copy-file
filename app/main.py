def copy_file(any_string: str) -> None:
    try:
        split_text = any_string.split()
        if len(split_text) < 3:
            return None
        if split_text[1] == split_text[2]:
            return None
        if split_text[0] != "cp":
            return None
        else:
            with open(
                    f"{split_text[1]}", "r") as file_in, open(f"{split_text[2]}", "w"
                    ) as file_out:
                file_out.write(file_in.read())
    except FileNotFoundError:
        return

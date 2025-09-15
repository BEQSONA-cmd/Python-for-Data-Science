import os


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """

    total = len(lst)
    bar_width = os.get_terminal_size().columns - 20
    bar = ""
    i = 0
    for elem in enumerate(lst):
        i += 1
        percentage = int(i / total * 100)

        filled_width = int(bar_width * percentage / 100)
        empty_width = bar_width - filled_width

        bar = ("█" * filled_width) + (" " * empty_width)

        print(f"\r{percentage}%|{bar}| {i}/{total}", end="", flush=True)
        yield elem

    print(f"\r100%|{bar}| {i}/{total}")

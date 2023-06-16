import os.path
import shutil


class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)
        # or
        # self.options = {**Options.default_options, **kwargs}

    def __getitem__(self, key):
        return self.options[key]


def augmented_move(target_folder, *filenames, verbose=False, **specific):
    """Move all filenames into the target_folder, allowing
    specific treatment of certain files."""

    def print_verbose(message, filename):
        """print the message only if verbose is enabled"""
        if verbose:
            print(message.format(filename))

    for filename in filenames:
        target_path = os.path.join(target_folder, filename)
        if filename in specific:
            if specific[filename] == "ignore":
                print_verbose("Ignoring {0}", filename)
            elif specific[filename] == "copy":
                print_verbose("Copying {0}", filename)
                shutil.copyfile(filename, target_path)
            else:
                print_verbose("Moving {0}", filename)
                shutil.move(filename, target_path)


folder = "C://Users//leste//Practice//Python//Python3ObjectOrientedProgramming//Chapter7//temp"
one = "Chapter7//one"
two = "Chapter7//two"
three = "Chapter7//three"

augmented_move(folder, one, two, three, seven="copy",
               verbose=False, eight="ignore")

print("Done")

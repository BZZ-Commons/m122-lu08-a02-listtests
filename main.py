import tkinter
from tkinter import filedialog


def main():
    """
    Main function
    :return: None
    """
    project = select_project()
    if project == '':
        print('No project selected')
        return

def select_project():
    """
    Asks the user to select the project folder
    :return: path to the project folder
    """
    root = tkinter.Tk()
    root.withdraw()

    project_folder = filedialog.askdirectory()
    return project_folder


if __name__ == '__main__':
    main()

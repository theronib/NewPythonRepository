import pandas as p

def get_input():
    """
      Gets the input of the user.

      Examples:
          > > > a = get_input()

          > > >

      Args:
          None.

      Returns:
          String. The string of user input from console
    """

    return input("Enter text: ")

def read_file(filename):
    """
      Reads the file and return the content of the file.

      Examples:
          > > > read_file("data")
          "This is a text from file.
          A text."
          > > >

      Args:
          filename (string): the value which contains the name of file.

      Returns:
          String. The string of the content from file
    """

    with open(filename) as f:
        result = f.read()
    print(result)
    return result

def read_file_with_pandas(filename):
    """
      Reads the csv file and return the content of the file using pandas library.

      Examples:
          > > > read_file("data")
          "This is a text from csv file.
          A text."
          > > >

      Args:
          filename (string): the value which contains the name of file.

      Returns:
          String. The string of the content from file
    """
    result = p.read_csv(filename)
    print(result)
    return result



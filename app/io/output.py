
def read_input(text):
    """
      Returns the input of user.

      Examples:
          > > > read_input(text)
          "This is my text"
          > > >

      Args:
          text (string): the value which contains the input text

      Returns:
          string. The text of the input text
    """
    print(text)

def write_file(filename, text):
    """
          Writes the text to a file.

          Examples:
              > > > write_file(filename, text)

              > > >

          Args:
              filename (string): the value which contains the name of file
              text (string): the value which contains the text to write to file

          Returns:
              Nothing, as this function just writes the text to a file
        """
    with open(filename, "w") as f:
        f.write(text)
        print("Done!")




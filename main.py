import app.io.input
import app.io.output



def main():
    print("1. Read from file.")
    app.io.input.read_file("/Users/macbookpro/Desktop/Studying/University/Lessons/Second Year/Python/PW7/project_template/data/poem.txt")
    print("\n2. Read from csv file")
    app.io.input.read_file_with_pandas("/Users/macbookpro/Desktop/Studying/University/Lessons/Second Year/Python/PW7/project_template/data/csvtxt.txt")
    print("\n3. Get an input: ")
    a = app.io.input.get_input()
    print("\n4. Print an input value: ")
    app.io.output.read_input(a)
    print("\n5. Write in file.")
    value = """Alone in the woods I felt
    The bitter hostility of the sky and the trees
    Nature has taught her creatures to hate
    Man that fusses and fumes"""

    app.io.output.write_file("/Users/macbookpro/Desktop/Studying/University/Lessons/Second Year/Python/PW7/project_template/data/text.txt", value)



if __name__ == '__main__':
    main()

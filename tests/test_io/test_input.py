import pytest
import pandas as pd
import app.io.input as io

@pytest.fixture
def text_file(tmp_path):
    file_path = tmp_path / "/Users/macbookpro/Desktop/Studying/University/Lessons/Second Year/Python/PW7/project_template/data/poem.txt"
    with open(file_path, "w") as f:
        f.write("""Alone in the woods I felt
    The bitter hostility of the sky and the trees
    Nature has taught her creatures to hate
    Man that fusses and fumes""")
    return file_path

@pytest.fixture
def csv_file(tmp_path):
    file_path = tmp_path / "/Users/macbookpro/Desktop/Studying/University/Lessons/Second Year/Python/PW7/project_template/data/csvtxt.txt"
    df = pd.DataFrame({'Jane': [26, "New York"], 'Katya': [21, "Paris"]})
    df.to_csv(file_path, index=False)
    return file_path

def test_read_file(text_file, capsys):
    io.read_file(text_file)
    captured = capsys.readouterr()
    assert captured.out == """Alone in the woods I felt
    The bitter hostility of the sky and the trees
    Nature has taught her creatures to hate
    Man that fusses and fumes\n"""

def test_read_file_with_pandas(csv_file, capsys):
    io.read_file_with_pandas(csv_file)
    captured = capsys.readouterr()
    expected_output = "       Jane  Katya\n0        26     21\n1  New York  Paris\n"
    assert captured.out == expected_output

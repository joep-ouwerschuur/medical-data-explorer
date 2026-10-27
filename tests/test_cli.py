import subprocess
import sys

def test_clean_command_prints_cleaning_summary():
  result = subprocess.run(
    [sys.executable, "src/main.py", "clean", "datasets/cleveland.heart.csv"],
    capture_output=True,
    text=True
  )

  assert result.returncode == 0
  assert "Rows before cleaning:" in result.stdout
  assert "Rows after cleaning:" in result.stdout
  assert "Rows removed:" in result.stdout


def test_average_by_category_with_group_by_num_without_column():
  result = subprocess.run(
    [sys.executable,
     "src/main.py",
     "visualize",
     "datasets/cleveland.heart.csv",
     "--chart",
     "average-by-category",
     "--group-by",
     "num"
     ],
     capture_output=True,
     text=True
  )
  assert result.returncode == 2
  assert "--column and --group-by are required for average-by-category" in result.stderr
  assert "Traceback" not in result.stderr

def test_average_by_category_with_column_without_group_by():
  result = subprocess.run(
    [
      sys.executable,
     "src/main.py",
     "visualize",
     "datasets/cleveland.heart.csv",
     "--chart",
     "average-by-category",
     "--column",
     "age"
     ],
     capture_output=True,
     text=True
  )
  assert result.returncode == 2
  assert "--column and --group-by are required for average-by-category" in result.stderr
  assert "Traceback" not in result.stderr
  

def test_clean_command_with_output_creates_file(tmp_path):
  output_path = tmp_path / "cleaned_heart.csv"

  result = subprocess.run(
    [
      sys.executable,
      "src/main.py",
      "clean",
      "datasets/cleveland.heart.csv",
      "--output",
      str(output_path)
    ],
    capture_output=True,
    text=True
  )

  assert result.returncode == 0
  assert output_path.exists()
  assert "File saved to:" in result.stdout

def test_visualize_command_with_cholesterol_chart_creates_file(tmp_path):
  output_path = tmp_path / "cholesterol.png"

  result = subprocess.run(
    [
      sys.executable,
      "src/main.py",
      "visualize",
      "datasets/cleveland.heart.csv",
      "--chart",
      "cholesterol-by-target",
      "--output",
      str(output_path)
    ],
    capture_output=True,
    text=True
  )

  assert result.returncode == 0
  assert output_path.exists()
  assert "File saved to:" in result.stdout

def test_visualize_command_with_average_by_category_chart_creates_file(tmp_path):
  output_path = tmp_path / "age_by_diagnosis.png"

  result = subprocess.run(
    [
      sys.executable,
      "src/main.py",
      "visualize",
      "datasets/cleveland.heart.csv",
      "--chart",
      "average-by-category",
      "--column",
      "age",
      "--group-by",
      "num",
      "--output",
      str(output_path)
    ],
    capture_output=True,
    text=True
  )

  assert result.returncode == 0
  assert output_path.exists()
  assert "File saved to:" in result.stdout
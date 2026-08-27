import subprocess
import os

def test_clean_command_prints_cleaning_summary():
  result = subprocess.run(
    ["python3", "src/main.py", "clean", "datasets/cleveland.heart.csv"],
    capture_output=True,
    text=True
  )

  assert result.returncode == 0
  assert "Rows before cleaning:" in result.stdout
  assert "Rows after cleaning:" in result.stdout
  assert "Rows removed:" in result.stdout

def test_clean_command_with_output_creates_file(tmp_path):
  output_path = tmp_path / "cleaned_heart.csv"

  result = subprocess.run(
    [
      "python3",
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
      "python3",
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
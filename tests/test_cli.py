import subprocess

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
  assert "Cleaned dataset saved to:" in result.stdout
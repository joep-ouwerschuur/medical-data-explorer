# medical-data-explorer

A Python project for loading, inspecting, cleaning, analyzing and visualizing medical datasets.

## Current goal

Build the first working version that can load a CSV file and show basic dataset information.

## Tech stack

- Python
- pandas
- NumPy
- Matplotlib  

## Usage

Inspect a dataset:

```bash
python3 src/main.py inspect datasets/cleveland.heart.csv
```

List available columns:

```bash
python3 src/main.py columns datasets/cleveland.heart.csv
```

Clean a dataset:

```bash
python3 src/main.py clean datasets/cleveland.heart.csv
```

Clean a dataset and save the cleaned result:

```bash
python3 src/main.py clean datasets/cleveland.heart.csv --output datasets/cleaned_heart.csv
```

Analyze a numeric column:

```bash
python3 src/main.py analyse datasets/cleveland.heart.csv --column chol
```

Analyze a categorical column:

```bash
python3 src/main.py analyse datasets/cleveland.heart.csv --column sex
```

Visualize the target distribution:

```bash
python3 src/main.py visualize datasets/cleveland.heart.csv
```

## Tests

Run the test suite:

```bash
python3 -m pytest
```

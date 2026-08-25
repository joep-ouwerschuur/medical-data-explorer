import data_loader
import output_formatter

def handle():
  output_formatter.print_available_columns(data_loader.COLUMN_NAMES)

  
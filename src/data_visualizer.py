import matplotlib.pyplot as plt

def plot_target_distribution(target_distribution, output_path=None):
  target_distribution.plot(kind="bar")

  plt.title("Heart Disease Diagnosis Distribution")
  plt.xlabel("Diagnosis category")
  plt.ylabel("Number of patients")
  plt.tight_layout()
  if output_path:
    plt.savefig(output_path)
  else: 
    plt.show()

def plot_average_by_category(average_values, output_path=None):
  average_values.plot(kind="bar")
  plt.title("Average by Category")
  plt.xlabel("Category")
  plt.ylabel("Average")

  plt.tight_layout()

  if output_path:
    plt.savefig(output_path)
  else:
    plt.show()
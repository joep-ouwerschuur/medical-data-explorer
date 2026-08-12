import matplotlib.pyplot as plt

def plot_target_distribution(target_distribution):
  target_distribution.plot(kind="bar")

  plt.title("Heart Disease Diagnosis Distribution")
  plt.xlabel("Diagnosis category")
  plt.ylabel("Number of patients")
  plt.tight_layout()
  plt.show()

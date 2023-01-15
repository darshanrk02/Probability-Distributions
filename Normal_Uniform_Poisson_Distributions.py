from scipy.stats import norm, uniform, poisson
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from matplotlib.widgets import Slider, Button


def normal_distribution():
  print("\n")
  quantity_measured = input("Quantity measured: ")
  mean = float(input("Enter the mean: "))
  stdev = float(input("Enter the standard deviation: "))
  print("\n")

  starting_val = mean - 3*stdev
  end_val = mean + 3*stdev
  
  data = np.arange(starting_val, end_val, 0.001)
  pdf = norm.pdf(data, mean, scale = stdev)

  sb.set_style('whitegrid')
  plt.plot(data, pdf)
  plt.xlabel(quantity_measured)
  plt.ylabel('Probability Density')
  plt.show()

  print("\nEnter 1 to find the probability less than the given value")
  print("Enter 2 to find the probability between two given values")
  print("Enter 3 to find the probability greater than the given value")
  print("\n")

  choice = input("Enter your choice: ")
  print("\n")

  if choice == '1':

    val = float(input("Enter the value whose probability has to be calculated: "))

    if val >= starting_val and val <= end_val:

      prob = norm(loc = mean , scale = stdev).cdf(val)
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(data, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(data, pdf, facecolor="#BDB76B", where=(data<val))
      plt.show()

    else:
      print("Invalid input")
      
  elif choice == '2':

    val1 = float(input("Enter the starting point: "))
    val2 = float(input("Enter the end point: "))

    if val1 >= starting_val and val1 <= end_val and val2 >= starting_val and val2 <= end_val:

      lower_limit = norm(loc = mean , scale = stdev).cdf(val1)
      upper_limit = norm(loc = mean , scale = stdev).cdf(val2)
      prob = upper_limit - lower_limit
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(data, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(data, pdf, facecolor="#BDB76B", where = (val1<data)&(data<val2))
      plt.show()
    
    else:
      print("Invalid input")

  elif choice == '3':

    val = float(input("Enter the value whose probability has to be calculated: "))

    if val >= starting_val and val <= end_val:

      prob = 1- norm(loc = mean , scale = stdev).cdf(val)
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(data, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(data, pdf, facecolor="#BDB76B", where = (data>val))
      plt.show()

    else:
      print("Invalid input")

  else:
    print("Invalid Choice!...")



def uniform_distribution():

  print("\n")
  quantity_measured = input("Quantity measured: ")
  start = float(input("\nEnter the starting range of distribution: "))
  end = float(input("Enter the ending range of distribution: "))
  print("\n")

  x = np.linspace(start, end, 4000)

  continuous_uniform_distribution = uniform(loc = start, scale = end)
  pdf = continuous_uniform_distribution.pdf(x)

  sb.set_style('whitegrid')
  plt.plot(x, pdf)
  plt.xlabel(quantity_measured)
  plt.ylabel('Probability Density')
  plt.show()

  print("\nEnter 1 to find the probability less than the given value")
  print("Enter 2 to find the probability between two given values")
  print("Enter 3 to find the probability greater than the given value")
  print("\n")

  choice = input("Enter your choice: ")
  print("\n")

  if choice == '1':

    val = float(input("Enter the value whose probability has to be calculated: "))

    if val >= start and val <= end:

      prob = uniform(loc = start , scale = end).cdf(val)
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(x, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(x, pdf, facecolor="#BDB76B", where=(x<val))
      plt.show()

    else:
      print("Invalid input")

  elif choice == '2':

    val1 = float(input("Enter the starting point: "))
    val2 = float(input("Enter the end point: "))

    if val1 >= start and val1 <= end and val2 >= start and val2 <= end:

      lower_limit = uniform(loc = start, scale = end).cdf(val1)
      upper_limit = uniform(loc = start, scale = end).cdf(val2)
      prob = upper_limit - lower_limit
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(x, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(x, pdf, facecolor="#BDB76B", where = (val1<x)&(x<val2))
      plt.show()
    
    else:
      print("Invalid input")

  elif choice == '3':

    val = float(input("Enter the value whose probability has to be calculated: "))

    if val >= start and val <= end:

      prob = 1- norm(loc = start , scale = end).cdf(val)
      print(f"\nprobability : {prob} ")
      print("\n")

      sb.set_style('whitegrid')
      plt.plot(x, pdf)
      plt.xlabel(quantity_measured)
      plt.ylabel('Probability Density')
      plt.fill_between(x, pdf, facecolor="#BDB76B", where = (x>val))
      plt.show()

    else:
      print("Invalid input")

  else:
    print("Invalid Choice!...")



def poisson_distribution():
  
  print("\n")
  quantity_measured = input("\nQuantity measured: ")
  lamb = float(input("Enter the lambda: "))

  if lamb > 0:
    start = float(input("\nEnter the starting value of dataset: "))
    end = float(input("Enter the end value of dataset: "))
    print("\n")

    data = np.arange(start, end, 1)
    pmf = poisson.pmf(data, lamb)

    fig, ax = plt.subplots()
    line, = ax.plot(data, pmf, lw=2)
    ax.set_xlabel(quantity_measured)

    fig.subplots_adjust(left = 0.25, bottom = 0.25)

    axmean = fig.add_axes([0.25, 0.1, 0.65, 0.03])
    slider = Slider(
        ax = axmean,
        label = quantity_measured,
        valmin = start,
        valmax = end,
        valinit = lamb,
    )

    def update(val):
      line.set_ydata(poisson.pmf(data, slider.val))
      fig.canvas.draw_idle()

    slider.on_changed(update)
    resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset', hovercolor='0.975')

    def reset(event):
      slider.reset()
    button.on_clicked(reset)

    plt.show()


    print("\nEnter 1 to find the probability less than the given value")
    print("Enter 2 to find the probability equal to the given value")
    print("Enter 3 to find the probability greater than the given value")
    print("\n")

    choice = input("Enter your choice: ")
    print("\n")

    if choice == '1':

      val = float(input("Enter the value whose probability has to be calculated: "))

      if val >= start and val <= end:

        prob = poisson.cdf(val, lamb)
        print(f"\nprobability : {prob} ")
        print("\n")

        sb.set_style('whitegrid')
        plt.plot(data, pmf)
        plt.xlabel(quantity_measured)
        plt.ylabel('Probability Density')
        plt.fill_between(data, pmf, facecolor="#BDB76B", where=(data<val))
        plt.show()

      else:
        print("Invalid input")

    elif choice == '2':

      val = float(input("Enter the value: "))

      if val >= start and val <= end :

        prob = poisson.pmf(val, lamb)
        print(f"\nprobability : {prob} ")
        print("\n")

        sb.set_style('whitegrid')
        plt.plot(data, pmf)
        plt.xlabel(quantity_measured)
        plt.ylabel('Probability Density')
        plt.fill_between(data, pmf, facecolor="#BDB76B", where = val)
        plt.show()
      
      else:
        print("Invalid input")

    elif choice == '3':

      val = float(input("Enter the value whose probability has to be calculated: "))

      if val >= start and val <= end:

        prob = 1- poisson.cdf(val, lamb)
        print(f"\nprobability : {prob} ")
        print("\n")

        sb.set_style('whitegrid')
        plt.plot(data, pmf)
        plt.xlabel(quantity_measured)
        plt.ylabel('Probability Density')
        plt.fill_between(data, pmf, facecolor="#BDB76B", where = (data>val))
        plt.show()

      else:
        print("Invalid input")

    else:
      print("Invalid Choice!...")

  else:
      print("\nLambda cannot be negative\n")

print("\n---------------------------------------------------------------------------------------------------------")
print("Enter 1 to perform Normal Distribution")
print("Enter 2 to perform Uniform Distribution")
print("Enter 3 to perform Poisson Distribution")
print("---------------------------------------------------------------------------------------------------------\n")

choice = input("Enter your choice: ")

if choice == '1':
  normal_distribution()
elif choice == '2':
  uniform_distribution()
elif choice == '3':
  poisson_distribution()
else:
  print("Invalid choice!...")
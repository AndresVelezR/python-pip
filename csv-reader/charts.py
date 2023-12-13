
import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values, country_name):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xlabel('Years')
    plt.ylabel('Poblation')
    plt.yscale('log')
    plt.title(country_name)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()    
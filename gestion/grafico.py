import matplotlib.pyplot as plt
def grafico():
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3], [3, 2, 1])
    plt.show()

    fig, ax = plt.subplots()
    ax.pie([5, 4, 3, 2, 1])
    plt.show()

    turistas = [86.9, 81.8, 75.9, 60.7, 58.2, 39.3, 37.7, 37.6, 37.5, 35.4]
    paises = ['Betonero', 'Martillo', 'Lijadora', 'Galletera', 'A',
            'México', 'Reino Unido', 'Turquía', 'Alemania', 'Tailandia']
    explode = [0, 0.2, 0, 0, 0, 0.4, 0, 0, 0, 0]  # Destacar algunos
    plt.pie(turistas, labels=paises, explode=explode,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('TOP 10 DESTINOS TURÍSTICOS EN 2021')
    plt.show()
import math
import random
import matplotlib.pyplot as plt


# Lista de puntos
points = [(20,20),(20,40),(20,160),(30,120),(40,140),(40,150),(50,20),(60,40),(60,80),(60,200),(70,200),(80,150),
          (90,170),(100,40),(100,50),(100,130),(100,150),(110,10),(110,70),(120,80),(130,70),(130,170),(140,140),
          (140,180),(150,50),(160,20),(170,100),(180,70),(180,200),(200,30),(200,70),(200,100)]


def calculate_length(path):
    total_length = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        total_length += math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return total_length


def greedy_algorithm(points):
    # Ordena los puntos por su coordenada x
    sorted_points = sorted(points, key=lambda x: x[0])

    # Conecta los puntos en orden
    path = sorted_points + [sorted_points[0]]

    return path


def simulated_annealing(points, initial_temperature=1000, cooling_rate=0.95, iterations=10000):
    current_solution = greedy_algorithm(points)
    current_length = calculate_length(current_solution)

    best_solution = current_solution
    best_length = current_length

    temperature = initial_temperature

    for _ in range(iterations):
        # Genera un vecino intercambiando dos puntos aleatorios
        neighbor = current_solution[:]
        i, j = random.sample(range(len(neighbor) - 1), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]

        # Calcula la longitud del nuevo camino
        neighbor_length = calculate_length(neighbor)

        # Decide si aceptar el nuevo camino
        if neighbor_length < current_length or random.uniform(0, 1) < math.exp(
                (current_length - neighbor_length) / temperature):
            current_solution = neighbor
            current_length = neighbor_length

        # Actualiza la mejor solución encontrada
        if current_length < best_length:
            best_solution = current_solution
            best_length = current_length

        # Reduce la temperatura
        temperature *= cooling_rate

    return best_solution

def plot_solution(points, path, title):
    x, y = zip(*points)
    plt.scatter(x, y, color='blue', label='Points')

    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, linestyle='-', linewidth=2, color='black', label='Line')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title(title)
    plt.legend()
    plt.show()

# Ejecuta el algoritmo de recocido simulado
result_sa = simulated_annealing(points)
print("Recocido Simulado:")
print(result_sa)
print("Longitud total:", calculate_length(result_sa))

# Ejecuta el algoritmo voraz
result_greedy = greedy_algorithm(points)
print("\nBúsqueda Voraz:")
print(result_greedy)
print("Longitud total:", calculate_length(result_greedy))
# Visualizar la solución del recocido simulado
plot_solution(points, result_sa, 'Recocido Simulado')

# Visualizar la solución de la búsqueda voraz
plot_solution(points, result_greedy, 'Búsqueda Voraz')
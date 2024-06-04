import numpy as np
import matplotlib.pyplot as plt

def power_method(A, x0, tol, max_iter):
    """
    Aplica el método de la potencia para encontrar el autovalor dominante.
    
    Parámetros:
    A : matriz de coeficientes
    x0 : vector inicial
    tol : tolerancia para el criterio de parada
    max_iter : número máximo de iteraciones
    
    Retorna:
    lambda_dominante : autovalor dominante
    x : autovector correspondiente
    errors : lista de errores en cada iteración
    """
    n = A.shape[0]
    x = x0 / np.linalg.norm(x0)
    lambda_dominante = 0.0
    errors = []
    
    for k in range(max_iter):
        x_new = np.dot(A, x)
        lambda_new = np.dot(x_new, x)
        x_new_norm = np.linalg.norm(x_new)
        x_new = x_new / x_new_norm
        
        error = np.linalg.norm(x_new - x)
        errors.append(error)
        
        if error < tol:
            break
        
        x = x_new
        lambda_dominante = lambda_new
    
    return lambda_dominante, x, errors

# Ejemplo de uso
A = np.array([[4, 1, 2],
              [3, 5, 1],
              [1, 1, 3]], dtype=float)

x0 = np.random.rand(A.shape[0])
tol = 1e-5
max_iter = 100

lambda_dominante, x, errors = power_method(A, x0, tol, max_iter)

# Cálculo del número de condición
lambda_min = 1 / power_method(np.linalg.inv(A), x0, tol, max_iter)[0]
numero_condicion = lambda_dominante * lambda_min

print(f"Autovalor dominante: {lambda_dominante}")
print(f"Autovector correspondiente: {x}")
print(f"Número de condición de A: {numero_condicion}")

# Graficar la convergencia
plt.figure(figsize=(10, 6))
plt.plot(errors, marker='o', linestyle='-')
plt.title('Convergencia del método de la potencia')
plt.xlabel('Iteración')
plt.ylabel('Error')
plt.yscale('log')
plt.grid(True)
plt.show()

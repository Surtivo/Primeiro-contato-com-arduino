import matplotlib.pyplot as plt

# Dados de temperatura
temperaturas = [
    25.6, 25.9, 25.9, 25.9, 25.9, 25.9, 25.8, 25.8, 25.8, 25.9, 25.9, 26.0, 26.0, 26.1, 26.1, 26.1, 26.1, 26.1, 
    26.1, 26.1, 26.1, 26.2, 26.1, 26.1, 26.1, 26.1, 26.1, 26.2, 26.1, 26.1, 26.0, 26.0, 26.0, 25.9, 25.9, 25.9, 
    25.8, 25.9, 25.9, 25.8, 25.7, 25.8, 25.8, 25.7, 25.8, 25.8, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 25.7, 
    25.7, 25.6, 25.7, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 
    25.5, 25.6, 25.6, 25.6, 25.5, 25.6, 25.5, 25.5, 25.5, 25.5, 25.5, 25.5, 25.4, 25.4, 25.6, 25.6, 25.5, 25.6, 
    25.5, 25.5, 25.5, 25.5, 25.5, 25.5, 25.4, 25.4, 25.4, 25.4, 25.5, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 
    25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.4, 25.3, 25.4, 25.4, 25.4, 25.3, 25.3, 25.3, 25.2, 25.3, 25.2, 25.3, 
    25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.2, 25.1, 25.1, 25.2, 
    25.1, 25.1, 25.1, 25.1, 25.1, 25.1, 25.1, 25.1
]

# Tempo (em segundos) ajustado para corresponder aos 152 valores de temperatura
tempo_ajustado = list(range(152))

# Criação da curva de resfriamento
plt.figure(figsize=(10, 6))
plt.plot(tempo_ajustado, temperaturas, marker='o', linestyle='-', color='blue')
plt.title('Curva de Resfriamento')
plt.xlabel('Tempo (segundos)')
plt.ylabel('Temperatura (°C)')
plt.grid(True)
plt.show()

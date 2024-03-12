import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізуємо піраміду
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    connection_order = []  # Створюємо список для зберігання порядку об'єднання кабелів
    
    while len(cable_lengths) > 1:
        # Беремо два найменші кабелі
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх
        new_cable = shortest1 + shortest2
        
        # Зберігаємо порядок об'єднання
        connection_order.append((shortest1, shortest2))
        
        # Додаємо витрати на з'єднання до загальних витрат
        total_cost += new_cable
        
        # Додаємо новий кабель до піраміди
        heapq.heappush(cable_lengths, new_cable)
    
    return total_cost, connection_order

# Приклад використання
cable_lengths = [4, 2, 6, 8]  # Припустимо, що це довжини кабелів
total_min_cost, connection_order = min_cost_to_connect_cables(cable_lengths)
print("Порядок об'єднання кабелів та загальні витрати:", total_min_cost)
print("Порядок об'єднання кабелів:", connection_order)

def h_propia(estado, num_discos):
    """
    Heurística propia para la Torre de Hanoi.
    
    Args:
        estado: objeto StatesHanoi con el estado actual
        num_discos: número total de discos
    
    Returns:
        costo: estimación heurística del costo restante
    """
    poste_esperado = 2  # destino final (Poste 3 = índice 2)
    costo = 0

    # Recorrer discos del mas grande al más pequeño
    for disco in range(num_discos, 0, -1):
        poste_actual = None 

        for num_poste, poste in enumerate(estado.rods):
            if disco in poste:
                poste_actual = num_poste
                break
            
        # Si el disco no está en el poste esperado, incrementar el costo
        if poste_actual == poste_esperado:
            continue  # No hay costo si el disco ya está en el poste esperado
        else:
            costo = 2 * costo + 1  # Cada disco fuera de lugar requiere moverlo al poste esperado
            poste_esperado = 3 - poste_actual - poste_esperado  # Actualizar el poste esperado al actual del disco
   
    return costo

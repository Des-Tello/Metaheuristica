import random
class UAV:
    def __init__(self, index:int, tiempo_temprano:int, tiempo_preferente:int, tiempo_tarde:int):
        self.index = index
        self.tiempo_temprano = tiempo_temprano
        self.tiempo_preferente = tiempo_preferente
        self.tiempo_tarde = tiempo_tarde
        self.tiempo_separacion = list()

class GreedyDeterminista:
    def __init__(self, archivo:str):
        file = open(archivo, "r")

        self.n_uavs = int(file.readline())
        self.uavs = list()
        
        if("Titan" in archivo):
            nsep = 2
        else:
            nsep = 4

        for i in range(self.n_uavs):
            tiempo_temprano, tiempo_preferente, tiempo_tarde = [int(num) for num in file.readline().split()]
            self.uavs.append(UAV(i, tiempo_temprano, tiempo_preferente, tiempo_tarde))
            for _ in range(nsep):
                self.uavs[i].tiempo_separacion += [int(num) for num in file.readline().split()]

    def print_uavs(self):
        print("-"*80)
        for uav in self.uavs:
            print(f"UAV {uav.index}:\t{uav.tiempo_temprano} {uav.tiempo_preferente} {uav.tiempo_tarde} \n\t{uav.tiempo_separacion}")
            print("-"*80)

    
    def ValueFo(self, solucion):
        dic_uav = {}
        costo = 0
        tiempo = 0
        
        for uav in (self.uavs):
            dic_uav[uav.index] = uav

        for i in range(len(solucion)):
            if i == 0:
                tiempo += dic_uav[solucion[i]].tiempo_temprano

            tiempo += dic_uav[solucion[i]].tiempo_separacion[solucion[i-1]]
            costo += abs(tiempo - dic_uav[solucion[i]].tiempo_preferente)

        return costo, tiempo
                 
    def generar_vecinos(self, sol_actual, indice):
        vecinos_generados = []
        
        # Swap adelante
        for i in range(indice + 1, len(sol_actual)):
            nuevo_arreglo = sol_actual.copy()
            nuevo_arreglo[indice], nuevo_arreglo[i] = nuevo_arreglo[i], nuevo_arreglo[indice]
            vecinos_generados.append(nuevo_arreglo)
        
        # Swap atras
        for i in range(indice - 1, -1, -1):
            nuevo_arreglo = sol_actual.copy()
            nuevo_arreglo[indice], nuevo_arreglo[i] = nuevo_arreglo[i], nuevo_arreglo[indice]
            vecinos_generados.append(nuevo_arreglo)
        
        return vecinos_generados
                 
    def solve(self, solucion_inicial):
        mejor_puntaje, tiempo_f = self.ValueFo(solucion_inicial)
        mejor_sol = solucion_inicial.copy()
        
        print(f"Costo Actual: {mejor_puntaje}")
        print(f"Tiempo Actual: {tiempo_f}")
        
        for a in range(100):
            idx = random.randint(0, self.n_uavs - 1)
            vecinos = self.generar_vecinos(mejor_sol, idx)

            for vecino in vecinos:
                puntaje_actual, tiempo = self.ValueFo(vecino)
                if puntaje_actual < mejor_puntaje:
                    mejor_puntaje = puntaje_actual
                    mejor_sol = vecino
                    tiempo_f = tiempo
                    break

        print(f"Costo Final: {mejor_puntaje}")
        print(f"Tiempo Final: {tiempo_f}") 



        return mejor_sol

if __name__ == "__main__":
    problem_titan = GreedyDeterminista("./t2_Titan.txt")
    sol_greedy = [2, 3, 4, 5, 6, 7, 8, 0, 9, 13, 12, 1, 11, 10, 14]

    sol = problem_titan.solve(sol_greedy)

    print(sol)
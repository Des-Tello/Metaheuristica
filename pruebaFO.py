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
                 



if __name__ == "__main__":
    problem_titan = GreedyDeterminista("./t2_Titan.txt")
    sol_greedy = [2, 3, 4, 5, 6, 7, 8, 0, 9, 13, 12, 1, 11, 10, 14] 
    # sol_greedy = [2, 3, 4, 5, 6, 7, 8, 0, 9, 13, 12, 1, 11, 10, 14] original 19

    sol = problem_titan.ValueFo(sol_greedy)

    print(sol)
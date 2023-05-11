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
            else:
                tiempo += dic_uav[solucion[i]].tiempo_separacion[solucion[i-1]]
                if tiempo >= dic_uav[solucion[i]].tiempo_preferente:
                    costo += tiempo - dic_uav[solucion[i]].tiempo_preferente
        return costo, tiempo
                 



if __name__ == "__main__":
    problem_titan = GreedyDeterminista("./t2_Deimos.txt")
    sol_greedy = [0, 1, 5, 3, 6, 2, 4, 9, 8, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    # sol_greedy = [2, 3, 4, 5, 6, 7, 8, 0, 9, 13, 12, 1, 11, 10, 14] original 19
    # sol_greedy = [2, 3, 4, 5, 7, 6, 8, 13, 9, 0, 12, 1, 11, 10, 14]  mejora 15
    # sol_greedy = [2, 3, 4, 5, 7, 6, 8, 9, 0, 13, 12, 1, 11, 10, 14]  mejora 7

    sol = problem_titan.ValueFo(sol_greedy)

    print(sol)
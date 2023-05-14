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

    def solve(self):
        UAVS = sorted(self.uavs, key=lambda uav: uav.tiempo_temprano)
        orden_llegada = list()
        tiempo = 0
        puntaje = 0

        for i, uav in enumerate(UAVS):
            if i == 0:
                tiempo += uav.tiempo_temprano
                print(f"[<] Atterriza antes UAV {uav.index} - {tiempo}/{uav.tiempo_preferente}")
                orden_llegada.append(uav)
                continue

            tiempo += uav.tiempo_separacion[orden_llegada[-1].index]
            if tiempo < uav.tiempo_preferente:
                print(f"[<] Atterriza antes UAV {uav.index} - {tiempo}/{uav.tiempo_preferente} ")
                puntaje += abs(tiempo - uav.tiempo_preferente)

            elif tiempo > uav.tiempo_preferente:
                print(f"[>] Atterriza despues UAV {uav.index} - {tiempo}/{uav.tiempo_preferente} ")
                puntaje += abs(tiempo - uav.tiempo_preferente)

            elif tiempo == uav.tiempo_preferente:
                print(f"[=] Atterriza correctamente UAV {uav.index} - {tiempo}/{uav.tiempo_preferente}")
    
                
            orden_llegada.append(uav)

        print(f"Puntaje: {puntaje}")
        # print(f"Orden De Llegada: {[uav.index for uav in UAVS]}")
        print(f"Orden de llegada Greedy Determinista: {[uav.index for uav in orden_llegada]}")


    

if __name__ == "__main__":
    problem_titan = GreedyDeterminista("./t2_Deimos.txt")
    problem_titan.solve()
import copy
from time import time


class Model:
    def __init__(self):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []

    def risolvi_n_regine(self, N):
        self.N_soluzioni = 0
        self.N_iterazioni = 0
        self.soluzioni = []
        self._ricorsione([], N)

    def _ricorsione(self, parziale, N):
        self.N_iterazioni += 1
        # condizione terminale
        if len(parziale) == N:
            if self._soluzione_nuova(parziale):
                self.soluzioni.append(copy.deepcopy(parziale))
                print(parziale)
                self.N_soluzioni += 1
        # caso ricorsivo
        else:
            for row in range(N):
                for col in range(N):
                    parziale.append((row, col))
                    if self._regina_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop()

    def _regina_ammissibile(self, parziale):
        if len(parziale) == 1:
            return True

        ultima_regina = parziale[-1]
        for regina in parziale[:len(parziale) - 1]:
            # controllare righe
            if ultima_regina[0] == regina[0]:
                return False
            #  controllare righe
            if ultima_regina[1] == regina[1]:
                return False
            # controllare diagonali (row + col)
            if (ultima_regina[0] - ultima_regina[1]) == (regina[0] - regina[1]):
                return False
            if (ultima_regina[0] + ultima_regina[1]) == (regina[0] + regina[1]):
                return False
        return True

    def _soluzione_nuova(self, soluzione_nuova):
        # POSSO UTILIZZARE UN ANY CHE MI RIDA' UN TRUE SE ALMENO UNA DLLE COSE IN UN ITERABLE E' TRUE
        # controllo tutte le soluzioni precedenti
        for soluzione in self.soluzioni:
            # per ogni regina della nuova soluzione controllo se e' una configurazione nuova o ripetuta in ordine diverso
            for regina in soluzione_nuova:
                if regina in soluzione:
                    return False
        return True


if __name__ == '__main__':
    model = Model()
    start = time()
    model.risolvi_n_regine(4)
    end = time()
    print(f"soluzioni: {model.N_soluzioni}")
    print(f"iterazioni: {model.N_iterazioni}")
    print(f"temppo impegato: {end - start}")

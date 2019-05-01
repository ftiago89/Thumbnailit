# -*- coding: utf-8 -*-
import numpy as np

class ProcuraImagem:
    def procuraPorPixel(self, thumb, frame):
        erro = 0
        for i in range(0, len(thumb)):
            for j in range(0, len(thumb[0])):
                if (abs(int(thumb[i][j][2]) - int(frame[i][j][2])) != 0):
                    erro += 1
                    if (erro == 92161):   
                        return 0
        return 1


# -*- coding: utf-8 -*-
from copy import copy

class ProcuraThumbnail:
    def procuraThumbnailTipo1(self, thumb, frame):
        erroTotal = (frame.size*5)/100
        erro = 0
        for i in range(0, len(thumb)):
            for j in range(0, len(thumb[0])):
                if (abs(int(thumb[i][j][2]) - int(frame[i][j][2])) > 50):
                    erro += 1
                    if (erro > erroTotal):
                        return 0
        return 1

    def procuraThumbnailTipo2(self, thumb, frame):
        erroTotal = (frame.size*0.5)/100
        erro = 0
        for i in range(0, len(thumb)):
            for j in range(0, len(thumb[0])):
                if (abs(int(thumb[i][j][2]) - int(frame[i][j][2])) > 30):
                    if (((int(thumb[i][j][0] == 0)) and (int(thumb[i][j][1] == 0)) and (int(thumb[i][j][2] == 0)))):
                        pass
                    else:
                        erro += 1
                    if (erro > erroTotal):
                        return 0
        return 1

    def limpaRuido(self, img):
        imgAux = copy(img)
        for i in range(0, len(img)):
            for j in range(0, len(img[0])):
                if ((((int(img[i][j][0] > 199)) or (int(img[i][j][1] > 199)) or (int(img[i][j][2] > 199)))) or
                        (((int(img[i][j][0] < 11)) or (int(img[i][j][1] < 11)) or (int(img[i][j][2] < 11))))):
                    imgAux[i][j][0] = 0
                    imgAux[i][j][1] = 0
                    imgAux[i][j][2] = 0
        return imgAux

    def procuraThumbnailTipo3(self, thumb, frame):

        blocoW = int (len(thumb) / 2)

        parte1 = 0
        parte2 = int (blocoW / 2)
        parte3 = int (blocoW)
        parte4 = int (blocoW + (blocoW / 2))

        contBlocos = 0
        blocosDefeituosos = 7

        contBlocos += self.calcBlock(parte1, parte2, frame, thumb)
        contBlocos += self.calcBlock(parte2, parte3, frame, thumb)
        if(contBlocos > blocosDefeituosos): return 0

        contBlocos += self.calcBlock(parte3, parte4, frame, thumb)
        if(contBlocos > blocosDefeituosos): return 0

        contBlocos += self.calcBlock(parte4, len(thumb), frame, thumb)

        #print('ContBlock = {}'.format(contBlocos))
        if(contBlocos > blocosDefeituosos): return 0

        return 1

    def calcBlock(self, inicio, fim, frame, thumb):

        contBlocos = 0
        blocoH = int (len(thumb[0]) / 2)
        erroP1 = erroP2 = erroP3 = erroP4 = 0
        limite = 40

        margem = 15  #margem de 10%
        limitePixel = (margem * (len(frame) * len(frame[0])) / 4) / 100

        parte1 = 0
        parte2 = int (blocoH / 2)
        parte3 = int (blocoH)
        parte4 = int (blocoH + (blocoH / 2))

        for i in range(inicio, fim):
            for j in range(0, int (len(thumb[0]) / 4)):
                if(abs(int(thumb[i][j + parte1][2]) - int(frame[i][j + parte1][2])) > limite) : erroP1 += 1
                if(abs(int(thumb[i][j + parte2][2]) - int(frame[i][j + parte2][2])) > limite) : erroP2 += 1
                if(abs(int(thumb[i][j + parte3][2]) - int(frame[i][j + parte3][2])) > limite) : erroP3 += 1
                if(abs(int(thumb[i][j + parte4][2]) - int(frame[i][j + parte4][2])) > limite) : erroP4 += 1

        if(erroP1 > limitePixel) : contBlocos += 1
        if(erroP2 > limitePixel) : contBlocos += 1
        if(erroP3 > limitePixel) : contBlocos += 1
        if(erroP4 > limitePixel) : contBlocos += 1

        return contBlocos

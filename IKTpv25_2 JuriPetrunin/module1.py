import random
import string

def lisa_andmeid():
    for i in range(3):
        täht=input("Sisestage täht inemese")
        palk=input("Sisestage listid täht", täht ,"ja", palk)
        palk.append(palk)

def suurim_palk(inimesed, palgad):
    max_palk = max(palgad)
    index = palgad.index(max_palk)
    return inimesed[index], max_palk


def vaikseim_palk(inimesed, palgad):
    min_palk = min(palgad)
    index = palgad.index(min_palk)
    return inimesed[index], min_palk

def palga_otsing(inimesed, palgad, otsitav_nimi):
    tulemused = []
    for i in range(inimesed):
        if inimesed[i] == otsitav_nimi:
            tulemused.append(palgad[i])
    return tulemused


def piiratud_palk(inimesed, palgad, min_palk, max_palk):
    tulemused = []
    for i in range(len(palgad)):
        if min_palk <= palgad[i] <= max_palk:
            tulemused.append((inimesed[i], palgad[i]))
    return tulemused


def keskmine_palk(palgad):
    if len(palgad) == 0:
        return 0
    return sum(palgad) / len(palgad)


def sorteeri_nime_jargi(inimesed, palgad):

    return inimesed, palgad

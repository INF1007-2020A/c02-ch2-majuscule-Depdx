#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    delta_maj_min = ord("a")-ord("A")
    for lettre in mot:
        # TODO completer la fonction ici
        if ord("a") <= ord(lettre) <= ord("z"):
            lettre = chr(ord(lettre)-delta_maj_min)
        resultat += lettre
    return resultat

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

#!/usr/bin/env python
#encoding: utf-8

"""
    Nome file: demo.py
    Autori: Sanelli Gabriele (0227605)
            Scaccia Flavio (0230163)
            Swid Marco (0227134)
    Data creazione: 12/02/2017
    Data ultima modifica: 16/02/2017
    Versione Python: 3.5.2

    Testing sulle prestazioni dei tre algoritmi per il calcolo del minimo
    albero ricoprente
"""

import sys
sys.path.append("../")
from random import randint, seed
from time import clock
from copy import deepcopy
from mst.GraphHelper import GraphHelper
from ExtendedGraph_IncidenceList import ExtendedGraphIncidenceList
from boruvka import ExtendedMST
from mst.mst import MST
from mainBoruvka import createRandomGraph

def testMST(amount, nCalls, maxNodes, maxEdges):
      """ Test sulle diverse implementazione degli algoritmi per il calcolo del
          minimo albero ricoprente

          Verra' eseguito un numero totale di test pari a 'amount' dove,
          in ognuno, calcoliamo il tempo medio su un numero di chiamate pari
          d 'nCalls' per ognuno degli algoritmi.
      """
      #inizializzo il generatore di numeri casuali
      seed()
      for _ in range(amount):
            nNodes = randint(1, maxNodes)
            nEdges = randint(1, maxEdges)
            # azzero i tempi
            timeTotB = 0
            timeTotK = 0
            timeTotP = 0
            for _ in range(nCalls):
                  #creo il grafo
                  graph = createRandomGraph(nNodes, nEdges)
                  GraphHelper.cleanGraph(graph)
                  graphCopy = deepcopy(graph)
                  # tempo boruvka
                  start = clock()
                  w, mst = ExtendedMST.boruvka(graphCopy)
                  timeTotB += clock() - start
                  # tempo kruskal
                  start = clock()
                  w, mst = MST.kruskal(graph)
                  timeTotK += clock() - start
                  # tempo prim
                  start = clock()
                  w, mst = MST.prim(graph)
                  timeTotP += clock() - start
            print ("Test eseguito con {} grafi aventi {} nodi e {} archi, con" \
                       " i seguenti tempi medi:\n".format(nCalls,nNodes,nEdges))
            print ("KRUSKAL: {} secondi".format(timeTotK / nCalls))
            print ("BORUVKA: {} secondi".format(timeTotB / nCalls))            
            print ("PRIM: {} secondi".format(timeTotP / nCalls))
            print ("\n\n")

if __name__ == "__main__":

      testMST(30,20,10,10)

      testMST(10,5,100,100)

      testMST(3,2,1000,1000)

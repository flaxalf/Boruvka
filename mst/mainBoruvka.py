#!/usr/bin/env python
#encoding: utf-8

"""
    Nome file: mainBoruvka.py
    Autori: Sanelli Gabriele (0227605)
            Scaccia Flavio (0230163)
            Swid Marco (0227134)
    Data creazione: 12/02/2017
    Data ultima modifica: 16/02/2017
    Versione Python: 3.5.2

    Il modulo permette di testare i tre algoritmi di calcolo del minimo
    albero ricoprente di un grafo, con rispettivi profiling.
    Necessaria la chiamata da riga di comando con passaggio degli argomenti:
    numero nodi, numero archi da creare.
"""

import sys
sys.path.append("../")
import argparse
from random import random, randint, seed
from copy import deepcopy
from mst.GraphHelper import GraphHelper
from ExtendedGraph_IncidenceList import ExtendedGraphIncidenceList
from boruvka import ExtendedMST
from mst.mst import MST
import pstats
import cProfile

def _parseargs():
      parser = argparse.ArgumentParser(description='Calcolatore di minimo ' \
                                       'albero ricoprente di un grafo casuale')
      parser.add_argument("Nodes", help = "Numero di nodi da creare", \
                                                           type = int)
      parser.add_argument("Edges", help = "Numero archi da creare", \
                                                           type = int)
      args = parser.parse_args()
      return args

def createRandomGraph(nodes, edges):
      #inizializzo il generatore di numeri casuali
      seed()
      g = ExtendedGraphIncidenceList()
      for i in range(0,nodes):
            g.insertNode(i)
      for i in range(0,edges):
            # peso dell'arco generato casualmente
            weight = round(randint(0, nodes * 100 - 1) + random(), 6)
            # genero casualmente nodi su cui inciderà l'arco
            tail = randint(0,nodes - 1)
            head = randint(0,nodes - 1)
            # inserisco l'arco ad entrambe le liste di incidenza
            g.insertEdge(tail, head, weight)
            g.insertEdge(head, tail, weight)
      return g

def main(args):
      nodes = int(sys.argv[1])
      edges = int(sys.argv[2])
      if nodes <= 0 or edges <= 0:
            return
      # creo il grafo, lo rendo connesso ed elimino archi multipli
      graph = createRandomGraph(nodes, edges)
      GraphHelper.cleanGraph(graph)
      graphCopy = deepcopy(graph)

      print("THE GRAPH:\n")
      graph.printGraph()

      print("\n")
      # test boruvka
      w1, mst = ExtendedMST.boruvka(graphCopy)
      print("WEIGHT BORUVKA:", w1)

      print("\n")
      # test kruskal
      w2, mst2 = MST.kruskal(graph)
      print("WEIGHT KRUSKAL:", w2)

      print("\n")
      # test prim
      w3, mst3 = MST.prim(graph)
      print("WEIGHT PRIM:", w3)

      print("\n")

      if(round(w1,3) == round(w2,3) and round(w2, 3) == round(w3,3)):
            print("Computato stesso peso dai 3 algoritmi.")
      else:
            print("Error! I 3 algoritmi tornano un peso totale differente!")

      print ("\n")

if __name__ == '__main__':
      _args = _parseargs()
      # main viene eseguito nella chiamata successiva
      cProfile.runctx("main(_args)",globals(), locals(), "mstTimes.prof")
      p = pstats.Stats("mstTimes.prof")
      p.strip_dirs().sort_stats('time').print_stats("kruskal")
      p.strip_dirs().sort_stats('time').print_stats("boruvka")
      p.strip_dirs().sort_stats('time').print_stats("prim")

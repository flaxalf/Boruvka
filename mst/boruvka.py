#!/usr/bin/env python
#encoding: utf-8

"""
    Nome file: boruvka.py
    Autori: Sanelli Gabriele (0227605)
            Scaccia Flavio (0230163)
            Swid Marco (0227134)
    Data creazione: 12/02/2017
    Data ultima modifica: 16/02/2017
    Versione Python: 3.5.2

    Implementazione dell'algoritmo di Boruvka
"""

import sys
sys.path.append("../")
from mst.mst import MST
from ExtendedGraph_IncidenceList import ExtendedGraphIncidenceList
from linked_ds.queue.Queue import CodaArrayList_deque as Queue

class ExtendedMST(MST):
      """
      Contiene un algoritmo per il calcolo del minimo albero ricoprente
      """

      @staticmethod
      def boruvka(graph):
            """Algoritmo di Boruvka per la ricerca del minimo albero ricoprente
                  che prende in input un grafo assunto come NON orientato
                  (implementato con liste di incidenza).
            """
            if graph.nodes == None:
                  return 0, []

            #dizionario utile per salvare gli spostamenti dei nodi
            dic = {}
            for i in range(len(graph.nodes)):
                  dic[i] = i
            #inserisco gli indici dei nodi nella coda
            q = Queue()
            for i in range(len(graph.nodes)):
                  q.enqueue(i)
            #lista di archi scelti per il minimo albero ricoprente
            mstEdges = []
            #contatore per mantenere il peso totale del mst
            mstWeight = 0
            while len(graph.nodes) > 1:

                  edges = []
                  while not(q.isEmpty()):
                        node = q.dequeue()
                        # se il nodo è stato già fuso continuo
                        #l'estrazione dalla coda
                        if graph.inc[node].getFirstRecord() == None:
                              continue

                        #trovo il minimo arco incidente sul nodo
                        minEdge = graph.inc[node].getMinElem()
                        edges.append(minEdge)

                  for edge in edges:
                        #se considero un arco incidente sullo stesso nodo
                        #lo elimino e passo all'arco minimo successivo
                        if edge.tail == edge.head:
                              #devo trovare il nodo sorgente dell'arco
                              indexNodeTail = dic[edge.tail]
                              graph.deleteEdge(indexNodeTail, edge.weight)
                              q.enqueue(indexNodeTail)
                              continue

                        #devo trovare il nodo sorgente e destinazione dell'arco
                        indexNodeTail = dic[edge.tail]
                        indexNodeHead = dic[edge.head]
                        listIncTail = graph.inc[indexNodeTail]
                        listIncHead = graph.inc[indexNodeHead]
                        #se i due nodi non si trovano nello stesso super-vertice
                        if indexNodeTail != indexNodeHead:
                              #includo l'arco nella soluzione
                              mstEdges.append(edge)
                              mstWeight += edge.weight
                              #fondo le due liste
                              listIncTail.append(listIncHead)
                              #cancello la lista collegata al nodo destinazione
                              listIncHead.first = None
                              del graph.nodes[indexNodeHead]
                              #contraggo i due nodi formando un super-vertice
                              dic[indexNodeHead] = indexNodeTail
                              for key in dic:
                                    if dic[key] == indexNodeHead:
                                          dic[key] = indexNodeTail
                              #elimino gli archi all'interno dello stesso
                              #super-vertice
                              curr = listIncTail.getFirstRecord()
                              while curr != None:
                                    edge = curr.elem
                                    nextRec = curr.next
                                    if dic[edge.tail] == dic[edge.head]:
                                          listIncTail.deleteRecord(curr)
                                    curr = nextRec
                              #aggiungo il super-vertice nella coda
                              q.enqueue(indexNodeTail)

            return mstWeight, mstEdges

def main():
      print ("Grafo della figura 12.8 del libro:\n")
      graph = ExtendedGraphIncidenceList()
      graph.insertNode("A")
      graph.insertNode("B")
      graph.insertNode("C")
      graph.insertNode("D")
      graph.insertNode("E")
      graph.insertNode("F")
      graph.insertNode("G")

      graph.insertEdge(0,1,7.0)
      graph.insertEdge(0,2,14.0)
      graph.insertEdge(0,3,30.0)
      graph.insertEdge(1,0,7.0)
      graph.insertEdge(1,2,21.0)
      graph.insertEdge(2,0,14.0)
      graph.insertEdge(2,1,21.0)
      graph.insertEdge(2,3,10.0)
      graph.insertEdge(2,4,1.0)
      graph.insertEdge(3,0,30.0)
      graph.insertEdge(3,2,10.0)
      graph.insertEdge(4,2,1.0)
      graph.insertEdge(4,5,6.0)
      graph.insertEdge(4,6,9.0)
      graph.insertEdge(5,4,6.0)
      graph.insertEdge(5,6,4.0)
      graph.insertEdge(6,4,9.0)
      graph.insertEdge(6,5,4.0)

      graph.printGraph()

      print ("\nBoruvka\n")

      w,mst = ExtendedMST.boruvka(graph)

      print("lista di archi del minimo albero ricoprente")
      print([str(item) for item in mst])
      print("\nweight: ",w)

if __name__ == "__main__":
      main()

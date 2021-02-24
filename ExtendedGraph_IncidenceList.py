#!/usr/bin/env python
#encoding: utf-8

"""
    Nome file: ExtendedGraph_IncidenceList.py
    Autori: Sanelli Gabriele (0227605)
            Scaccia Flavio (0230163)
            Swid Marco (0227134)
    Data creazione: 12/02/2017
    Data ultima modifica: 16/02/2017
    Versione Python: 3.5.2

    Estensione classe GrapIncidenceList
"""

import sys
sys.path.append("../")
from ExtendedDoubleLinkedList import ExtendedDoubleLinkedList as Lista
from graph.Graph_IncidenceList import GraphIncidenceList
from mst.tree.CmpEdge import CmpEdge

class ExtendedGraphIncidenceList(GraphIncidenceList):

    def insertNode(self, elem):
        newnode = super().insertNode(elem)
        if self.nodes == None:  #crea nuovi dizionari
            self.nodes = {newnode.index : newnode}
            #ci occorre la lista doppiamente collegata estesa
            self.inc = {newnode.index : Lista()}
        else:   #aggiungi ai dizionari esistenti
            self.nodes[newnode.index] = newnode
            #ci occorre la lista doppiamente collegata estesa
            self.inc[newnode.index] = Lista()
        return newnode

    def insertEdge(self, tail, head, weight=None):
        if head in self.nodes and tail in self.nodes:
            #ci occorre la classe CmpEdge per confrontare i costi degli archi
            self.inc[tail].addAsLast(CmpEdge(tail, head, weight))

    def deleteEdge(self, tail, weight):
        """ Cancello un arco cercandolo in base al peso nella lista
               di incidenza """
        if tail in self.nodes:
            curr = self.inc[tail].getFirstRecord()
            while curr != None:
                if curr.elem.weight == weight:
                    self.inc[tail].deleteRecord(curr)
                    # non possono esserci archi con pesi uguali
                    break
                curr=curr.next

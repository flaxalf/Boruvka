#!/usr/bin/env python
#encoding: utf-8

"""
    Nome file: ExtendedDoubleLinkedList.py
    Autori: Sanelli Gabriele (0227605)
            Scaccia Flavio (0230163)
            Swid Marco (0227134)
    Data creazione: 12/02/2017
    Data ultima modifica: 16/02/2017
    Versione Python: 3.5.2

    Estensione classe DoubleLinkedList
"""

import sys
sys.path.append("../")
from linked_ds.list.DoubleLinkedList import ListaDoppiamenteCollegata

class ExtendedDoubleLinkedList(ListaDoppiamenteCollegata):

      def getMinElem(self):
            """ Ritorna l'elemento minimo di una lista """
            if self.first == None:
                  return None
            minElement = self.first.elem
            current = self.first.next
            while current != None:
                  if current.elem < minElement:
                        minElement = current.elem
                  current = current.next
            return minElement

      def append(self, lista):
            """ Concatena la lista passata come argomento a quella
            su cui è invocato il metodo """
            firstRec = lista.first
            lastRec = lista.last
            if self.first == None:
                  self.first = firstRec
                  self.last = lastRec
            else:
                  self.last.next = firstRec
                  firstRec.prev = self.last
                  self.last = lastRec

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on May 8, 2016

@author: David Hernandez
'''
import datetime
from decimal import *

class Transaccion:
    
    def __init__(self, monto, id):
        getcontext().prec = 10
        self.monto = Decimal(monto)
        self.fecha = datetime.datetime.now()
        self.idEstablecimiento = id
        
class BilleteraElectronica:
    '''
    Classdocs
    '''
    def __init__(self, Id, nombres, apellidos, CI, PIN):
        '''
        Constructor
        '''
        #try:
        getcontext().prec = 10
        self.__Id = Id
        self.nombres = nombres
        self.apellidos = apellidos
        self.CI = CI
        self.__PIN = PIN
        self.__recargas = []
        self.__consumos = []
        self.__saldo = Decimal(0)
        assert(type(self.__Id) is int)
        assert(type(self.nombres) is str)
        assert(type(self.apellidos) is str)
        assert((type(self.CI) is int) and self.CI>0)
        assert((type(self.__PIN) is str) and self.__PIN.isdigit())
        #except:
        #    raise ValueError('Error de tipo al construir')
    
    def recargar(self, credito):
        self.__recargas.append(credito)
        if(credito.monto>0):
            self.__saldo += credito.monto
        else:
            raise ValueError('No se puede recargar montos menores o iguales a 0')
    
    def consumir(self, PIN, debito):
        if(self.__PIN == PIN and debito.monto>=0):
            if(self.__saldo >= debito.monto):
                self.__saldo -= debito.monto
                self.__consumos.append(debito)
            else:
                raise ValueError('Saldo insuficiente, transaccion invalida')
    
    def saldo(self):
        return self.__saldo

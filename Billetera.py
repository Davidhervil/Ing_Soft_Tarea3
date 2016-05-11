#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on May 8, 2016

@author: David Hernandez
'''
import datetime
import decimal
class Transaccion:
    
    def __init__(self, monto, id):
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
        try:
            self.__Id = Id
            self.nombres = nombres
            self.apellidos = apellidos
            self.CI = CI
            self.__PIN = PIN
            self.__recargas = []
            self.__consumos = []
            self.__saldo = Decimal(0)
            assert(type(self.__Id) is int)
            assert(type(self.nombres_list) is str)
            assert(type(self.apellidos_list) is str)
            assert((type(self.CI) is int) and self.CI>0)
            assert((type(self.__PIN) is str) and self.__PIN.isnumeric())
        except:
            raise ValueError('Error de tipo al construir')
    
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

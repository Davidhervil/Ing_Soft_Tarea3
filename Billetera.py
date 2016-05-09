'''
Created on May 8, 2016

@author: David Hernandez
'''
from datetime import date
class Transaccion:
    
    def __init__(self,monto,fecha,id):
        self.monto=monto
        self.fecha=fecha
        self.idEstablecimiento=id
        
class BilleteraElectronica:
    '''
    classdocs
    '''
    def __init__(self, Id,nombres,apellidos,CI,PIN):
        '''
        Constructor
        '''
        self.__Id = Id
        self.nombres_list = nombres.split(' ')
        self.apellidos_list = apellidos.split(' ')
        self.CI = CI
        self.__PIN = PIN
        self.__recargas = []
        self.__consumos = []
        self.__saldo = 0
    
    def recargar(self,credito):
        self.__recargas.append(credito)
        self.__saldo += credito.monto
    
    def consumir(self,debito):
        if(self.__saldo>=debito.monto):
            self.__saldo -= debito.monto
            self.__consumos.append(debito)
        else:
            raise ValueError('Saldo insuficiente, transaccion invalida')
    
    def saldo(self):
        return self.__saldo

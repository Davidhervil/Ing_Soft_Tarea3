#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 9/5/2016

@author: Dell
'''
from Billetera import * 
from datetime import date 
import unittest


class BilleteraTester(unittest.TestCase):
    
    def testCrearBilletera(self):
        miBilletera = BilleteraElectronica("MiBilletera", "nombre", "apellido", 23711366, 4561)
        self.assertTrue(miBilletera._BilleteraElectronica__Id=="MiBilletera")
        self.assertTrue(miBilletera.saldo()==0)
        self.assertTrue(miBilletera._BilleteraElectronica__PIN==4561)
        self.assertTrue(miBilletera._BilleteraElectronica__recargas==[])
        self.assertTrue(miBilletera._BilleteraElectronica__recargas==[])
        
    def testUsuarioConNombreEspecial(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Ñángara", "Diaz", 23711366, 4561)
        self.assertEquals(miBilletera.nombres_list,["Ñángara"])
    
    def testUsuarioConApellidoEspecial(self):
        miBilletera = BilleteraElectronica("MiBilletera", "David", "Ñángara", 23711366, 4561)
        self.assertEquals(miBilletera.apellidos_list,["Ñángara"])
    
    def testUsuarioConNombreSimple(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        self.assertEquals(miBilletera.nombres_list,["Eliot"])
    
    def testUsuarioConNombreMultiple(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot David", "Hernandez", 23711366, 4561)
        self.assertEquals(miBilletera.nombres_list,["Eliot","David"])
            
    def testUsuarioConApellidoSimple(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        self.assertEquals(miBilletera.apellidos_list,["Hernandez"])
    
    def testUsuarioConApellidoMultiple(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez Diaz", 23711366, 4561)
        self.assertEquals(miBilletera.apellidos_list,["Hernandez","Diaz"])
        
    def testRecargaSimple(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(123, fecha, 117)
        miBilletera.recargar(credito)
        self.assertEquals(miBilletera.saldo(), 123)
        

    def testConsumirConPINCorrecto(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(234, fecha, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(122, fecha, "Restaurant El Paso")
        miBilletera.consumir(4561, debito)
        self.assertEquals(miBilletera.saldo(), 234-122)

    def testConsumirSinPINCorrecto(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(234, fecha, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(122, fecha, "Restaurant El Paso")
        miBilletera.consumir(4562, debito)
        self.assertEquals(miBilletera.saldo(), 234)

    def testConsumirSinSaldoSuficiente(self):
        try:
            miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
            fecha = date(2016,2,23)
            credito = Transaccion(100, fecha, "Casa")
            miBilletera.recargar(credito)
            debito = Transaccion(122, fecha, "Restaurant El Paso")
            miBilletera.consumir(4561, debito)
            print("Fallo de encuentro de Error")
        except:
            print("Saldo insuficiente, transaccion invalida")
        
    def testRecargaNegativa(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(25680, fecha, "Casa")
        miBilletera.recargar(credito)
        credito2 = Transaccion(-680, fecha, "Casa")
        miBilletera.recargar(credito2)
        self.assertEquals(miBilletera.saldo(), 25680)

    def testConsumoNegativo(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(970680, fecha, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(-680, fecha, "Casa")
        miBilletera.consumir(4561, debito)
        self.assertEquals(miBilletera.saldo(), 970680)
        
    def testRecargaYConsumoDecimal(self):
        miBilletera = BilleteraElectronica("MiBilletera", "Eliot", "Hernandez", 23711366, 4561)
        fecha = date(2016,2,23)
        credito = Transaccion(25.97068085, fecha, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(20.987654321, fecha, "Casa")
        miBilletera.consumir(4561, debito)
        self.assertEquals(miBilletera.saldo(), (25.97068085-20.987654321))
        
    
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
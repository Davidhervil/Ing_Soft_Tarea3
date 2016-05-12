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
        miBilletera = BilleteraElectronica("1234", "nombre", "apellido", 23711366, "4561")
        self.assertTrue(miBilletera._BilleteraElectronica__Id=="1234")
        self.assertTrue(miBilletera.saldo()==0)
        self.assertTrue(miBilletera._BilleteraElectronica__PIN=="4561")
        self.assertTrue(miBilletera._BilleteraElectronica__recargas==[])
        self.assertTrue(miBilletera._BilleteraElectronica__consumos==[])
        self.assertTrue(miBilletera.nombres=="nombre")
        self.assertTrue(miBilletera.apellidos=="apellido")
        self.assertTrue(miBilletera.CI==23711366)
    
    def testCrearBilleteraFalloId(self):
        try:
            miBilletera = BilleteraElectronica("1234.3213", "nombre", "apellido", 23711366, "4561")
            print("Fallo de deteccion de error de tipo al construir")
        except:
            print("Exito al detectar error de tipo al construir")

    def testCrearBilleteraFalloNombre(self):
        try:
            miBilletera = BilleteraElectronica("1234", 1273676, "apellido", 23711366, "4561")
            print("Fallo de deteccion de error de tipo al construir")
        except:
            print("Exito al detectar error de tipo al construir")

    def testCrearBilleteraFalloApellid(self):
        try:
            miBilletera = BilleteraElectronica("1234.3213", "nombre", 123478628, 23711366, "4561")
            print("Fallo de deteccion de error de tipo al construir")
        except:
            print("Exito al detectar error de tipo al construir")

    def testCrearBilleteraFalloId(self):
        try:
            miBilletera = BilleteraElectronica("1234.3213", "nombre", "apellido", 23711366, "asd4561")
            print("Fallo de deteccion de error de tipo al construir")
        except:
            print("Exito al detectar error de tipo al construir")

    def testUsuarioConNombreEspecial(self):
        miBilletera = BilleteraElectronica("1234", "Ñángara", "Diaz", 23711366, "4561")
        self.assertEquals(miBilletera.nombres,"Ñángara")
    
    def testUsuarioConApellidoEspecial(self):
        miBilletera = BilleteraElectronica("1234", "David", "Ñángara", 23711366, "4561")
        self.assertEquals(miBilletera.apellidos,"Ñángara")
    
    def testUsuarioConNombreSimple(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        self.assertEquals(miBilletera.nombres,"Eliot")
    
    def testUsuarioConNombreMultiple(self):
        miBilletera = BilleteraElectronica("1234", "Eliot David", "Hernandez", 23711366, "4561")
        self.assertEquals(miBilletera.nombres,"Eliot David")
            
    def testUsuarioConApellidoSimple(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        self.assertEquals(miBilletera.apellidos,"Hernandez")
    
    def testUsuarioConApellidoMultiple(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez Diaz", 23711366, "4561")
        self.assertEquals(miBilletera.apellidos,"Hernandez Diaz")
        
    def testRecargaSimple(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion(123,  117)
        miBilletera.recargar(credito)
        self.assertEquals(miBilletera.saldo(), 123)
        

    def testConsumirConPINCorrecto(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion(234, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(122, "Restaurant El Paso")
        miBilletera.consumir("4561", debito)
        self.assertEquals(miBilletera.saldo(), 234-122)

    def testConsumirSinPINCorrecto(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion(234, "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(122, "Restaurant El Paso")
        miBilletera.consumir("4562", debito)
        self.assertEquals(miBilletera.saldo(), 234)

    def testConsumirSinSaldoSuficiente(self):
        try:
            miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
            credito = Transaccion(100,  "Casa")
            miBilletera.recargar(credito)
            debito = Transaccion(122,  "Restaurant El Paso")
            miBilletera.consumir("4561", debito)
            print("Fallo de encuentro de Error")
        except:
            self.assertEquals(miBilletera.saldo(),100)
        
    def testRecargaNegativa(self):
        try:
            miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
            credito = Transaccion(25680,  "Casa")
            miBilletera.recargar(credito)
            credito2 = Transaccion(-680,  "Casa")
            miBilletera.recargar(credito2)
        except:
            self.assertEquals(miBilletera.saldo(), 25680)

    def testConsumoNegativo(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion(970680,  "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(-680,  "Casa")
        miBilletera.consumir("4561", debito)
        self.assertEquals(miBilletera.saldo(), 970680)
        
    def testRecargaYConsumoDecimal(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion(25.97068085,  "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion(20.987654321,  "Casa")
        miBilletera.consumir("4561", debito)
        self.assertEquals(miBilletera.saldo(), (Decimal(25.97068085)-Decimal(20.987654321)))

    def testConsumoExacto(self):
        miBilletera = BilleteraElectronica("1234", "Eliot", "Hernandez", 23711366, "4561")
        credito = Transaccion("25.97068085",  "Casa")
        miBilletera.recargar(credito)
        debito = Transaccion("25.97068085",  "Casa")
        miBilletera.consumir("4561", debito)
        self.assertEquals(miBilletera.saldo(), (Decimal(25.97068085)-Decimal(25.97068085)))        
        
    def testRecargaCero(self):
        try:
            miBilletera = BilleteraElectronica("1234", "Meñique", "Stark", 23711366, "4561")
            credito2 = Transaccion(123,"Invernalia")
            miBilletera.recargar(credito2)
            credito = Transaccion(0,"Samoa")
            miBilletera.recargar(credito)
            print("Fallo al no permitir recargas de 0")
        except:
            self.assertEquals(miBilletera.saldo(),123)

    def testConsumoCero(self):
        miBilletera = BilleteraElectronica("1234", "Meñique", "Stark", 23711366, "4561")
        credito2 = Transaccion(123,"Invernalia")
        miBilletera.recargar(credito2)
        consumo = Transaccion(0,"Samoa")
        miBilletera.consumir("4561",consumo)
        self.assertEquals(miBilletera.saldo(),123)
     
    def testConsumoEnteroRecargaDecimal(self):
        miBilletera = BilleteraElectronica("1234", "Meñique", "Stark", 23711366, "4561")
        credito = Transaccion(123.123,"Invernalia")
        miBilletera.recargar(credito)
        consumo = Transaccion(123,"Samoa")
        miBilletera.consumir("4561",consumo)
        self.assertEquals(miBilletera.saldo(),Decimal(123.123)-consumo.monto)

    def testConsumoDecimalRecargaEntero(self):
        miBilletera = BilleteraElectronica("1234", "Meñique", "Stark", 23711366, "4561")
        credito = Transaccion(123,"Invernalia")
        miBilletera.recargar(credito)
        consumo = Transaccion(12.12,"Samoa")
        miBilletera.consumir("4561",consumo)
        self.assertEquals(miBilletera.saldo(),Decimal(123)-consumo.monto)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

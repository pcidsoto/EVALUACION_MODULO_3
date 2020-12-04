from clase_bodega import Bodega
from clase_diseno import Diseno
from class_armado import Armado
from ArchivoDict import ArchivoDict
import time
import os


registro_ramos_terminados = ArchivoDict("Ramos_salida_test1")
mi_bodega = Bodega()
diseno1 = Diseno("Diseno_test1")
proceso1 = Armado()

#diseno_listo = diseno1.agregar_diseno()
diseno_listo = ['CL4a5f6c15','BL10a10b4d24']
diseno1.agregar_elemento(diseno_listo)

while True:
    
    mi_bodega.recibir_flores(5) # Se define las flores que llegaran a bodega
    for elem in diseno_listo:
        #print(mi_bodega.bodega_sistematizada)
        print("Armando diseño: ", elem)
        proceso1.set_diseno(elem)
       
        mi_bodega.sistematizacion_bodega()
        print(mi_bodega.bodega_sistematizada.items())
        time.sleep(5)
        mi_bodega.actualizar_archivo()
        ramo_a_procesar = proceso1.identificar_flores()
        ramo_a_pedir = proceso1.armar_ramo(ramo_a_procesar)

        stock_bodega = mi_bodega.get_diccionario()

        stock, ramo_ok = proceso1.ver_disponibilidad_bodega(ramo_a_pedir, stock_bodega)
        if ramo_ok:
            print("Ramo Guardado")
            print(stock.items())
            ramo = proceso1.ramo_string(ramo_ok)
            registro_ramos_terminados.agregar_elemento(ramo,1)
            mi_bodega.recibir_diccionario(stock)
            time.sleep(5)
            os.system('cls')
        else:
            print("No hay flores para el armar el Ramo")
            mi_bodega.recibir_diccionario(stock)
            time.sleep(5)
            os.system('cls')
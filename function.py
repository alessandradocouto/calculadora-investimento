import string
from tkinter import messagebox
import math
from typing import List

class Func():
    def jc( self, r: float, t: float, n: int = 1) -> float:
        return (1 + r /  float(n) )**( float(n) * t ) - 1

    def day2year (self, d: float, wd: int = 252) -> float:
        return 100.0 * (self.jc(d, wd ))

    def year2month (self, a: float) -> float:
        return 100.0 * (self.jc(a, 1 / 12))

    def doublePrincipal(self, r: float ) -> float:
        return math.log(2, 1 + r )

    # validacao
    def _validate_float(self, num: float) -> float:
        if(num == ""): 
            return True
        try:
            value = float(num)
        except ValueError:
            messagebox.showwarning("Alert", "Digite um número válido,"
            "sem uso de vírgulas ou números negativos. Vamos tentar de novo?", icon="error")
            return False
        return value

    def _validate_int(self, num: int) -> int:
        if(num == ""): 
            return True
        try:
            value = int(num)  
        except ValueError:
            messagebox.showwarning("Alert", "Digite um número válido, "
            "sem uso de vírgulas ou números negativos. Vamos tentar de novo?", icon="error")
            return False
        return 0 <= value <= 10000000000

    # poupanca
    def calcular_poupanca(self, tx_selic: float) -> List:
        text_num = float(tx_selic) / 100
        tr = 0.0
        if( text_num <= 0.085 ):
            tx_poupanca = ((0.7 * text_num) + tr) * 100.0
            tx_poupanca_mes = self.year2month(tx_poupanca / 100.0)
            return [tx_poupanca, tx_poupanca_mes]
        else:
            tx_poupanca = (0.0617 + tr) * 100.0
            tx_poupanca_mes = (0.0050000 + tr) * 100.0
            return [tx_poupanca, tx_poupanca_mes]

    def mostra_poupanca(self, tx_selic: float) -> string:
        return f"{self.calcular_poupanca(tx_selic)[0]:.2f}% ao ano = {self.calcular_poupanca(tx_selic)[1]:.4f}% ao mês"

    # cdi
    def calcular_cdi_juros(self, cdi: float) -> List:
        cdi_mes = (self.year2month((cdi/100)) / 100)
        cdi_dia = self.jc((cdi_mes), 1/21)

        return [cdi, (cdi_mes * 100), (cdi_dia * 100)]

    def calculo_rent_bruta(self, rent_cdi_input:float, cdi:float) -> float: 
        # taxa de rentabilidade 100%
        rent_cdi = 0
        if(rent_cdi_input == 100):
            rent_cdi = self.calcular_cdi_juros(cdi)[0] 
            return rent_cdi
        else:
            # taxa de rentabilidade diferente de 100
            rent_cdi = (self.calcular_cdi_juros(cdi)[0] * rent_cdi_input)/100
            return rent_cdi

    # calculo percentual Rentabilidade Com IR
    def calculo_rent_com_IR(self, rent_cdi:float, cdi:float, ir:float) -> List:
        # rentabilidade cdi ir
        rent_cdi_IR = round(rent_cdi * (1 - (ir/100)),2)
        # cdi com IR ao ano
        cdi_IR = (rent_cdi_IR * (self.calcular_cdi_juros(cdi)[0])/100)
        return [rent_cdi_IR, cdi_IR]

    def montante(self, c:float, juros_mes: float, m: int=1) -> float:
        return c * ((1 + (juros_mes/100)) ** m)

    # frame blue
    def CDB ( self, c: float, cdi: float, p: float, t: float, i: float, m: int=1) -> List:
        tx_rent_cdijuros_mes = (self.year2month(cdi/100))
        mont_bruto = self.montante(c, tx_rent_cdijuros_mes, m)

        rent_bruto_lci = mont_bruto - c

        mont_ir = rent_bruto_lci * (i/100)
        mont_apl = mont_bruto - mont_ir

        rent_liq_cdb = rent_bruto_lci - mont_ir
        mont_poup = self.montante(c, p[1], m)
        
        dif_apl_poup = mont_apl - mont_poup
        rend_mes = (rent_liq_cdb / c) * 100
        
        return [mont_apl, mont_poup, mont_ir, dif_apl_poup, rend_mes]
 
    def apl_dif_poup(self, c: float, result_cdb: List) -> float:
        apl_poup = (result_cdb[3] / c) * 100
        return apl_poup


    def rent_poup_cdi(self, cdi, ir: float, calc_poup: List) -> float:
        rent_poup_cdi_ir = calc_poup[0] / ( cdi * (1 - (ir/100)))

        return rent_poup_cdi_ir * 100


    def tempo_double_poup(self, juros_poup_anual: List) -> float:
        tempo_poup = self.doublePrincipal(juros_poup_anual[0]/100)
        return tempo_poup
        
    def tempo_double_apl(self, rent_cdi_ir: List) -> float:
        tempo_apl = self.doublePrincipal(rent_cdi_ir[1]/100)
        return tempo_apl

import unittest
from app_function import Func
# from nomeArquivo import nomeDaClasse

# nomear class do teste com o mesmo nome módulo testado
class FuncTest(unittest.TestCase):
    
    def test_doublePrincipal(self):
        result = 0.0617
        expected = 11.57726752437506
        self.assertEqual(Func.doublePrincipal(self, result), expected)

    def test_jc_type(self):
        juros = 0.1315
        self.assertIsInstance(Func.jc(self, juros, 1/12), float, 'Not a float')

    def test_jc_return(self):
        r = 0.010348528288471437
        juros = 0.1315
        self.assertEqual(Func.jc(self, juros, 1/12), r)

    def test_year2month_type (self):
        juros = 0.1315
        result_jc = Func.jc(self, juros, 1/12) * 100
        """ teste para tipo de retorno float"""
        self.assertIsInstance(result_jc, float, 'Not a float')

    def test_year2month_return (self):
        juros = 0.1315
        expected = 1.0348528288471437
        result_jc = Func.jc(self, juros, 1/12) * 100
        self.assertEqual(result_jc, expected)

    def validate_float_affirmative(self):
        self.assertTrue(Func._validate_float(self, ''))

    def test_validate_float_return(self):
        self.assertIsInstance(Func._validate_float(self, 1000.00), float)
    
    def validate_float_negative(self):
        self.assertFalse(Func._validate_float(self, -1000))

    def test_validate_int_affirmative(self):
        self.assertTrue(Func._validate_int(self, ''))
    
    def test_validate_int_return(self):
        self.assertIsInstance(Func._validate_int(self, 1000.00), int)
    
    def test_validate_int_negative(self):
        self.assertFalse(Func._validate_int(self, -390))

    def test_calcular_poupanca_high_selic(self):
        juros_selic = 13.25
        expected = [6.17, 0.5000]
        calc_poupanca = Func.calcular_poupanca(self, juros_selic)

        self.assertEqual(calc_poupanca, expected)

    def test_calcular_poupanca_low_selic(self):
        # num_tr = 0.0
        # tx_poup = ((0.7 * juros_selic/100.0) + num_tr) * 100.0
        # poup_mes = Func.year2month(Func, tx_poup /100.0)
        juros_selic = 8.25
        cdi = 5.7749999999999995
        cdi_mes = 0.46896296058003273
        expected = [ cdi, cdi_mes ]

        calc_poupanca = Func.calcular_poupanca(self, juros_selic)
        self.assertEqual(calc_poupanca, expected)

    def test_calcular_cdi_juros(self):
        cdi_a = 13.15
        # cdi_mes = (Func.year2month(self, (cdi/100))) / 100
        # cdi_dia = Func.jc(self, cdi_mes, 1/21)
        cdi_m = 1.0348528288471437
        cdi_d = 0.049037490119197
        expected = [ cdi_a, cdi_m, cdi_d ]
        self.assertEqual(Func.calcular_cdi_juros(self, cdi_a), expected)

    def test_calcular_rent_bruta_high_percent(self):
        rentab_cdi = 100
        cdi_a = 13.15
        expected = 13.15
        
        self.assertEqual(Func.calcular_rent_bruta(self, rentab_cdi, cdi_a), expected)

    def test_calcular_rent_bruta_low_percent(self):
        rentab_cdi = 93
        cdi_a = 13.15
        expected = 12.2295
        
        self.assertEqual(Func.calcular_rent_bruta(self, rentab_cdi, cdi_a), expected)

    def test_calcular_rent_com_IR(self):
        rentab_cdi = 93
        cdi_a = 0.1315
        ir = 22.5

        rentab_cdi_IR = 72.08
        cdi_a_IR = 0.0947852
        expected = [ rentab_cdi_IR, cdi_a_IR ]

        self.assertEqual(Func.calcular_rent_com_IR(self, rentab_cdi, 
        cdi_a, ir), expected)

    def test_montante(self):
        cap = 1000.00
        cdi_juros_mes = 1.0349
        m = 1
        expected = 1010.3489999999999

        self.assertEqual(Func.montante(self, cap, cdi_juros_mes, m), expected)

    def test_CDB (self):
        mont_aplic = 1008.0201094235654
        mont_poupanca = 1004.9999999999999
        mont_ir = 2.328418864906081
        dif_apl_poup = 3.0201094235654864
        rendim_mes = 0.802010942356539
        expected = [ mont_aplic, mont_poupanca, mont_ir, dif_apl_poup, rendim_mes ]
        
        self.assertEqual(Func.CDB(self, 1000.00, 13.15, [6.17, 0.5], 100, 22.5, 1), expected)

    def test_apl_dif_poup(self):
        cap = 1000.00
        expected = 0.30201094235654864
        lista_cdb = [
            1008.0201094235654, 
            1004.9999999999999, 
            2.328418864906081, 
            3.0201094235654864,
            0.802010942356539
        ]

        self.assertEqual(Func.apl_dif_poup(self, cap, lista_cdb), expected)

    def test_rent_poup_cdi(self):
        calc_poup = [ 6.17, 0.5 ]
        expected = 60.54213173065129
  
        self.assertEqual(Func.rent_poup_cdi(self, 13.15, 22.5, calc_poup), expected)

    def test_tempo_double_poup(self):
        expected = 11.57726752437506
        calc_poup = [ 6.17, 0.5 ]

        self.assertEqual(Func.tempo_double_poup(self, calc_poup), expected)

    def test_tempo_double_apl(self):
        rentab_cdi_ir = [ 77.5, 10.19 ]
        expected =  7.143198898832219
        self.assertEqual(Func.tempo_double_apl(self, rentab_cdi_ir), expected)



if __name__ == '__main__':
    unittest.main()
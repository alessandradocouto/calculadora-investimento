from tkinter import *
import tkinter as tk
from function import Func

root = Tk()

class Application(Func):
    

    def __init__(self):
        self.root = root
        # chamar a funcoes
        self.tela()
        self.frames_janela()
        root.mainloop()

    def tela(self):
        self.root.title("tkinter")
        self.root.configure(background="#cac3ba")
        self.root.geometry("450x600")
        self.root.resizable(False,False)
        
        # criar button calcular
        self.bt_calcular = Button(self.root, text="Calcular", 
        highlightthickness = 0, bd=0, bg="#f8fad7", fg="red", justify="center",
        font=("Times", 10, "bold"), cursor="hand2", command=self.janela2)
        self.bt_calcular.place(relx=0.42, rely=0.79, width=74, height=25)
        
        #  criacao label(arraste-me)
        self.lb_arrasta = Label(self.root, text="(arrasta-me para reposicionar a janela)",
        bg = "#cac3ba", fg="black")
        self.lb_arrasta.place(relx=0.2, rely=0.9)
    
    def frames_janela(self):
        
        # frame orange
        self.frame = Frame (self.root, bd=4, bg = "#ff6347",
        highlightbackground= "#add8e6", highlightthickness=4)
        self.frame.place(relx=0.11, rely=0.01, width=340, height=55)

        # criacao variaveis entry spinbox
        self._cap = tk.DoubleVar(value=1000)
        self._tx_selic = tk.DoubleVar(value=13.25)
        self._tx_cdi = tk.DoubleVar(value=13.15)
        self._tx_rent_cdi = tk.DoubleVar(value=100)
        self._num_meses = tk.IntVar(value = 1)
        self._optionIR = tk.DoubleVar(value=22.5)

        # criacao titulo orange label
        self.lb_capital = Label(self.frame, 
        text="CDBs, LCIs e LCAs indexadas por \n"
        "Certificados de Depósitos Interbancários",
         bg = "#ff6347", fg="black", justify="left", font=("Times", 12, "bold"))
        self.lb_capital.place(relx=0.02, rely=0.09)
                
        #  frame inputs/ labels
        self.frame2 = Frame (self.root, bd=3, bg = "#faebd7",
        highlightbackground= "#add8e6", highlightthickness=3)
        self.frame2.place(relx=0.08, rely=0.11, width=370, height=400)
    
        #  criacao labels(texto: Capital)
        self.lb_capital = Label(self.frame2, text="Capital:", bg = "#faebd7", fg="black")
        self.lb_capital.place(relx=0.03, rely=0.03)
        #  criacao labels(texto: $)
        self.lb_simbolo_cap = Label(self.frame2, text="$", bg = "#faebd7", fg="black")
        self.lb_simbolo_cap.place(relx=0.3, rely=0.03)
        #  criacao input Capital
        self.vcmd = (self.root.register(self._validate_float))
        self.capital = Spinbox(self.frame2, textvariable=self._cap,
        from_=0.0, to=100000000000.0, increment=0.01, format="%.2f",
        bg = "white", fg="black", width=20, validate="all",
        validatecommand=(self.vcmd, '%P'))
        self.capital.place(relx=0.35, rely=0.03)

        #  criacao labels(texto: selic)
        self.lb_selic = Label(self.frame2, text="Taxa Selic:", bg = "#faebd7", fg="black")
        self.lb_selic.place(relx=0.03, rely=0.14)
        #  criacao input selic
        self.vcmdselic = (self.root.register(self._validate_float))
        self.selic = Spinbox(self.frame2, textvariable=self._tx_selic,
        from_=0.0, to=10000.0, increment=0.01, format="%.2f",
        validate="all", validatecommand=(self.vcmdselic, '%P'),
        bg = "white", fg="black", width=6)
        self.selic.place(relx=0.35, rely=0.14)
        #  criacao labels(texto: % ao ano)
        self.lb_ano = Label(self.frame2, text="% ano", bg = "#faebd7", fg="black")
        self.lb_ano.place(relx=0.54, rely=0.14)


        #  criacao labels(texto: cdi)
        self.lb_cdi = Label(self.frame2, text="Taxa CDI:", bg = "#faebd7", fg="black")
        self.lb_cdi.place(relx=0.03, rely=0.25)
        #  criacao input cdi
        self.vcmdcdi = (self.root.register(self._validate_float))
        self.cdi = Spinbox(self.frame2, textvariable=self._tx_cdi,
        from_=0.0, to=10000.0, increment=0.01, format="%.2f",
        validate="all", validatecommand=(self.vcmdcdi, '%P'),
        bg = "white", fg="black",bd=0, width=6)
        self.cdi.place(relx=0.35, rely=0.25)
        self.lb_ano = Label(self.frame2, text="% ano", bg = "#faebd7", fg="black")
        self.lb_ano.place(relx=0.54, rely=0.25)


        #  criacao labels(texto: rentabilidade)
        self.lb_rentabilidade = Label(self.frame2, text="Rentabilidade:", 
        bg = "#faebd7", fg="black")
        self.lb_rentabilidade.place(relx=0.03, rely=0.35)
        #  criacao input rentabilidade
        self.vcmdrent = (self.root.register(self._validate_float))
        self.rent_cdi = Spinbox(self.frame2, textvariable=self._tx_rent_cdi,
        from_=0.0, to=10000.0, increment=0.01, format="%.2f",
        validate="all", validatecommand=(self.vcmdrent, '%P'),
        bg = "white", fg="black", width=6)
        self.rent_cdi.place(relx=0.35, rely=0.35)
        self.lb_prc_cdi = Label(self.frame2, text="% CDI", bg = "#faebd7", fg="black")
        self.lb_prc_cdi.place(relx=0.54, rely=0.35)

        #  criacao labels(texto: meses)
        self.lb_meses = Label(self.frame2, text="Meses:", bg = "#faebd7", fg="black")
        self.lb_meses.place(relx=0.03, rely=0.45)
        #  criacao input meses
        self.vcmdmeses = (self.root.register(self._validate_float))
        self.meses = Spinbox(self.frame2, textvariable=self._num_meses, from_=1, 
        to=10000, validate="all", validatecommand=(self.vcmdmeses, '%P'),
        increment=1,bg = "white", fg="black",width=4)
        self.meses.place(relx=0.35, rely=0.45)

        #  criacao labels(texto: Aliquota IR)
        self.lb_ir = Label(self.frame2, text="Aliquota IR:", bg = "#faebd7", fg="black")
        self.lb_ir.place(relx=0.03, rely=0.55)
        
        self.r1 = Radiobutton(self.frame2,text='0.0 (LAC ou LCI)', bg = "#faebd7", 
        fg="black", highlightthickness = 0, value=0.0, 
        variable=self._optionIR)
        self.r1.place(relx=0.07, rely=0.62)
        self.r2 = Radiobutton(self.frame2,text='15.0 (acima de 721 dias', bg = "#faebd7", 
        fg="black",highlightthickness = 0, value=15.0, 
        variable=self._optionIR)
        self.r2.place(relx=0.07, rely=0.68)
        self.r3 = Radiobutton(self.frame2,text='17.5 (de 361 até 720 dias)', bg = "#faebd7", 
        fg="black",highlightthickness = 0, value=17.5, 
        variable=self._optionIR)
        self.r3.place(relx=0.07, rely=0.74)
        self.r4 = Radiobutton(self.frame2,text='20.0 (de 181 até 360 dias)', bg = "#faebd7",
        fg="black", highlightthickness = 0, value=20.0, 
        variable=self._optionIR)
        self.r4.place(relx=0.07, rely=0.80)
        self.r5 = Radiobutton(self.frame2,text='22.5 (até 180 dias)', 
        bg = "#faebd7", fg="black", highlightthickness = 0, value=22.5, 
        highlightbackground= "#add8e6", variable=self._optionIR)
        self.r5.place(relx=0.07, rely=0.86) 

    def janela2 (self):
        self.root2 = Toplevel(root)
        self.root2.transient(root)
        self.root2.title("Rendimentos")
        self.root2.configure(background="#ffffff")
        self.root2.geometry("900x700")
        self.root2.resizable(False,False)
        self.root2.focus_force()
        self.root2.grab_set()
        # chamar funcao aqui
        self.frame_green()
        self.mostra_frame_green()
        self.frame_blue()
        self.mostra_frame_blue()
        self.frame_red()
        self.mostra_frame_red()
        
    def frame_green(self):      
        self.frame3 = Frame (self.root2, bg="#d3d3d3",
        highlightbackground= "green", highlightthickness=12)
        self.frame3.place(relx=0.02, rely=0.01, width=430, height=270)

    def mostra_frame_green(self):
        # resultado de capital
        self.lb_result_cap = Label(self.root2, 
        text= f"Capital: ${self._cap.get()}", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_cap.place(relx=0.05, rely=0.07)
        
        # resultado de tx selic
        self.lb_result_selic = Label(self.root2,
        text=f"Taxa Selic: {self._tx_selic.get()}% ao ano",
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_selic.place(relx=0.05, rely=0.11)

        # resultado de cdi
        self.lb_result_cdi = Label(self.root2, 
        text=f"CDI: {(self.calcular_cdi_juros(self._tx_cdi.get())[0]):.2f}% ao ano = {(self.calcular_cdi_juros(self._tx_cdi.get())[1]):.4f}% ao mês = {(self.calcular_cdi_juros(self._tx_cdi.get())[2]):.6f}% ao dia",
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_cdi.place(relx=0.05, rely=0.15)

        # resultado de taxa de poupança
        self.lb_result_poupanca = Label(self.root2, 
        text=f"Taxa Poupança: {self.mostra_poupanca(self.selic.get())}", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_poupanca.place(relx=0.05, rely=0.19)

        # resultado IR
        self.lb_result_ir = Label(self.root2, text=f"IR: {self._optionIR.get()}%", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_ir.place(relx=0.05, rely=0.23)

        # resultado de rentabilidade bruto
        self.lb_result_rentabilidade = Label(self.root2, 
        text=f"Rentabilidade:  {self._tx_rent_cdi.get():.2f}% CDI = {self.calculo_rent_bruta(self._tx_rent_cdi.get(), self._tx_cdi.get()):.2f} % ao ano", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_rentabilidade.place(relx=0.05, rely=0.27)
        
        # resultado de rentabilidade bruto Imposto
        self.lb_result_rentabilidade_ir = Label(self.root2,
        text=f"Com impostos:  {self.calculo_rent_com_IR(self._tx_rent_cdi.get(),self._tx_cdi.get(), self._optionIR.get())[0]:.2f}% CDI = {self.calculo_rent_com_IR(self._tx_rent_cdi.get(),self._tx_cdi.get(),self._optionIR.get())[1]:.2f}% ao ano", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_rentabilidade_ir.place(relx=0.05, rely=0.29)

        # resultado meses
        self.lb_result_meses = Label(self.root2, 
        text=f"Meses: {self.meses.get()}", 
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_meses.place(relx=0.05, rely=0.33)

    def frame_blue(self):
        self.frame3 = Frame (self.root2, bg="#d3d3d3",
        highlightbackground= "blue", highlightthickness = 12)
        self.frame3.place(relx=0.55, rely=0.01, width=300, height=220)
    
    def mostra_frame_blue(self):
        self.lb_result_mont_apl= Label(self.root2, 
        text=f"""Montante Aplicação = ${self.CDB(self._cap.get(),
        self.calculo_rent_bruta(self._tx_rent_cdi.get(), self._tx_cdi.get()),
        self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
        self._optionIR.get(),self._num_meses.get())[0]:.2f}""",
        bg="#d3d3d3", fg="black", font=("Times", 11, "bold"))
        self.lb_result_mont_apl.place(relx=0.6, rely=0.07)
        
        self.lb_result_mont_poup = Label(self.root2, 
        text=f"""Montante da Poupança = ${self.CDB(self._cap.get(),
        self.calculo_rent_bruta(self._tx_rent_cdi.get(), self._tx_cdi.get()),
        self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
        self._optionIR.get(),self._num_meses.get())[1]:.2f}""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_mont_poup.place(relx=0.6, rely=0.11)

        self.lb_result_dif_apl_poup = Label(self.root2, 
        text=f"""Apl - Poup ({self._num_meses.get()} meses ) = ${self.CDB(self._cap.get(),
        self.calculo_rent_bruta(self._tx_rent_cdi.get(), self._tx_cdi.get()),
        self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
        self._optionIR.get(),self._num_meses.get())[3]:.2f}""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_dif_apl_poup.place(relx=0.6, rely=0.15)

        self.lb_result_ir_apl_poup = Label(self.root2, 
        text=f"""Imposto = ${self.CDB(self._cap.get(),self.calculo_rent_bruta(
            self._tx_rent_cdi.get(), self._tx_cdi.get()),
            self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
            self._optionIR.get(),self._num_meses.get())[2]:.4f}""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_ir_apl_poup.place(relx=0.6, rely=0.19)

        self.lb_result_rend_mes = Label(self.root2, text=f"""Rendimento em {self._num_meses.get()} meses = {
            self.CDB(self._cap.get(),self.calculo_rent_bruta(
            self._tx_rent_cdi.get(), self._tx_cdi.get()),
            self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
            self._optionIR.get(),self._num_meses.get())[4]:.4f}%""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_rend_mes.place(relx=0.6, rely=0.23)
    
    def frame_red(self):
        self.frame3 = Frame (self.root2, bg="#d3d3d3",
        highlightbackground= "red", highlightthickness = 12)
        self.frame3.place(relx=0.13, rely=0.46, width=240, height=180)

    def mostra_frame_red(self):
        self.lb_result_saldo_apl_poup= Label(self.root2, 
        text=f"""Apl - Poup({self._num_meses.get()} meses) = {self.apl_dif_poup(
        self._cap.get(),self.CDB(self._cap.get(),
        self.calculo_rent_bruta(self._tx_rent_cdi.get(), self._tx_cdi.get()),
        self.calcular_poupanca(self._tx_selic.get()),self._tx_rent_cdi.get(),
        self._optionIR.get(),self._num_meses.get())):.4f}%""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_saldo_apl_poup.place(relx=0.16, rely=0.53)

        self.lb_result_poup_apl_cdi= Label(self.root2, 
        text=f"""Apl = Poup = {self.rent_poup_cdi(self._tx_cdi.get(), self._optionIR.get(),
            self.calcular_poupanca(self._tx_selic.get())):.2f}% CDI""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_poup_apl_cdi.place(relx=0.18, rely=0.57)

        self.lb_result_double_poup_cdi = Label(self.root2, 
        text=f"""Tempo 2 x Poupança = {self.tempo_double_poup(
        self.calcular_poupanca(self._tx_selic.get())):.2f} anos""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_double_poup_cdi.place(relx=0.15, rely=0.61)

        self.lb_result_double_cdi= Label(self.root2, 
        text=f"""Tempo 2 x Aplicação = {self.tempo_double_apl(
            self.calculo_rent_com_IR(self._tx_rent_cdi.get(), 
            self._tx_cdi.get(), self._optionIR.get())):.2f} anos""",
        bg="#d3d3d3", fg="black", font=("Times", 10, "bold"))
        self.lb_result_double_cdi.place(relx=0.15, rely=0.65)




def main():
    Application()

if __name__== "__main__":
    main()
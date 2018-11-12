#conding: utf-8

from kivy import Config

Config.set('graphics','multisamples','0')
Config.set('graphics','resizable','0')
Config.set('graphics','position','custom')
Config.set('graphics','top','100')
Config.set('graphics','left','350')


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from time import sleep
 
class Calcu(App):
  lista_ex = []
  _sinal = None
  def build(self):
    self.icon = 'calculadora_icone.png'

    layout = FloatLayout()

    #widget dos resultados
    area_text_1 = TextInput()
    area_text_1.multiline = True
    area_text_1.focus = False
    area_text_1.allow_copy = False
    area_text_1.font_size = '25sp'
    area_text_1.background_color = [255,255,255,1]
    area_text_1.readonly = True
    area_text_1._hint_text = '0'
    area_text_1.size_hint = (1.0,0.3333)
    area_text_1.pos_hint = {'x':0.0,'top':1.0}

    #widget Botões
    #um
    botao_1 = Button()
    botao_1.text = "1"
    botao_1.size_hint = (0.1666,0.1666)
    botao_1.pos_hint = {'x':0.0,'top':0.666}
    #dois
    botao_2 = Button()
    botao_2.text = "2"
    botao_2.size_hint = (0.1666,0.1666)
    botao_2.pos_hint = {'x':0.1666,'top':0.666}
    #três
    botao_3 = Button()
    botao_3.text = "3"
    botao_3.size_hint = (0.1666,0.1666)
    botao_3.pos_hint = {'x':0.333,'top':0.666}
    #quatro
    botao_4 = Button()
    botao_4.text = "4"
    botao_4.size_hint = (0.1666,0.1666)
    botao_4.pos_hint = {'x':0.0,'top':0.5}
    #cinco
    botao_5 = Button()
    botao_5.text = "5"
    botao_5.size_hint = (0.1666,0.1666)
    botao_5.pos_hint = {'x':0.1666,'top':0.5}
    #seis
    botao_6 = Button()
    botao_6.text = "6"
    botao_6.size_hint = (0.1666,0.1666)
    botao_6.pos_hint = {'x':0.333,'top':0.5}
    #sete
    botao_7 = Button()
    botao_7.text = "7"
    botao_7.size_hint = (0.1666,0.1666)
    botao_7.pos_hint = {'x':0.0,'top':0.333}
    #oito
    botao_8 = Button()
    botao_8.text = "8"
    botao_8.size_hint = (0.1666,0.1666)
    botao_8.pos_hint = {'x':0.1666,'top':0.333}
    #nove
    botao_9 = Button()
    botao_9.text = "9"
    botao_9.size_hint = (0.1666,0.1666)
    botao_9.pos_hint = {'x':0.333,'top':0.333}
    #zero
    botao_0 = Button()
    botao_0.text = "0"
    botao_0.size_hint = (0.333,0.1666)
    botao_0.pos_hint = {'x':0.0,'top':0.1666}
    #-----------------------------------------------
    #vírgula/ponto
    botao_ponto = Button()
    botao_ponto.text = "."
    botao_ponto.size_hint = (0.1666,0.1666)
    botao_ponto.pos_hint = {'x':0.333,'top':0.1666}
    #soma
    botao_soma = Button()
    botao_soma.text = "+"
    botao_soma.size_hint = (0.1666,0.1666)
    botao_soma.pos_hint = {'x':0.5,'top':0.666}
    #subtração
    botao_subtr = Button()
    botao_subtr.text = "-"
    botao_subtr.size_hint = (0.1666,0.1666)
    botao_subtr.pos_hint = {'x':0.666,'top':0.666}
    #multiplicação
    botao_mult = Button()
    botao_mult.text = "*"
    botao_mult.size_hint = (0.1666,0.1666)
    botao_mult.pos_hint = {'x':0.833,'top':0.666}
    #divisão
    botao_divs = Button()
    botao_divs.text = "/"
    botao_divs.size_hint = (0.1666,0.1666)
    botao_divs.pos_hint = {'x':0.5,'top':0.5}
    #parenteses
    botao_parent_l = Button()
    botao_parent_l.text = "("
    botao_parent_l.size_hint = (0.1666,0.1666)
    botao_parent_l.pos_hint = {'x':0.666,'top':0.5}

    botao_parent_r = Button()
    botao_parent_r.text = ")"
    botao_parent_r.size_hint = (0.1666,0.1666)
    botao_parent_r.pos_hint = {'x':0.833,'top':0.5}

    #resultado
    botao_resultado = Button()
    botao_resultado.text = "="
    botao_resultado.size_hint = (0.1666,0.1666)
    botao_resultado.pos_hint = {'x':0.5,'top':0.333}
    #apagar
    botao_apagar = Button()
    botao_apagar.text = "C"
    botao_apagar.size_hint = (0.1666,0.1666)
    botao_apagar.pos_hint = {'x':0.666,'top':0.333}
    
    botao_apagar_parte = Button()
    botao_apagar_parte.text = "<--"
    botao_apagar_parte.size_hint = (0.1666,0.1666)
    botao_apagar_parte.pos_hint = {'x':0.8333,'top':0.333}

    #funções---------------------------------------------

    def escreve_area_main(ins):
      def escreve_area_():
        if len(Calcu.lista_ex) > 0:
          if Calcu.lista_ex[-1] in ['+','-','*','/','.']:
            if ins.text in ['+','-','*','/','.']:
              Calcu.lista_ex.pop()
        Calcu._sinal = 0
        if ('.' in Calcu.lista_ex) and (ins.text == '.'):
          
          for _cc in Calcu.lista_ex[((len(Calcu.lista_ex)-(Calcu.lista_ex[::-1].index('.'))-1)+2):]:
            if _cc in ['+','-','*','/']:
              Calcu._sinal += 1
          if Calcu._sinal == 0:
            Calcu._sinal = -1
        Calcu.lista_ex.append(ins.text)
        if Calcu._sinal < 0:
          Calcu.lista_ex.pop()
        if Calcu.lista_ex[0] in ['+','-','*','/','.']:
          Calcu.lista_ex.insert(0,'0')  
          
        area_text_1.text = str(''.join(Calcu.lista_ex))
      return escreve_area_

    def escreve_area_resposta():
        
      lista_teste = ''.join(Calcu.lista_ex)
      try:
        lista_teste = eval(lista_teste)
      except:
        lista_teste = 'Erro'
        Calcu.lista_ex.clear()
        area_text_1.text = str(lista_teste)
        return
      area_text_1.text = str(lista_teste)
      Calcu.lista_ex = list(str(lista_teste))

    def apagar_area():
      Calcu.lista_ex.clear()
      area_text_1.text = str(''.join(Calcu.lista_ex))
    def apagar_expressao():

      if len(Calcu.lista_ex) >0:
        Calcu.lista_ex.pop()
      area_text_1.text = str(''.join(Calcu.lista_ex))

    #eventos------------------------------------------
    for _bb in range(10):
      exec("botao_{0}.on_press = escreve_area_main(botao_{0})".format(_bb))
    
    botao_soma.on_press = escreve_area_main(botao_soma)
    botao_subtr.on_press = escreve_area_main(botao_subtr)
    botao_mult.on_press = escreve_area_main(botao_mult)
    botao_divs.on_press = escreve_area_main(botao_divs)
    botao_parent_l.on_press = escreve_area_main(botao_parent_l)
    botao_parent_r.on_press = escreve_area_main(botao_parent_r)
    botao_ponto.on_press = escreve_area_main(botao_ponto)
    botao_resultado.on_press = escreve_area_resposta
    botao_apagar.on_press = apagar_area
    botao_apagar_parte.on_press = apagar_expressao
    #add_wiget-------------------------------------------
    #area de texto
    layout.add_widget(area_text_1)
    #botões na tela
    for _bb in range(10):
      exec("layout.add_widget(botao_{0})".format(_bb))
  
    layout.add_widget(botao_ponto)
    layout.add_widget(botao_soma)
    layout.add_widget(botao_subtr)
    layout.add_widget(botao_mult)
    layout.add_widget(botao_divs)
    layout.add_widget(botao_parent_l)
    layout.add_widget(botao_parent_r)
    layout.add_widget(botao_resultado)
    layout.add_widget(botao_apagar)
    layout.add_widget(botao_apagar_parte)
    return layout

from kivy.core.window import Window
Window.size = (250,400)
Window.fullscreen = False
Window.clearcolor = [0,1,0,0]#verde
Window.set_system_cursor('hand')
if __name__ == '__main__':
  Calcu(title="Calculadora").run()
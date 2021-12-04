class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print (valor)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    # adicionado os impostos no import
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador= Calculador_de_impostos()
    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ISS COM ICMS')
    calculador.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP()) # imprime 25.0
    calculador.realiza_calculo(orcamento, IKCV()) # imprime 30.0

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
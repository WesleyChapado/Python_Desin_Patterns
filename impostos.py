'''
class ICMS(object):
    def calcula(orcamento):
        return orcamento * 0.1

class ISS(object):
    def calcula(orcamento):
        return orcamento * 0.06'''

def calcula_ISS(orcamento):
    return orcamento.valor * 0.1

def calcula_ICMS(orcamento):
    return orcamento.valor * 0.06
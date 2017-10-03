'''
Estudo sobre classes
'''
class gata:
    def __init__ (self, nome, dono):
        self.n = nome #aqui dentro eu posso inicializar a classe como eu quiser
        self.dono = dono
        self.acordou = False
        self.dorme = False
    def anda(self):
        return print("Gata andando.")

    def acorda_dono(self):
        self.acordou = True
        return '{} acordando {}'.format(self.nome,
                                      self.dono)
    def dormindo(self):
        self.dorme = True
        self.acordou = False
        return '{} dormindo.'.format(self.n)

    @property
    def chata(self):
        if self.acordou == True:
            return True
        if self.dorme == True:
            return False
        else:
            return False

Sophie = gata('Sophie','Beatriz')
Sophie.anda()
Sophie.dormindo()
Sophie.chata

Sophie.acorda_dono()
Sophie.chata
Sophie.dormindo()
Sophie.chata

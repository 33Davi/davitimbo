class enc():
    def __init__(self, encf):
        self.encf = encf

class esc(enc):
    def __init__(self, encf):
        super().__init__(encf)
    def __str__(self):
         return (f'{self.encf}')

class vorf(enc):
    def __init__(self, encf, *args):
        super().__init__(encf)
        self.args = args

    def __str__(self,*args):
        kzn = f'{self.encf}\n'
        for arg in self.args:
            kzn += f'( ) {arg}\n'    
        return (kzn)


class mtpl(enc):
    def __init__(self, encf, **kwargs):
        super().__init__(encf)
        self.kwargs = kwargs

    def __str__(self, **kwargs):
        kzn = f'{self.encf}\n'
        for key, ib in self.kwargs:
            kzn += f'{key}. {ib}\n'    
        return (kzn)


if __name__ == '__main__':
    a = esc('Qual a fórmula da água?')
    print(a)
    print()
    b = vorf('O sistema solar tem oito planetas','verdadeiro', 'falso')
    print(b)
    print()
    c = mtpl('A órbita da Terra em Torno do Sol é:',a='Elíptica',b='circular',c='Hiperbolica',d='N.d.a.')
    print(c)

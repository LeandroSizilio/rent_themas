from .models import Theme, Rent
from datetime import datetime
from .models import Client

class Util:
    def CalcularDesconto(self, idCliente: int, idTema: int, rent: Rent = None):
        cliente = Client.objects.get(id=idCliente)
        desconto = 0

        contador_Rent = Rent.objects.filter(client=cliente).count()
        if contador_Rent > 0:
            desconto += 10
            print("Desconto:", desconto)

        if rent is not None:
            print("Rent date:")  # Removed .date here
            data_rent = rent.date
            if data_rent is not None:
                dia = data_rent.weekday()
                if dia in [0, 1, 2, 3]:  # segunda, terça, quarta, quinta
                    desconto += 40

        print("Desconto:", desconto) 

        tema = Theme.objects.get(id=idTema)
        valorTema = tema.price

        total = ((100-desconto)*valorTema)/100
        return total
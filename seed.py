import os, django, random
from bardapi import Bard

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from apps.viagens.models import  Depoimento
from apps.destinos.models import Destino

os.environ['_BARD_API_KEY'] = str(os.getenv('_BARD_API_KEY'))


def criando_depoimento(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(7561)

    for _ in range(quantidade_de_pessoas):
        prompt = f"Faça um depoimento sobra uma viagem para alguma cidade aleatória do brasil ou do mundo com no máximo 200 caracteres"
        nome = fake.name()
        depoimento = Bard().get_answer(prompt)['content']
        depoimento = depoimento.split('\n')[2]
        a = Depoimento(foto = "", nome=nome, depoimento=depoimento)
        a.save()


def criando_destinos(quantidade_de_destinos):
    fake = Faker()
    Faker.seed(123)

    for _ in range(quantidade_de_destinos):
        nome = fake.city()
        meta = f"Cideda de {nome}"
        preco = random.randrange(500, 1000)
        prompt = f"resumo sobre a cidade de {nome} em 200 caracteres"
        os.environ['_BARD_API_KEY'] = str(os.getenv('_BARD_API_KEY'))

        texto_descritivo = Bard().get_answer(prompt)['content']
        # Tive que por o while porque as respostas do Bard são bem ruins
        while texto_descritivo.startswith('Claro'):
            texto_descritivo = Bard().get_answer(prompt)['content']

        a = Destino(foto_1 = "", foto_2="", nome=nome, meta=meta, texto_descritivo=texto_descritivo, preco=preco)
        a.save()

#criando_depoimento(10)
criando_destinos(5)

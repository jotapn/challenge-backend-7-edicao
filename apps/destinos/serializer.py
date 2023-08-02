from rest_framework import serializers
from .models import Destino
from .validators import *
from dotenv import load_dotenv
import os, openai
from bardapi import Bard


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

    def validate(self, data):
        if texto_descritivo_valido(data['texto_descritivo']):
            load_dotenv()


            # UTILIZANDO O CHAT GPT (não utilizei por não possuir mais créditos):
            '''openai.api_key = os.getenv("OPENAI_API_KEY")
            model_engine = 'text-davinci-003'

            prompt = f"Faça um resumo sobre {data['nome']} enfatizando o porque este lugar é incrível. Utilize uma linguagem informal e até 100 caracteres no máximo em cada parágrafo. Crie 2 parágrafos neste resumo."

            completion = openai.Completion.create(
                engine= model_engine,
                prompt = prompt_chargpt,
                max_tokens = 1024,
                temperature = 0.5,
            )

            response = completion.choices[0].text '''      


            # UTILIZANDO O BARD
            prompt = f"resumo sobre a cidade de {data['nome']} em 200 caracteres"
            os.environ['_BARD_API_KEY'] = str(os.getenv('_BARD_API_KEY'))

            response = Bard().get_answer(prompt)['content']
            # Tive que por o while porque as respostas do Bard são bem ruins
            while response.startswith('Claro'):
                response = Bard().get_answer(prompt)['content']

            data['texto_descritivo'] = response
        return data

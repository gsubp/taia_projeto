# Conjunto de importacao
import csv
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class TwitterListener(StreamListener):
    # metodo de inicializacao
    def __init__(self):
        self.cont_tweet = 0
        self.max_tweets = 500

    def on_data(self, data):
        # incrementa o contador de tweets
        self.cont_tweet = self.cont_tweet + 1
        try:

            # converte o tweet para o formato json
            tweet = json.loads(data)
            user = tweet.get('user')
            print ("%i id: %i texto: %s" % (self.cont_tweet, tweet.get('id'), tweet.get('text')))

            # cria e carrega o arquivo 'twitter_data_csv.csv'
            meu_arquivo = open('twitter_data.csv', mode='a', encoding='utf-8')
            # cria o objeto writer para escrever no arquivo
            writer = csv.writer(meu_arquivo)
            # escreve os dados dos campos 'created_at' e 'text' no arquivo csv
            writer.writerow([tweet.get('id'), tweet.get('text'), tweet.get('created_at'), user.get('id_str')])

            # fecha a referencia para o arquivo
            meu_arquivo.close()
        except BaseException as erro:
            print('Erro: ' + erro)
        # condicaoo de parada
        if self.cont_tweet >= self.max_tweets:
            # retorne false
            return False


def coletar_tweets():
    # Complete aqui com o valor da "access_token" gerada para voce
    access_token = "2945304513-rggBh51pWbxyNsX1HEYx9sFc0gcQGVXfiUxqPzm"
    # Complete aqui com o valor da "access_token_secret" gerada para voce
    access_token_secret = "77vUYQZ0QLZRELvgta82nyFBj6c0JFZZORwtLdBo1dmyi"
    # Complete aqui com o valor da "consumer_key" gerada para voce
    consumer_key = "iPsRWYvRZuQZhLfFrYAPwVJpk"
    # Complete aqui com o valor da "consumer_secret" gerada para voce
    consumer_secret = "VSsQ6cDfTLeCaTIJ69God8RDyVB8OUACUNgbgnG1cfuOUOGs0K"

    tl = TwitterListener()
    oauth = OAuthHandler(consumer_key, consumer_secret)
    oauth.set_access_token(access_token, access_token_secret)

    stream = Stream(oauth, tl)
    stream.filter(track=['#ForaTemer', '#LavaJato', '#DiretasJa', '@jairbolsonaro', '@dilmabr'])


# chamada da funcao coletar_tweets()
coletar_tweets()

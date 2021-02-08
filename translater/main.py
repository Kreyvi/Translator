import json
import os

import requests
import telegram
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()



API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
API_TRANSLATE = '/v3/translate?version=2018-05-01/'
API_IDENTIFY = '/v3/identify?version=2018-05-01/'


def lang_detect(text):
    auth = IAMAuthenticator(API_KEY)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=auth
    )

    language_translator.set_service_url(API_URL)
    language = json.dumps(
        language_translator.identify(text).get_result(),
        indent=2
    )
    lang = json.loads(language)
    return lang['languages'][0]['language']


def translate(text, language):
    auth = IAMAuthenticator(API_KEY)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=auth
    )

    language_translator.set_service_url(API_URL)
    translation = language_translator.translate(
        text=text,
        model_id=f'{language}-ru').get_result()
    return json.dumps(translation, indent=2, ensure_ascii=False)


def main():
    text = input()
    answer = json.loads(translate(text, lang_detect(text)))
    print(answer['translations'][0]['translation'])


if __name__ == '__main__':
    main()



'''hello! what is your name? where is your brain?'''

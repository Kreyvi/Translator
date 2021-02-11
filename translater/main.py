import json
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
API_TRANSLATE = '/v3/translate?version=2018-05-01/'
API_IDENTIFY = '/v3/identify?version=2018-05-01/'


def lang_detect(text):
    # Language detection
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
    # Translation
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


def main(text):
    answer = json.loads(translate(text, lang_detect(text)))
    return answer['translations'][0]['translation']

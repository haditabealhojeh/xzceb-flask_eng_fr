
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    if english_text == "":
        return ""
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(frenchText):

    if frenchText == "":
        return ""
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    englishText=translation['translations'][0]['translation']
    return englishText

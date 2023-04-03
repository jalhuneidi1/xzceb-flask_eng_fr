'''
py
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# setting up watson intance, prepare the authenticator
# apikey and url obtained from Wastson instance created on IBM cloud
authenticator = IAMAuthenticator('MNucSok99jJxp2dWm8DZG_1aiW8F09EwpremWtf8YXw_')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/455fb491-cca0-474c-a1de-1580041859db')

def english_to_french(english_text):
    '''
    Takes english text as an input and return french translation as the output
    '''
    french_translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_translation.get("translations")[0].get("translation")
    return french_text

def french_to_english(french_text):
    '''
    Takes french text as an input and return english translation as the output
    '''
    english_translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_translation.get("translations")[0].get("translation")
    return english_text

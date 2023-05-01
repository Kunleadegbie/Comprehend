#*********************************************************************************************************************
# Author - Adekunle Adegbie
# This program demonstrates various AWS Comprehend APIs
# This is provided as part of my project without any warrenty. Use the code at your own risk.
# https://docs.aws.amazon.com/comprehend/latest/dg/functionality.html
#*********************************************************************************************************************

import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
text = "I am a highly motivated and detail-oriented Cloud Architect with over 3 years of experience in designing, deploying, and managing cloud-based solutions for small and medium-sized enterprises. Posséder de solides compétences en analyse et en résolution de problèmes, avec une expérience éprouvée dans la réalisation de projets réussis dans les délais et dans les limites du budget"

print("Calling DetectDominantLanguage")
print(json.dumps(comprehend.detect_dominant_language(Text = text), sort_keys=True, indent=4))

print('Calling DetectEntities')
print(json.dumps(comprehend.detect_entities(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectSentiment')
print(json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('Calling DetectSyntax')
print(json.dumps(comprehend.detect_syntax(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('All done\n')


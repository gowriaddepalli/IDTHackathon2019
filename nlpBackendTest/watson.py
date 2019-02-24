# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:03:29 2019

@author: Bhumi
"""


import random
import time
import json
import speech_recognition as sr
    
from urllib.request import Request, urlopen
from urllib.parse import urlencode

responses = []


def watson_tts (audio_file, model = 'en-US_NarrowbandModel'):
    
    from watson_developer_cloud import SpeechToTextV1 
    
    speech_to_text = SpeechToTextV1(
        iam_apikey=ibm_key,
        url='https://stream.watsonplatform.net/speech-to-text/api'
    )
    
    #models = speech_to_text.list_models().get_result()
    
    
    with open(audio_file,'rb') as audio_file:
        resp = speech_to_text.recognize(
                audio=audio_file,
                model=model,
                content_type='audio/wav',
                timestamps=True,
                speaker_labels = True,
                word_confidence=True).get_result()
        responses.append(resp)
        print(json.dumps(resp, indent=2))

    pt = []
    ps = []
    for d1 in resp['results']:
            for t in d1['alternatives']:
                pt.extend(t['timestamps'])
    
    ps.extend(resp['speaker_labels'])
        
    wl = list(zip(ps, pt))
    wl2 = []
    for w in wl:
        sp = w[0]['speaker']
        wd = w[1][0]
        wl2.append((sp, wd))
        
    final = []
    currsp = wl2[0][0]
    ph = ""
    for wd in wl2:
        if currsp == wd[0]:
            ph = ph+wd[1] + " "
        else:
            final.append((currsp, ph.strip()+"."))
            currsp = wd[0]
            ph = wd[1] + " "
    
    final.append((currsp, ph.strip()+"."))
    
    final2 = {}
    for s in final:
        if s[0] not in final2:
            final2[s[0]] = s[1]
        else:
            final2[s[0]] = final2[s[0]] + " " + s[1]

    print(final2)    
    return final2
    

watson_tts(audio_file = 'TOEFL_Listening.wav')#, model = 'es-ES_NarrowbandModel')

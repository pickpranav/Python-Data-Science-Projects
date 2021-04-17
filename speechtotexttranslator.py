Python 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def exampleFunction(stringie)
SyntaxError: invalid syntax
>>> def exampleFunction(stringie):
	return(stringie)

>>> exampleFunction("loser")
'loser'
>>> from ibm_watson import SpeechToTextV1
>>> import json
>>> from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
>>> url_s2t = "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/bde8631c-2863-46b2-90d9-e9b07633a4cc"
>>> iam_apikey_s2t = "L_ahYdaLfstjQz3yoSFD-hAJMbIdFAA30hp9JOBzLdvZ"
>>> authenticator = IAMAuthenticator(iam_apikey_s2t)
>>> s2t = SpeechToTextV1(authenticator=authenticator)
>>> s2t.set_service_url(url_s2t)
>>> s2t
<ibm_watson.speech_to_text_v1_adapter.SpeechToTextV1Adapter object at 0x7ff3ea7e62b0>
>>> >>> def exampleFunction(stringie)
SyntaxError: invalid syntax
>>> def exampleFunction(stringie):
	return(stringie)

>>> exampleFunction("loser")
'loser'
>>> from ibm_watson import SpeechToTextV1
>>> import json
>>> from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
>>> url_s2t = "https://api.us-south.speech-to-text.
SyntaxError: invalid syntax
>>> def TextToSpeechTranslatorSpanish(filename):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')

	    
>>> def TextToSpeechTranslatorSpanish(filename):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	type(recognized_text)
	from ibm_watson import LanguageTranslatorV3

	
>>> from ibm_watson import LanguageTranslatorV3
>>> url_lt='https://api.us-south.language-translator.watson.cloud.ibm.com/instances/0636263c-6270-476f-9771-74540ac9d398'
>>> apikey_lt='FnK4BiNqRQTeG1lC7L9Bv1gfNnG-LhQu5guNf3p1EJIR'
>>> version_lt='2018-05-01'
>>> authenticator = IAMAuthenticator(apikey_lt)
>>> language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
>>> language_translator.set_service_url(url_lt)
>>> language_translator
<ibm_watson.language_translator_v3.LanguageTranslatorV3 object at 0x7ff3ecb7ab80>
>>> from pandas.io.json import json_normalize
>>> json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

Warning (from warnings module):
  File "<pyshell#36>", line 1
FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
   language                 name
0        af            Afrikaans
1        ar               Arabic
2        az          Azerbaijani
3        ba              Bashkir
4        be           Belarusian
..      ...                  ...
71       uk            Ukrainian
72       ur                 Urdu
73       vi           Vietnamese
74       zh   Simplified Chinese
75    zh-TW  Traditional Chinese

[76 rows x 2 columns]
>>> def TextToSpeechTranslatorSpanish(filename):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	translation=translation_response.get_result()
	spanish_translation =translation['translations'][0]['translation']
	return spanish_translation

>>> fName1 = '/Users/ranbarasan/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/sampleUno.mp3'
>>> TextToSpeechTranslatorSpanish(fName1)

Warning (from warnings module):
  File "<pyshell#41>", line 5
FutureWarning: pandas.io.json.json_normalize is deprecated, use pandas.json_normalize instead
'hi mi nombre es Pranab garage y tengo diecisiete años de edad '
>>> def TextToSpeechTranslator(filename, language):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	if (language == 'Spanish'):
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	elif (language == 'Tamil):
	      
SyntaxError: EOL while scanning string literal
>>> def TextToSpeechTranslator(filename, language):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	if (language == "Spanish"):
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	elife (language == "Tamil"):
		
SyntaxError: invalid syntax
>>> def TextToSpeechTranslator(filename, language):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	if (language == "Spanish"):
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	elif language == "Tamil" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-ta')
	elif language == "Hindi" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-hi')
	else:
		return "This language is not currently supported"
	translation= translation_response.get_result()
	f_translation =translation['translations'][0]['translation']
	return f_translation

>>> TextToSpeechTranslator(fName1, Spanish)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    TextToSpeechTranslator(fName1, Spanish)
NameError: name 'Spanish' is not defined
>>> TextToSpeechTranslator(fName1, "Spanish")
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1347, in getresponse
    response.begin()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 307, in begin
    version, status, reason = self._read_status()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 268, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/socket.py", line 704, in readinto
    return self._sock.recv_into(b)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [Errno 54] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/util/retry.py", line 532, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/packages/six.py", line 734, in reraise
    raise value.with_traceback(tb)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1347, in getresponse
    response.begin()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 307, in begin
    version, status, reason = self._read_status()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 268, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/socket.py", line 704, in readinto
    return self._sock.recv_into(b)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    TextToSpeechTranslator(fName1, "Spanish")
  File "<pyshell#60>", line 3, in TextToSpeechTranslator
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/ibm_watson/speech_to_text_v1.py", line 506, in recognize
    response = self.send(request)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/ibm_cloud_sdk_core/base_service.py", line 281, in send
    response = self.http_client.request(**request,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/adapters.py", line 498, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
>>> def TextToSpeechTranslator(filename, str language):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	if (language == "Spanish"):
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	elif language == "Tamil" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-ta')
	elif language == "Hindi" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-hi')
	else:
		return "This language is not currently supported"
	translation= translation_response.get_result()
	f_translation =translation['translations'][0]['translation']
	return f_translation
SyntaxError: invalid syntax
>>> def TextToSpeechTranslator(filename, language):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	if (language == "Spanish"):
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-es')
	elif language == "Tamil" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-ta')
	elif language == "Hindi" :
		translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-hi')
	else:
		return "This language is not currently supported"
	translation= translation_response.get_result()
	f_translation =translation['translations'][0]['translation']
	return f_translation

>>> TextToSpeechTranslator(fName1,Spanish)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    TextToSpeechTranslator(fName1,Spanish)
NameError: name 'Spanish' is not defined
>>> spanish = "Spanish"
>>> tamil = "Tamil"
>>> hindi = "Hindi"
>>> TextToSpeechTranslator(fName1, spanish)
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1347, in getresponse
    response.begin()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 307, in begin
    version, status, reason = self._read_status()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 268, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/socket.py", line 704, in readinto
    return self._sock.recv_into(b)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [Errno 54] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 755, in urlopen
    retries = retries.increment(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/util/retry.py", line 532, in increment
    raise six.reraise(type(error), error, _stacktrace)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/packages/six.py", line 734, in reraise
    raise value.with_traceback(tb)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 699, in urlopen
    httplib_response = self._make_request(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 445, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/urllib3/connectionpool.py", line 440, in _make_request
    httplib_response = conn.getresponse()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1347, in getresponse
    response.begin()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 307, in begin
    version, status, reason = self._read_status()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 268, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/socket.py", line 704, in readinto
    return self._sock.recv_into(b)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    TextToSpeechTranslator(fName1, spanish)
  File "<pyshell#65>", line 8, in TextToSpeechTranslator
    translation_response = language_translator.translate(\
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/ibm_watson/language_translator_v3.py", line 191, in translate
    response = self.send(request)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/ibm_cloud_sdk_core/base_service.py", line 281, in send
    response = self.http_client.request(**request,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/requests/adapters.py", line 498, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))
>>> def TextToSpeechTranslatorTamil(filename):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-ta')
	translation=translation_response.get_result()
	tamil_translation =translation['translations'][0]['translation']
	return tamil_translation

>>> TextToSpeechTranslatorTamil(fName1)
'இன ் பெயர ் நான ் என ் பெயர ், நான ் பதின ் ஆண ் டேன ். '
>>> def TextToSpeechTranslatorHindi(filename):
	with open(filename, mode="rb")  as wav:
	    response = s2t.recognize(audio=wav, content_type='audio/mp3')
	from pandas.io.json import json_normalize
	json_normalize(response.result['results'],"alternatives")
	recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
	translation_response = language_translator.translate(\
	    text=recognized_text, model_id='en-hi')
	translation=translation_response.get_result()
	hindi_translation =translation['translations'][0]['translation']
	return hindi_translation

>>> TextToSpeechTranslatorSpanish(fName1)
'hi mi nombre es Pranab garage y tengo diecisiete años de edad '
>>> TextToSpeechTranslatorTamil(fName1)
'இன ் பெயர ் நான ் என ் பெயர ், நான ் பதின ் ஆண ் டேன ். '
>>> TextToSpeechTranslatorHindi(fName1)
'हाय मेरा नाम प्रणव गैरेज है और मैं सत्रह साल का हूँ '
>>> fileName100 = '/Users/ranbarasan/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/mummySample.mp3'
>>> TextToSpeechTranslatorTamil(fName2)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    TextToSpeechTranslatorTamil(fName2)
NameError: name 'fName2' is not defined
>>> TextToSpeechTranslatorTamil(fileName100)
'என் பெயர் '
>>> TextToSpeechTranslatorHindi(fileName100)
'हाय मेरा नाम है '
>>> 
>>> 
from googletrans import Translator

tr = Translator(service_urls=[
      'translate.google.com',
    ])

def a():
    return tr.translate('你好')

print(a())

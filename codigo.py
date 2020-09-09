from nltk.tokenize.treebank import TreebankWordDetokenizer
import spacy
tratarTX = spacy.load('pt_core_news_lg')

spacy.__version__

entrada = tratarTX('3730061 - led,0603,red,smd,dcs-c0603r-z01,dechangshun, marca intelbras partnumber 3730029 - po - 439.963 - diodo emissor luz (led), montado, smd, montagem superficie, cor vermelho - partnumber - 3730061')

listagem = [token.text for token in entrada if not token.is_punct if token.pos_ != 'NUM']
listagem = TreebankWordDetokenizer().detokenize(listagem)
entrada = tratarTX(listagem)
PROPN = [token.lemma_ for token in entrada if token.pos_ == 'PROPN']
PROPN = TreebankWordDetokenizer().detokenize(PROPN)
ADJ = [token.lemma_ for token in entrada if token.pos_ == 'ADJ']
ADJ = TreebankWordDetokenizer().detokenize(ADJ)
VERB = [token.lemma_ for token in entrada if token.pos_ == 'VERB']
VERB = TreebankWordDetokenizer().detokenize(VERB)
NOUN = [token.lemma_ for token in entrada if token.pos_ == 'NOUN']
NOUN = TreebankWordDetokenizer().detokenize(NOUN)

print('FRASE : ' + PROPN + ADJ + VERB + NOUN)

entidades = entrada.ents
print('ENTIDADES: ' + str(entidades))
org = [(entidade,entidade.label_) for entidade in entrada.ents if entidade.label_ == 'ORG']
print('ORGANIZAÇÃO: ' + str(org))


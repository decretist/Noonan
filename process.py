#!/usr/local/bin/python3
#
# Paul Evans (pevans@sandiego.edu)
# 13 June 2018
#
import sys

# allow

kestemont_allow = [
    'a',        # preposition
    'ad',       # preposition
    'ante',     # preposition
    'apud',     # preposition
    'atque',    # conjunction
    'aut',      # conjunction
    'autem',    # conjunction
    'contra',   # preposition, adverb
    'cum',      # preposition, conjunction
    'de',       # preposition
    'dum',      # conjunction
    'enim',     # conjunction
    'ergo',     # adverb
    'et',       # conjunction
    'etiam',    # adverb
    'hic'       # adverb
    'idem',     # pronoun
    'in',       # preposition
    'inter',    # preposition
    'ita',      # adverb
    'licet',    # conjunction
    'ne',       # conjunction, adverb
    'nec',      # conjunction
    'nisi',     # conjunction
    'non',      # adverb
    'nunc',     # adverb
    'per',      # preposition
    'post',     # preposition, adverb
    'pro',      # preposition
    'propter',  # preposition
    'quam',     # conjunction
    'qui',      # relative pronoun
    'quia',     # conjunction
    'quod',     # conjunction
    'quoque',   # conjunction
    'sed',      # conjunction
    'si',       # conjunction
    'sic',      # adverb
    'sicut',    # adverb
    'sine',     # preposition
    'siue',     # conjunction
    'super',    # adverb, preposition
    'tamen',    # adverb
    'tunc',     # adverb
    'uel',      # conjunction
    'uidelicet',# adverb
    'unde',     # adverb
    'ut',       # adverb, conjunction
    'xque',     # conjunction
]

adverbs = [
    'aliqua',   # adverb
    'aliquando',# adverb
    'contra',   # preposition, adverb
    'ecce',     # adverb
    'ergo',     # adverb
    'etiam',    # adverb
    'forte',    # adverb
    'generaliter',      # adverb
    'hic',      # adverb
    'ideo',     # adverb
    'infra',    # adverb, preposition
    'ita',      # adverb
    'item',     # adverb
    'ne',       # conjunction, adverb
    'non',      # adverb
    'nunc',     # adverb
    'post',     # preposition, adverb
    'postea',   # adverb
    'prius',    # adverb
    'quando',   # conjunction, adverb
    'quo',      # adverb
    'quomodo',  # adverb
    'sic',      # adverb
    'sicut',    # adverb
    'similiter',# adverb
    'super',    # adverb, preposition
    'supra',    # adverb, preposition
    'tamen',    # adverb
    'tunc',     # adverb
    'uero',     # adverb
    'uidelicet',# adverb
    'unde',     # adverb
    'ut',       # adverb, conjunction
]

conjunctions = [
    'an',       # conjunction
    'atque',    # conjunction
    'aut',      # conjunction
    'autem',    # conjunction
    'cum',      # preposition, conjunction
    'dum',      # conjunction
    'enim',     # conjunction
    'et',       # conjunction
    'etsi',     # conjunction
    'itaque',   # conjunction
    'licet',    # conjunction
    'nam',      # conjunction
    'namque',   # conjunction
    'ne',       # conjunction, adverb
    'nec',      # conjunction
    'nisi',     # conjunction
    'quam',     # conjunction
    'quamuis',  # conjunction
    'quando',   # conjunction, adverb
    'quia',     # conjunction
    'quod',     # conjunction
    'quoque',   # conjunction
    'sed',      # conjunction
    'si',       # conjunction
    'siue',     # conjunction
    'uel',      # conjunction
    'ut',       # adverb, conjunction
    'xque',     # conjunction
]

prepositions = [
    'a',        # preposition
    'ab',       # preposition
    'ad',       # preposition
    'ante',     # preposition
    'apud',     # preposition
    'contra',   # preposition, adverb
    'cum',      # preposition, conjunction
    'de',       # preposition
    'ex',       # preposition
    'in',       # preposition
    'infra',    # adverb, preposition
    'infra',    # adverb, preposition
    'inter',    # preposition
    'iuxta',    # preposition
    'per',      # preposition
    'post',     # preposition, adverb
    'pro',      # preposition
    'propter',  # preposition
    'secundum', # preposition, adjective
    'sine',     # preposition
    'super',    # adverb, preposition
    'supra',    # adverb, preposition
    'supra',    # adverb, preposition
]

# deny

kestemont_deny = ['aliqui', 'alius', 'amicus', 'angelus', 'anima',
    'audio', 'beatus', 'bonum', 'bonus', 'cado', 'caritas', 'caro',
    'causa', 'celestis', 'celum', 'certus', 'ceterus', 'christus',
    'consilium', 'cor', 'corpus', 'debeo', 'deus', 'dico', 'dies',
    'diligo', 'diuinus', 'do', 'dominus', 'domus', 'duo', 'ecclesia',
    'ego', 'episcopus', 'eternus', 'facio', 'fidelis', 'fides',
    'filius', 'fors', 'frater', 'fratres', 'gloria', 'gratia',
    'habeo', 'hildegars', 'homo', 'honor', 'ideo', 'ille', 'inuenio',
    'is', 'iste', 'iudicium', 'iustitia', 'iustus', 'lex', 'locus',
    'loquor', 'magnus', 'malum', 'manus', 'mens', 'meus', 'misericordia',
    'modus', 'mors', 'multus', 'mundus', 'nam', 'nihil', 'nomen',
    'noster', 'nouus', 'nullus', 'o', 'oculus', 'omnis', 'opus',
    'os', 'pars', 'paruus', 'pater', 'pax', 'peccatum', 'pono',
    'populus', 'possum', 'potior', 'predico', 'primus', 'prior',
    'quero', 'quidam', 'quis', 'quomodo', 'res', 'rex', 'salus',
    'sanctus', 'scio', 'secundum', 'similis', 'sol', 'solus',
    'spiritus', 'sui', 'sum', 'summus', 'suus', 'ta', 'talis',
    'tantum', 'tempus', 'terra', 'totus', 'tu', 'tuus', 'uenio',
    'uerbum', 'ueritas', 'uerus', 'uester', 'uia', 'uideo', 'uir',
    'uirtus', 'uis', 'uita', 'uiuo', 'unus', 'uolo', 'uoluntas',
    'uox', 'us']

adjectives = ['alia', 'alii', 'aliis', 'aliud', 'alterius', 'bonum',
    'nulla', 'nulli', 'omnia', 'omnibus', 'primum', 'prius',
    'propria', 'sacris', 'secundo', 'secundum', 'solum', 'suum',
    'tantum', 'tolletano', 'uerum']

nouns = ['accusatione', 'ambrosius', 'apostolus', 'auctoritas',
    'auctoritate', 'auctoritatibus', 'augustini', 'augustinus',
    'bomum', 'canonibus', 'capitulo', 'causa', 'christi', 'christus',
    'clericis', 'concilii', 'concilio', 'coniugium', 'consensu',
    'crimen', 'dei', 'deo', 'deus', 'dictum', 'domini', 'domino',
    'dominus', 'ecclesia', 'ecclesiae', 'ecclesiam', 'episcopi',
    'episcopis', 'episcopo', 'episcoporum', 'episcopum', 'episcopus',
    'epistola', 'exemplo', 'fide', 'filii', 'filios', 'gelasius',
    'gregorii', 'gregorius', 'hereticis', 'ieronimus', 'iudicium',
    'iure', 'ius', 'lege', 'leo', 'libro', 'modo', 'nichil',
    'offitio', 'ordinibus', 'papa', 'papae', 'peccata', 'peccati',
    'peccato', 'peccatum', 'penitencia', 'penitenciam', 'potestatem',
    'rebus', 'res', 'sacerdotes', 'sacerdotibus', 'sacramenta',
    'sententia', 'sententiam', 'sinodo', 'statutum', 'tempore',
    'titulo', 'uerum', 'uiro', 'uitae', 'uxorem']

pronouns = ['aliqua', 'aliquid', 'aliquis', 'cui', 'cuius', 'eodem',
    'hac', 'hanc', 'hec', 'hic', 'hinc', 'his', 'hoc', 'idem',
    'ipsa', 'qua', 'que', 'quem', 'qui', 'quibus', 'quid', 'quidam',
    'quis', 'quorum', 'quos', 'se', 'sibi', 'uobis', 'uos']

pronouns_deleted = ['ea', 'eam', 'ei', 'eis', 'eius', 'eo', 'eorum',
    'eos', 'eum', 'id', 'illa', 'ille', 'illi', 'illis', 'illo',
    'illud', 'sua', 'suae', 'suam', 'sui', 'suis', 'suo', 'suorum']

verbs = ['ait', 'apparet', 'colligitur', 'datur', 'debent', 'debet',
    'dicens', 'dicitur', 'erat', 'esse', 'esset', 'est', 'facit',
    'fieri', 'fuerint', 'fuerit', 'habere', 'habet', 'intelligendum',
    'intelligi', 'intelligitur', 'inuenitur', 'legitur', 'liceat',
    'obicitur', 'oportet', 'patet', 'permittitur', 'posse', 'possit',
    'possunt', 'poterit', 'potest', 'premissis', 'probantur',
    'probatur', 'prohibentur', 'prohibetur', 'queritur', 'respondetur',
    'scribens', 'scribit', 'sint', 'sit', 'sunt', 'testatur',
    'ualet', 'uidetur']

other = ['b', 'etc', 'ii']

def main():
    allow = adverbs + conjunctions + prepositions
    deny = adjectives + nouns + pronouns + pronouns_deleted + verbs + other
    wordlist = 'wordlist.txt'
    with open(wordlist, 'r') as f:
        words = f.readlines()
    words = [word.rstrip() for word in words]
    for word in words:
        # warnings
        if word not in allow and word not in deny:
            print('warning: ' + word + ' not in allow and not in deny', file=sys.stderr)
        if word in allow and word in deny:
            print('warning: ' + word + ' in allow and in deny', file=sys.stderr)
            allow.remove(word)
        if word in kestemont_allow and word in deny:
            print('warning: ' + word + ' in kestemont_allow and in deny', file=sys.stderr)
        if word in allow and word in kestemont_deny:
            print('warning: ' + word + ' in allow and in kestemont_deny', file=sys.stderr)

        if word in allow:
        # if word not in deny:
            print(word)
        if word in deny:
            if word in pronouns_deleted:
                print('#' + word + '*')
            else:
                print('#' + word)

if __name__ == '__main__':
    main()


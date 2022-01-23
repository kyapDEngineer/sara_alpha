options = {
    'ka': '\u0F40',
    'kha': '\u0F41',
    'ga': '\u0F42',
    'gha': '\u0F43',

    'nga': '\u0F44',
    'ca': '\u0F45',
    'cha': '\u0F46',
    'ja': '\u0F47',

    'nya': '\u0F49',
    'tta': '\u0F4A',
    'ttha': '\u0F4B',
    'dda': '\u0F4C',

    'ddha': '\u0F4D',
    'nna': '\u0F4E',
    'ta': '\u0F4F',
    'tha': '\u0F50',

    'da': '\u0F51',
    'dha': '\u0F52',
    'na': '\u0F53',
    'pa': '\u0F54',

    'pha': '\u0F55',
    'ba': '\u0F56',
    'bha': '\u0F57',
    'ma': '\u0F58',

    'tsa': '\u0F59',
    'tsha': '\u0F5A',
    'dza': '\u0F5B',
    'dzha': '\u0F5C',

    'wa': '\u0F5D',
    'zha': '\u0F5E',
    'za': '\u0F5F',
    '-a': '\u0F60',

    'ya': '\u0F61',
    'ra': '\u0F62',
    'la': '\u0F63',
    'sha': '\u0F64',

    'ssa': '\u0F65',
    'sa': '\u0F66',
    'ha': '\u0F67',
    'a': '\u0F68',
    # kssa
    'kssa': '\u0F69',
    #Used only in transliteration and transcription
    'fixra': '\u0F6A',

    # syllable
    'om': '\u0F00',

    # head marks
    'aa': '\u0F01',
    'adma': '\u0F02',
    'egma': '\u0F03',
    'unma': '\u0F04',
    'abma': '\u0F05',
    'hadma': '\u0F06',
    'shadma': '\u0F07',

    # marks and signs
    'sbrul': '\u0F08',
    'bskur': '\u0F09',
    'bka': '\u0F0A',
    'inters': '\u0F0B',
    'bstar': '\u0F0C',
    'shey': '\u0F0D',
    'nyis': '\u0F0E',
    'tsheg': '\u0F0F',
    'isse': '\u0F10',
    'rin': '\u0F11',
    'rgya': '\u0F12',
    'caret': '\u0F13',
    'gter': '\u0F14',
    'dusrtags': '\u0F34',
    'nyizla': '\u0F35',
    'migcan': '\u0F36',
    'gorrtags': '\u0F37',
    'chemgo': '\u0F38',
    'tsaphru': '\u0F39',

    # astrological signs
    'chad': '\u0F15',
    'lhag': '\u0F16',
    'char': '\u0F17',
    'khyud': '\u0F18',
    'sdong': '\u0F19',
    'gcig': '\u0F1A',
    'gnyis': '\u0F1B',
    'gsum': '\u0F1C',
    'ngcig': '\u0F1D',
    'ngnyis': '\u0F1E',
    'dkar': '\u0F1F',

    'yartshes': '\u0F3E',
    'martshes': '\u0F3F',

    # digits
    'zero': '\u0F20',
    'one': '\u0F21',
    'two': '\u0F22',
    'three': '\u0F23',
    'four': '\u0F24',
    'five': '\u0F25',
    'six': '\u0F26',
    'seven': '\u0F27',
    'eight': '\u0F28',
    'nine': '\u0F29',

    # paired punctuation
    'gugrgyon': '\u0F3A',
    'gugrgyas': '\u0F3B',
    'anggyon': '\u0F3C',
    'anggyas': '\u0F3D',

    #extensions for balti
    'kka': '\u0F6B',
    'rra': '\u0F6B',

    #dependent vowel signs
    'achug': '\u0F71',
    'D': '\u0F72',
    'Di': '\u0F73',
    'F': '\u0F74',
    'Fi': '\u0F75',
    'vocalR': '\u0F76',
    'vocalRR': '\u0F77',
    'vocalL': '\u0F78',
    'vocalLL': '\u0F79',
    'J': '\u0F7A',
    'JJ': '\u0F7B',
    'K': '\u0F7C',
    'KK': '\u0F7D',

    # vocalic modification
    'anusvara': '\u0F7E',
    'visarga': '\u0F7F',

    # dependent vowel signs
    'reversedD': '\u0F80',
    '': '\u',

    # subjoined consonants
    'ska': '\u0F90',

    # dependent vowel signs
    'U': '\u0F74'

    #
}

word = input('enter the word = ')
word_2 = input('enter the second word = ')
word_3 = input('enter the third word = ')

if word or word_2 or word_3 in options:
    first_word = options.get(word, word)
    second_word = options.get(word_2, word_2)
    third_word = options.get(word_3, word_3)
    print("".join([first_word, second_word, third_word]))

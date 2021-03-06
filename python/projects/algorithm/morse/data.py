from audio import *
def logic():
    def morse():
        message = ' '.join(a for a in audio_get())
        morse_gen = ''
        for q in list(message.upper()):
            morse_gen += data['abs'][q]
        return morse_gen, message
    data = {
                'abs' :  {
                        'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-', ' ': ' '
                        },
                'pauses' : {
                        ' '     :   0.75,
                        '.'     :   0.25,
                        '-'     :   0.75
                        }
                }

    buffer = morse()

    for i in buffer[0]:
        audio_gen(temp=data['pauses'][i])
    return 'text:\t' + buffer[1] + '\nmorse:\t' + buffer[0]

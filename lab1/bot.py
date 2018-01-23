from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
print('hi')


@module.rule('')

def hi(bot, trigger):
    print(trigger)
    print(emo.detect_emotion_in_raw_np(trigger))
    bot.say('cool !' + trigger.nick)
    array = emo.detect_emotion_in_raw_np(trigger)
    print array.tolist()


    
	
#print(emo.detect_emotion_in_raw_np("hello"))





@module.rule('b')
@module.rule('c')
@module.rule('d')
@module.rule('e')
@module.rule('f')
@module.rule('g')
@module.rule('h')
@module.rule('i')
@module.rule('j')
@module.rule('k')
@module.rule('l')
@module.rule('m')
@module.rule('n')
@module.rule('n')
@module.rule('o')
@module.rule('p')
@module.rule('q')
@module.rule('r')
@module.rule('s')
@module.rule('t')
@module.rule('u')
@module.rule('v')
@module.rule('w')
@module.rule('x')
@module.rule('y')


  




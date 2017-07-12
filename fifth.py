import random
question =raw_input("Please ask the 8 ball a question: ")

array = question.split(" ")
#print array

last_word= len(array)-1
#print array[last_word]

responses = ['It is certain','It is decidedly so','Without a doubt',
	    'Yes definitely','You may rely on it','As I see it, yes',
	    'Most likely','Outlook good','Yes','Signs point to yes',
	    'Reply hazy try again','Better not tell you now',
	    'Cannot predict now','Concentrate and ask again',
	    'Do not count on it','My reply is no','My sources say no',
	    'Outlook not so good','Very doubtful']

if array[last_word].endswith("?")== True :
    print "yes"

    num = random.randint(0,len(responses))
    #print num
    print "The 8 ball reads: " + responses[num]+"."

    

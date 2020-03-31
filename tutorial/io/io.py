# standard
age = int(input( 'Enter your age in years: '))
max_heart_rate = 206.9 - (0.67* age) # as per Med Sci Sports Exerc.
target = 0.65* max_heart_rate
print( 'Your target fat-burning heart rate is' , target)

#files
fp = open('asd.txt','w')
fp.write('بسم الله الرحمن الرحيم')
fp.seek(0)
fp.write('asd \n')
fp.close()
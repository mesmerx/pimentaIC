n=1000 #number of intervals
max=2. #max value
min=-2. #min value
width=(max-min)/n #interval width
#function used to map a value to the intervals
hist(x,width)=width*floor(x/width)+width/2.0
set boxwidth width*0.9

#count and plot
plot "autogaussian1000-5.txt" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"green" notitle,sqrt(1-x**2)

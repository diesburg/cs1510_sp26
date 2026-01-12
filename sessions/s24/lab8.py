def hydrocarbon(hydrogen, carbon, oxygen):
	if hydrogen<0 or oxygen<0 or carbon<0:
		return None
	return hydrogen*1.0079+carbon*12.011+oxygen*15.9994

def bmi(weight,height):
	if weight<=0 or height<=0:
		return None
	return weight*0.453592/(height*0.0254)**2

def collatzLength(seed):
	count=0
	
	#error check
	if seed<1:
		return None

	#actually perform simulation
	while seed>1:
		count += 1
		if seed%2==0:
			seed=seed/2
		else:
			seed=seed*3+1
	return count

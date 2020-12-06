def convert(number):
	map_ = {
			3: 'Pling',
			5: 'Plang',
			7: 'Plong'
		}
	r_str = [v for k, v in map_.items() if number % k == 0]
	return ''.join(r_str) if r_str else str(number)

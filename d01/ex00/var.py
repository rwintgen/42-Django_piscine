def my_var():
	var_int = 42
	var_string_char = "42"
	var_string_num = "quarante-deux"
	var_float = 42.0
	var_bool = True
	var_list = [42]
	var_dict = {42: 42}
	var_tuple = (42,)
	var_set = set()

	variables = [var_int, var_string_char, var_string_num, var_float,
			  var_bool, var_list, var_dict, var_tuple, var_set]
	
	for var in variables:
		print(f"{var} has a type {type(var)}")
	
if __name__ == '__main__':
	my_var()
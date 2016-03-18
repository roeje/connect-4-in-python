import cPickle as pickle


class IO:
	def __init__ (self):
		return

	def save_obj (self, obj, file_name, t):
		file = open(file_name, t)	
		pickle.dump(obj, file)
		file.close()
		return True

	def load_obj (self, file_name):
		file = open(file_name)	
		new_obj = pickle.load(file, "r")
		file.close()
		return new_obj
	
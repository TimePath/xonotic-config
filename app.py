#!/usr/bin/env python2

from flask import Flask
from flask import request

app = Flask(__name__)

def identity(args): return args



import colorsys

def rainbow(args):
	def nearest(x, base=16):
	    return int(base * round(float(x)/base))
	ret = ''
	idx = 0.0
	for c in args:
		h = 0.25 + idx * 0.015
		color = [int(255 * x) for x in colorsys.hsv_to_rgb(h, 1, 1)]
		print(color)
		hex = ['{:x}'.format(min(nearest(x), 255))[0] for x in color]
		print(hex)
		color = ''.join(hex)
		ret += '^x' + color + c
		idx += 1
	return ret;

@app.route('/xon', methods=['POST'])
def default():
	cmd = request.form['cmd']
	args = request.form['args']
	filter = request.form['filter']
	f = globals()[filter]
	args = f(args)
	return cmd + " " + args


if __name__ == '__main__':
	app.run()

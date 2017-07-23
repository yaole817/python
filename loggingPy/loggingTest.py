import logging
# set file format 
logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s %(name)-12s %(levelname)-8s :%(message)s', 
					datefmt='%m-%d %H:%M',
					filename = 'myapp.log',
					filemode = 'w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)


# set console format
formater = logging.Formatter("%(name)-12s: %(levelname)-8s :%(message)s")
console.setFormatter(formater)

logging.getLogger('').addHandler(console)
logging.info('jack love my big ')

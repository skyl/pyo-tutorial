print """

Welcome to the unofficial, off-broadway, homespun
interactive tutorial companion to the pyo documentation.
Follow along @ http://www.iact.umontreal.ca/pyo/manual/


To install, you must have the dependencies listed here:
http://code.google.com/p/pyo/wiki/Installation

In addition, you must have IPython.
Do one of the following:

easy_install readline ipython        # espec. right now on OSX
pip install ipython                  # preferably?

Homebrew is recommended for OSX.
You must have a *nix system, OSX or Linux, for instance.
"""

try:
	from IPython.Shell import IPShellEmbed
	ipython = IPShellEmbed(argv=('-noconfirm_exit',))
except:
	print """

	Could not import IPython

	"""
	import sys
	sys.exit()

print """
####################################
Press ctrl+d to begin.
####################################
"""


ipython()
code = """
from pyo import Server
s = Server().boot()
s.start()
"""
print """
We're are about to import everything from pyo and start a server, running::

%s
""" % code
exec(code)
print """
(You might see some warning messages)
Now you have "s" as a variable in your scope,
referencing a pyo Server object with rational defaults.  Play around.
(ctrl+d to continue)
"""


ipython()
code = """
from pyo import SquareTable, CosTable, Metro, TrigEnv, TrigXnoiseMidi, Osc
wav = SquareTable()
env = CosTable([(0,0), (100,1), (500,.3), (8191,0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48,84))
out = Osc(table=wav, freq=pit, mul=amp).out()
"""
print """
Let's start with an example that makes some noise.

%s""" % code
exec(code)
print """
wav, env, met, amp, pit and out are now in the namespace for investigation.
Some things that you can do with these objects:

You can see the documentation for the objects by entering "?" after the object,
for instance::

wav?
env?
met?
amp?
pit?
out?
s?

to stop and start the audible sound, run::

out.stop()
out.out()

To change the tempo of the Metro, for instance::

met.setTime(.5)
met.setTime(met.time/3)

Change the shape of the envelope::

env.replace([(0,0), (100,1), (500,.3), (1000,0)])
env.replace([(0,0), (100,1), (200,.3), (1000,0)])
env.replace([(0,0), (100,1), (200,.3), (600,0)])
env.replace([(0,0), (199,1), (200,.3), (210,0)])

Change the order of the SquareWave table (number of harmonics)::

wav.setOrder(1)
wav.setOrder(5)
wav.setOrder(30)

be careful with the wave size, it can get a little unruly::

wav.setSize(wav.size+1000)






To stop the sound, run ``out.stop()``.
wav, env, met, amp, pit and out are now in the namespace for investigation.
(ctrl+d to continue)
"""


ipython()




















ipython()
code = """
from pyo import Map
m = Map(20., 20000., 'log')
print "m.get(.5)=%s" % m.get(.5)
print "m.set(632.455532034)=%s" % m.set(632.455532034)
"""
print """
Now we're going to import Map, http://www.iact.umontreal.ca/pyo/manual/Map.html
The scales are "lin" for linear and "log" for logarithmic.

%s""" % code
exec(code)


ipython()






print "press ctrl+c to exit"





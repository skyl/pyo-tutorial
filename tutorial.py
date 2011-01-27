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
from pyo import *
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

``out`` -- Output
to stop and start the audible sound, run::

out.stop()
out.out()


``met`` -- Metronome
To change the tempo of the Metro, for instance::

met.setTime(.5)
met.setTime(met.time/3)


``env`` -- Envelope
Change the shape of the envelope::

env.replace([(0,0), (100,1), (500,.3), (1000,0)])
env.replace([(0,0), (100,1), (200,.3), (1000,0)])
env.replace([(0,0), (100,1), (200,.3), (600,0)])
env.replace([(0,0), (199,1), (200,.3), (210,0)])


``wav`` -- Wave
Change the order of the SquareWave table (number of harmonics)::

wav.setOrder(1)
wav.setOrder(5)
wav.setOrder(30)

be careful with the wave size, it can get a little unruly::

wav.setSize(wav.size+1000)


``amp`` -- Amplitude
Messing with the ``amp`` is messed up with ipython.
Don't use the help or tab completion.  Why?
You can change the duration of the amp.
Default is 1

amp.setDur(2)
amp.setDur(.1)

Change the amp multiplier::

amp.setMul(.5)
amp.setMul(.12)

Set the table on the amp:

amp.setTable(SquareTable())
amp.setTable(HarmTable())
amp.setTable(HarmTable([1,.5,.5,.01,.01,.01,.01,0,0,0,0,1]))
amp.setTable(env)


``pit`` -- Pitch
(Introspecting pit in ipython while the sound is playing seems to be a problem)
Change the random distribution of the TrigXnoiseMidi object::

pit.setDist('weibull')
pit.setDist('cauchy')
pit.setDist('poisson')

Set the range of the midi notes::

pit.setRange(46,84)
pit.setRange(24,43)


To stop the sound, run ``out.stop()``.
wav, env, met, amp, pit and out are now in the namespace for investigation.
(ctrl+d to continue)
"""
ipython()


out.stop()
code = """
sine = Sine(freq=[110,440], phase=0, mul=0.01, add=0).out()
"""
print """
Let's play with sine waves:
Following on at: http://code.google.com/p/pyo/wiki/Introduction

%s

Stop the sine with sine.stop().
Start it again with sine.out().
""" % code
exec(code)
ipython()


code = """
sine.freq = [110,111]
"""
print """
The freq argument is in [L, R].
Instead of sine.setFreq([110,111]) - style as above,
we can use setters to set the attrs of our objects::

%s

""" % code
exec(code)
ipython()


code = """
mod = Sine(freq=55/32., mul=.5)
sine.mul = mod
"""
print """
We can apply an lfo modulator to the freq and/or the mul of a soundwave.

%s

""" % code
exec(code)
ipython()


code = """
mod.freq = 55/16.
"""
print """
The we can change the attributes of the modulator::

%s

try::

mod.freq = 55/8.
mod.freq = 55/4.
mod.freq = 55/2.
...
and others, try changing the mul (careful, can get loud):

mod.mul = 2

""" % code
exec(code)
ipython()


code = """
modMulmod = Sine(55/16., mul=.5)
mod.mul = modMulmod
"""
print """
We can go on and put a modulator on the modulator::

%s

Then, we can alter the attrs of modMulmod.
try::

modMulmod.freq = 55/256. # etc


""" % code
exec(code)
ipython()
















code = """
from pyo import Map
map = Map(20., 20000., 'log')
print "map.get(.5)=%s" % map.get(.5)
print "map.set(632.455532034)=%s" % map.set(632.455532034)
"""
print """
Now we're going to import Map, http://www.iact.umontreal.ca/pyo/manual/Map.html
The scales are "lin" for linear and "log" for logarithmic.

%s""" % code
exec(code)


print """


press ctrl+d to exit"""
s.stop()
ipython()











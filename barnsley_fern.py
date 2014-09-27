import numpy as np, scipy, scipy.stats, random
 # http://connor-johnson.com/2014/03/18/fractal-interpolation/
N = 200
P = 5
for i in range( 1,N ):
    u = scipy.stats.uniform().rvs()
    # there is an 85% chance of using this transformation
    if u < 0.85:
        R = np.matrix([[0.85,0.04],[-0.04,0.85]])
        T = np.matrix([[0.0],[1.6]])
        p = R * np.matrix(P[i-1]).T + T
        P[i] = np.array(p.T)[0]
    # there is a 7% chance of using this one
    if( u >= 0.85 )and( u < 0.92 ):
        R = np.matrix([[0.20,-0.26],[0.23,0.22]])
        T = np.matrix([[0.0],[1.6]])
        p = R * np.matrix(P[i-1]).T + T
        P[i] = np.array(p.T)[0]
    # a 7% chance of using this one
    if( u >= 0.92 )and( u < 0.99 ):
        R = np.matrix([[-0.15,0.28],[0.26,0.24]])
        T = np.matrix([[0.0],[0.44]])
        p = R * np.matrix(P[i-1]).T + T
        P[i] = np.array(p.T)[0]
    # and finally, a 1% chance of using this transformation
    if u >= 0.99:
        R = np.matrix([[0.0,0.0],[0.0,0.16]])
        T = np.matrix([[0.0],[0.0]])
        p = R * np.matrix(P[i-1]).T + T
        P[i] = np.array(p.T)[0]
 
fig, ax = subplots( figsize=(5,8))
ax.scatter( P[:,0], P[:,1], color='k', marker='.', s=10, alpha=0.5 )
ax.set_aspect(1.)
savefig( 'barnsleyfern.png', fmt='png', dpi=100 )
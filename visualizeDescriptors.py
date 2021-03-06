import soundAnalysis as SA
import numpy as np


''''
# Mapping of descriptors
descriptorMapping = { 0: 'lowlevel.spectral_centroid.mean',
                      1: 'lowlevel.dissonance.mean',
                      2: 'lowlevel.hfc.mean',
                      3: 'sfx.logattacktime.mean',
                      4: 'sfx.inharmonicity.mean',
                      5: 'lowlevel.spectral_contrast.mean.0',
                      6: 'lowlevel.spectral_contrast.mean.1',
                      7: 'lowlevel.spectral_contrast.mean.2',
                      8: 'lowlevel.spectral_contrast.mean.3',
                      9: 'lowlevel.spectral_contrast.mean.4',
                      10: 'lowlevel.spectral_contrast.mean.5',
                      11: 'lowlevel.mfcc.mean.0',
                      12: 'lowlevel.mfcc.mean.1',
                      13: 'lowlevel.mfcc.mean.2',
                      14: 'lowlevel.mfcc.mean.3',
                      15: 'lowlevel.mfcc.mean.4',
                      16: 'lowlevel.mfcc.mean.5'
                    }


'''

N = 17 # number of descriptors

# Iterate through all the possible pairs for descriptors and see if they cluster the sounds good or they don't

for i in range(N):
    for j in range(N):
        SA.descriptorPairScatterPlot('downloaded/', descInput=(i,j), anotOn=0)

# Cluster sounds using k-means algorithm
SA.clusterSounds('downloaded/', nCluster=10, descInput=[4,8,9,10,11,12,13,14,15])

# Final choice of descriptors: 4,8,9,10,11,12,13,14,15
# Mean accuracy of 68.65% using k-means algorithm with 10 clusters


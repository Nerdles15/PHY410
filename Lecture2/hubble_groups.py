import math
# If installed, use matplotlib!
#import matplotlib.pyplot as plt

# distances in Mpc
# velocities in km/s

#group 1
r1 = [ 0.032, 0.034 ]
v1 = [ +170, +290 ]

#group 2
r2 = [ 0.214 ]
v2 = [ -130 ]

#group 3
r3 = [ 0.263, 0.275, 0.275 ]
v3 = [ -70, -185, -220 ]

#group 4
r4 = [ 0.45, 0.5, 1.4, 1.1, 0.63, 0.5, 1.7, 0.8, ]
v4 = [ +200, +270, +500, +450, +200, +290, +960, +300]

#group 5
r5 = [ 0.9 ]
v5 = [ +500 ]

#group 6
r6 = [ 1.0 ]
v6 = [ +920 ]

#group 7
r7 = [ 1.1 ]
v7 = [ +500 ]

#group 8
r8 = [ 2.0, 2.0, 0.9, 2.0, 2.0, 0.9 ]
v8 = [ +800, +1090, +150, +500, +850, +650 ]

#group 9
r9= [ 0.9 ]
v9 = [ -30 ]

# For each, plot v versus r
#plt.scatter(r,v)

# For checking n < 2 condition:
#r = [0.0, 1.0]
#v = [0.0, 1.0]

# For checking denom > 0.000001 condition :
#r = [0.0, 0.0, 0.0]
#v = [0.0, 0.0, 0.0]

# number of galaxies for each group
n1 = len(r1)
n2 = len(r2)
n3 = len(r3)
n4 = len(r4)
n5 = len(r5)
n6 = len(r6)
n7 = len(r7)
n8 = len(r8)
n9 = len(r9)

if n1 < 2 :
      print 'Error! Group 1 needs at least two data points!'
      #exit()

if n2 <= 2 :
      print 'Error! Group 2 needs at least two data points!'
      #exit()

if n3 <= 2 :
      print 'Error! Group 3 needs at least two data points!'
      #exit()

if n4 <= 2 :
      print 'Error! Group 4 needs at least two data points!'
      #exit()

if n5 <= 2 :
      print 'Error! Group 5 needs at least two data points!'
      #exit()

if n6 <= 2 :
      print 'Error! Group 6 needs at least two data points!'
      #exit()

if n7 <= 2 :
      print 'Error! Group 7 needs at least two data points!'
      #exit()

if n8 <= 2 :
      print 'Error! Group 8 needs at least two data points!'
      #exit()

if n9 <= 2 :
      print 'Error! Group 9 needs at least two data points!'
      #exit()

# Compute all of the stat. variables we need

#group 1
s_x_1 = 0
s_y_1 = 0
s_xx_1 = 0
s_xy_1 = 0
sigma2_1 = 0
for i in range (0, n1 ): 
   s_x_1 += r1[i]
   s_y_1 += v1[i]
   s_xx_1 += r1[i]**2
   s_xy_1 += r1[i]*v1[i]
denom1 = n1 * s_xx_1 - s_x_1**2
if abs( denom1 ) < 0.000001 : 
      print 'Error! Denomominator for group 1 is zero!'
      #exit()

# Compute y-intercept and slope 
a1 = (s_xx_1 * s_y_1 - s_x_1 * s_xy_1) / denom1
b1 = (n1*s_xy_1 - s_x_1 * s_y_1) / denom1   

# Compute uncertainties
if n1 > 2 : 
      sigma1 = math.sqrt(sum((v1[i] - (a1+b1*r1[i]))**2 for i in range(n1)) / (n1-2))
      sigma_a1 = math.sqrt(sigma1**2 * s_xx_1 / denom1)
      sigma_b1 = math.sqrt(sigma1**2 * n1 / denom1)
else :
      sigma1 = 0.
      sigma_a1 = 0.
      sigma_b1 = 0.

#group 2, only one data point so excluded
"""s_x_2 = 0
s_y_2 = 0
s_xx_2 = 0
s_xy_2 = 0
sigma2_2 = 0
for i in range (0, n2 ): 
   s_x_2 += r2[i]
   s_y_2 += v2[i]
   s_xx_2 += r2[i]**2
   s_xy_2 += r2[i]*v2[i]
denom2 = n2 * s_xx_2 - s_x_2**2
if abs( denom2 ) < 0.000001 : 
      print 'Error! Denomominator for group 2 is zero!'
      #exit()

# Compute y-intercept and slope 
a2 = (s_xx_2 * s_y_2 - s_x_2 * s_xy_2) / denom2
b2 = (n2*s_xy_2 - s_x_2 * s_y_2) / denom2

# Compute uncertainties
if n2 > 2 : 
      sigma2 = math.sqrt(sum((v2[i] - (a2+b2*r2[i]))**2 for i in range(n2)) / (n2-2))
      sigma_a2 = math.sqrt(sigma2**2 * s_xx_2 / denom2)
      sigma_b2 = math.sqrt(sigma2**2 * n2 / denom2)
else :
      sigma2 = 0.
      sigma_a2 = 0.
      sigma_b2 = 0."""

#group 3
s_x_3 = 0
s_y_3 = 0
s_xx_3 = 0
s_xy_3 = 0
sigma2_3 = 0
for i in range (0, n3 ): 
   s_x_3 += r3[i]
   s_y_1 += v3[i]
   s_xx_3 += r3[i]**2
   s_xy_3 += r3[i]*v3[i]
denom3 = n3 * s_xx_3 - s_x_3**2
if abs( denom3 ) < 0.000001 : 
      print 'Error! Denomominator for group 3 is zero!'
      #exit()

# Compute y-intercept and slope 
a3 = (s_xx_3 * s_y_3 - s_x_3 * s_xy_3) / denom3
b3 = (n3*s_xy_3 - s_x_3 * s_y_3) / denom3   

# Compute uncertainties
if n3 > 2 : 
      sigma3 = math.sqrt(sum((v3[i] - (a3+b3*r3[i]))**2 for i in range(n3)) / (n3-2))
      sigma_a3 = math.sqrt(sigma3**2 * s_xx_3 / denom3)
      sigma_b3 = math.sqrt(sigma3**2 * n3 / denom3)
else :
      sigma3 = 0.
      sigma_a3 = 0.
      sigma_b3 = 0.

#group 4
s_x_4 = 0
s_y_4 = 0
s_xx_4 = 0
s_xy_4 = 0
sigma2_4 = 0
for i in range (0, n4 ): 
   s_x_4 += r4[i]
   s_y_4 += v4[i]
   s_xx_4 += r4[i]**2
   s_xy_4 += r4[i]*v4[i]
denom4 = n4 * s_xx_4 - s_x_4**2
if abs( denom4 ) < 0.000001 : 
      print 'Error! Denomominator for group 4 is zero!'
      #exit()

# Compute y-intercept and slope 
a4 = (s_xx_4 * s_y_4 - s_x_4 * s_xy_4) / denom4
b4 = (n4*s_xy_4 - s_x_4 * s_y_4) / denom4 

# Compute uncertainties
if n4 > 2 : 
      sigma4 = math.sqrt(sum((v4[i] - (a4+b4*r4[i]))**2 for i in range(n4)) / (n4-2))
      sigma_a4 = math.sqrt(sigma4**2 * s_xx_4 / denom4)
      sigma_b4 = math.sqrt(sigma4**2 * n4 / denom4)
else :
      sigma4 = 0.
      sigma_a4 = 0.
      sigma_b4 = 0.

#group 5, only one data point so excluded
"""s_x_5 = 0
s_y_5 = 0
s_xx_5 = 0
s_xy_5 = 0
sigma2_5 = 0
for i in range (0, n5 ): 
   s_x_5 += r5[i]
   s_y_5 += v5[i]
   s_xx_5 += r5[i]**2
   s_xy_5 += r5[i]*v5[i]
denom5 = n5 * s_xx_5 - s_x_5**2
if abs( denom5 ) < 0.000001 : 
      print 'Error! Denomominator in group 5 is zero!'
      #exit()

# Compute y-intercept and slope 
a5 = (s_xx_5 * s_y_5 - s_x_5 * s_xy_5) / denom5
b5 = (n5*s_xy_5 - s_x_5 * s_y_5) / denom5   

# Compute uncertainties
if n5 > 2 : 
      sigma5 = math.sqrt(sum((v5[i] - (a5+b5*r5[i]))**2 for i in range(n5)) / (n5-2))
      sigma_a5 = math.sqrt(sigma5**2 * s_xx_5 / denom5)
      sigma_b5 = math.sqrt(sigma5**2 * n5 / denom5)
else :
      sigma5 = 0.
      sigma_a5 = 0.
      sigma_b5 = 0."""

#group 6, only one data point so excluded
"""s_x_6 = 0
s_y_6 = 0
s_xx_6 = 0
s_xy_6 = 0
sigma2_6 = 0
for i in range (0, n6 ): 
   s_x_6 += r6[i]
   s_y_6 += v6[i]
   s_xx_6 += r6[i]**2
   s_xy_6 += r6[i]*v6[i]
denom6 = n6 * s_xx_6 - s_x_6**2
if abs( denom6 ) < 0.000001 : 
      print 'Error! Denomominator in group 6 is zero!'
      #exit()

# Compute y-intercept and slope 
a6 = (s_xx_6 * s_y_6 - s_x_6 * s_xy_6) / denom6
b6 = (n6*s_xy_6 - s_x_6 * s_y_6) / denom6   

# Compute uncertainties
if n6 > 2 : 
      sigma6 = math.sqrt(sum((v6[i] - (a6+b6*r6[i]))**2 for i in range(n6)) / (n6-2))
      sigma_a6 = math.sqrt(sigma6**2 * s_xx_6 / denom6)
      sigma_b6= math.sqrt(sigma6**2 * n6 / denom6)
else :
      sigma6 = 0.
      sigma_a6 = 0.
      sigma_b6 = 0."""

#group 7, only one data point so exluded
"""s_x_7 = 0
s_y_7 = 0
s_xx_7 = 0
s_xy_7 = 0
sigma2_7 = 0
for i in range (0, n7 ): 
   s_x_7 += r7[i]
   s_y_7 += v1[i]
   s_xx_7 += r7[i]**2
   s_xy_7 += r7[i]*v7[i]
denom7 = n7 * s_xx_7 - s_x_7**2
if abs( denom7 ) < 0.000001 : 
      print 'Error! Denomominator in group 7 is zero!'
      #exit()

# Compute y-intercept and slope 
a7 = (s_xx_7 * s_y_7 - s_x_7 * s_xy_7) / denom7
b7 = (n7*s_xy_7 - s_x_7 * s_y_7) / denom7   

# Compute uncertainties
if n7 > 2 : 
      sigma7 = math.sqrt(sum((v7[i] - (a7+b7*r7[i]))**2 for i in range(n7)) / (n7-2))
      sigma_a7 = math.sqrt(sigma7**2 * s_xx_7 / denom7)
      sigma_b7 = math.sqrt(sigma7**2 * n7 / denom7)
else :
      sigma7 = 0.
      sigma_a7 = 0.
      sigma_b7 = 0."""

#group 8
s_x_8 = 0
s_y_8 = 0
s_xx_8 = 0
s_xy_8 = 0
sigma2_8 = 0
for i in range (0, n8 ): 
   s_x_8 += r8[i]
   s_y_8 += v8[i]
   s_xx_8 += r8[i]**2
   s_xy_8 += r8[i]*v8[i]
denom8 = n8 * s_xx_8 - s_x_8**2
if abs( denom8 ) < 0.000001 : 
      print 'Error! Denomominator in group 8 is zero!'
      #exit()

# Compute y-intercept and slope 
a8 = (s_xx_8 * s_y_8 - s_x_8 * s_xy_8) / denom8
b8 = (n8*s_xy_8 - s_x_8 * s_y_8) / denom8   

# Compute uncertainties
if n8 > 2 : 
      sigma8 = math.sqrt(sum((v8[i] - (a8+b8*r8[i]))**2 for i in range(n8)) / (n8-2))
      sigma_a8 = math.sqrt(sigma8**2 * s_xx_8 / denom8)
      sigma_b8 = math.sqrt(sigma8**2 * n8 / denom8)
else :
      sigma8 = 0.
      sigma_a8 = 0.
      sigma_b8 = 0.

#group 9, only one data point so exluded
"""s_x_9 = 0
s_y_9 = 0
s_xx_9 = 0
s_xy_9 = 0
sigma2_9 = 0
for i in range (0, n9 ): 
   s_x_9 += r9[i]
   s_y_9 += v9[i]
   s_xx_9 += r9[i]**2
   s_xy_9 += r9[i]*v9[i]
denom9 = n9 * s_xx_9 - s_x_9**2
if abs( denom9 ) < 0.000001 : 
      print 'Error! Denomominator in group 9 is zero!'
      #exit()

# Compute y-intercept and slope 
a9 = (s_xx_9 * s_y_9 - s_x_9 * s_xy_9) / denom9
b9 = (n9*s_xy_9 - s_x_9 * s_y_9) / denom9   

# Compute uncertainties
if n9 > 2 : 
      sigma9 = math.sqrt(sum((v9[i] - (a9+b9*r9[i]))**2 for i in range(n9)) / (n9-2))
      sigma_a9 = math.sqrt(sigma9**2 * s_xx_9 / denom9)
      sigma_b9 = math.sqrt(sigma9**2 * n9 / denom9)
else :
      sigma9 = 0.
      sigma_a9 = 0.
      sigma_b9 = 0."""


# Print out results, Group 1:
print ' \nLeast squares fit of', n1, 'data points: Group 1'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b1, sigma_b1)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a1, sigma_a1)
print ' Estimated v error bar sigma =', round(sigma1, 1), 'km/s'

#plt.show()

# Print out results, Group 3:
print ' \nLeast squares fit of', n3, 'data points: Group 3'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b3, sigma_b3)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a3, sigma_a3)
print ' Estimated v error bar sigma =', round(sigma3, 1), 'km/s'

#plt.show()

# Print out results, Group 4:
print ' \nLeast squares fit of', n4, 'data points: Group 4'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b4, sigma_b4)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a4, sigma_a4)
print ' Estimated v error bar sigma =', round(sigma4, 1), 'km/s'

#plt.show()

# Print out results, Group 8:
print ' \nLeast squares fit of', n8, 'data points: Group 8'
print ' -----------------------------------'
print " Hubble's constant slope   b = {0:6.2f} +- {1:6.2f}  km/s/Mpc".format( b8, sigma_b8)
print " Intercept with r axis     a = {0:6.2f} +- {1:6.2f}  km/s".format( a8, sigma_a8)
print ' Estimated v error bar sigma =', round(sigma8, 1), 'km/s'

#plt.show()

print '\nGroups 2, 5, 6, 7, and 9 have been omitted since they only contain one data point each.'

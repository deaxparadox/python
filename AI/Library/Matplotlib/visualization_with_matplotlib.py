# In[]:
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# %%

# %%
"""the plt.style directive to choose appropriate aesthetic
styles for our figures."""
plt.style.use("classic")
# %%
x = np.linspace(0,10,100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
# plt.show()
# %%
"""Saving Figures to File
"""

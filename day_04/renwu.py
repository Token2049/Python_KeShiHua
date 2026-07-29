import matplotlib.pyplot as plt
fig = plt.figure(constrained_layout=True)
gs = fig.add_gridspec(3, 4)
fig.add_subplot(gs[0, :])
fig.add_subplot(gs[1, :-2])
fig.add_subplot(gs[1, -2:])
fig.add_subplot(gs[2, 0])
fig.add_subplot(gs[2, 1:])
plt.show()
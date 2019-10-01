import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.style.use('dark_background')


# Plotted bob circle radius
r = 0.04
# Plot a trail of the m2 bob's position for the last trail_secs seconds.
trail_secs = 1

fig = plt.figure(figsize=(7, 7), dpi=102.867)
ax = fig.add_subplot(111)
ax.set_aspect('equal')


def plot_frame(pendulums, i, dt, di):
    t = i * dt

    # Plot and save an image of the double pendulum configuration for time
    # point i.
    # The pendulum rods.
    for p_i, p in enumerate(pendulums):
        # The colour of the pendulum
        c = f'C{p_i % 10}'
        ax.plot([0, p.x1[i], p.x2[i]], [0, p.y1[i], p.y2[i]], lw=1.2, c='white')
        # Circles representing the anchor point of rod 1, and bobs 1 and 2.
        c0 = Circle((0, 0), 0.5 * r, fc='white', zorder=10)
        c1 = Circle((p.x1[i], p.y1[i]), 0.5 * r, fc='white', zorder=10)
        c2 = Circle((p.x2[i], p.y2[i]), r, fc=c, ec=c, zorder=10)
        ax.add_patch(c0)
        ax.add_patch(c1)
        ax.add_patch(c2)

    # The trail will be divided into ns segments and plotted as a fading line.
    max_trail = int(trail_secs / dt)
    ns = 20
    s = max_trail // ns

    for j in range(ns):
        imin = i - (ns - j)*s
        if imin < 0:
            continue
        imax = imin + s + 1
        # The fading looks better if we square the fractional length along the
        # trail.
        alpha = (j / ns)**2
        for p_i, p in enumerate(pendulums):
            # The colour of the pendulum
            c = f'C{p_i % 10}'
            ax.plot(p.x2[imin:imax], p.y2[imin:imax], c=c, solid_capstyle='butt',
                    lw=2, alpha=alpha)

    plt.text(-0.1, 2, f't = {t:.01f}', fontdict={'size': 20})

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    p = pendulums[0]
    ax.set_xlim(-p.L1 - p.L2 - r, p.L1 + p.L2 + r)
    ax.set_ylim(-p.L1 - p.L2 - r, p.L1 + p.L2 + r)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig('frames/{:04d}.png'.format(i//di), dpi=102.867)
    plt.cla()
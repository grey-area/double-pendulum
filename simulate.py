import os
import argument_parser
import pendulum
import plotting
from tqdm import tqdm


if __name__ == '__main__':
    # Parse command-line arguments
    args = argument_parser.parse_args()

    # Create directory for frames
    os.makedirs('frames', exist_ok=True)

    # Create the pendulums
    pendulums = [pendulum.Pendulum(noise_scale=args.noise_scale) for i in range(args.num_pendulums)]

    dt = 0.01
    # Simulate their motion
    for p in pendulums:
        p.simulate(args.simulation_time, dt)

    # Make an image every di time points, corresponding to a frame rate of fps
    # frames per second.
    # Frame rate, s-1
    di = int(1 / args.fps / dt)
    for i in tqdm(range(0, int(args.simulation_time / dt), di)):
        plotting.plot_frame(pendulums, i, dt, di)
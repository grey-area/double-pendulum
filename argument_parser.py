import argparse


def validate_args(args):
    if args.num_pendulums < 1 or args.num_pendulums > 200:
        raise ValueError('Number of pendulums must be between 1 and 200')
    if args.simulation_time < 0.1 or args.simulation_time > 1000:
        raise ValueError('Simulation time must be between 0.1 and 1000 seconds')
    if args.fps < 5 or args.fps > 60:
        raise ValueError('Frames per second must be between 5 and 60')
    if args.noise_scale < 0 or args.noise_scale > 1:
        raise ValueError('Noise scale must be between 0 and 1')


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--num-pendulums', type=int,
        default=1,
        help='Number of pendulums, between 1 and 200'
    )

    parser.add_argument(
        '--simulation-time', type=float,
        default=10,
        help='Simulation time in seconds, between 0.1 and 1000'
    )

    parser.add_argument(
        '--fps', type=int,
        default=20,
        help='Frames per second, between 5 and 60'
    )

    parser.add_argument(
        '--noise-scale', type=float,
        default=1e-3,
        help='Pendulum angles differ via Gaussian noise with this standard deviation'
    )

    args = parser.parse_args()
    validate_args(args)

    return args

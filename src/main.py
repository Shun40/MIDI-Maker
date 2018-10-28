import sys, os, argparse
import Maker

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-if', '--input_file', help = 'Input text file path (*.txt)', type = str)
    parser.add_argument('-of', '--output_file', help = 'Output MIDI file path (*.mid)', type = str)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    input_path = args.input_file
    output_path = args.output_file

    if not os.path.exists(input_path):
        print('{} does not exist.'.format(input_path))
        sys.exit(1)

    sequence = Maker.make_sequence(input_path)
    sequence.show()
    sequence.write_to_file(output_path)

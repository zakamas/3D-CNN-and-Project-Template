
from datetime import datetime
import os
import argparse
import numpy as np





if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument('--train', dest='train', required=True, help='(REQUIRED) location of the train directory')
    parser.add_argument('--test', dest='test', required=True, help='(REQUIRED) location of the test directory')
    parser.add_argument('--cats', '-c', dest='categories', type=int, required=True, help='(REQUIRED) number of categories for the model to learn')
    parser.add_argument('--model', '-m', dest='model', required=True, help='(REQUIRED) location of the model and checkpoints')
    parser.add_argument('--experiment', dest='experiment', required=True, help='(REQUIRED) the name of the experiment')
    # Optional
    parser.add_argument('--output', '-o', dest='output', default='./output/', required=False, help='location of the output directory (default:./)')
    parser.add_argument('--batch', '-b', dest='batch', default=32, type=int, required=False, help='batch size (default:32)')
    parser.add_argument('--epochs', '-e', dest='epochs', default=30, type=int, required=False, help='number of epochs to run (default:30)')
    parser.add_argument('--shape','-s', dest='shape', default=128, type=int, required=False, help='The shape of the image, single dimension will be applied to height and width (default:128)')

    args = parser.parse_args()

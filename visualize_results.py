# visualize_results.py
# Dan Popp
# 12/07/21
#
# This file will be used to generate loss plots or whatever
import os

import numpy as np
from matplotlib import pyplot as plt

OUTPUT_DIR = './Metrics/'
TRAINING_FILE = 'CAP_Xception(Training).csv'
VALIDATION_FILE = 'CAP_Xception(Validation).csv'


def main():
    # Load validation data
    valid_file_path = os.path.join(OUTPUT_DIR, VALIDATION_FILE)
    with open(valid_file_path, 'r') as file:
        lines = file.readlines()
        acc = []
        epochs = []
        losses = []
        for line in lines:
            line = line.strip()
            tokens = line.split(',')
            epoch = int(tokens[0])
            accuracy = float(tokens[2])
            loss = float(tokens[1])

            acc.append(accuracy)
            epochs.append(epoch)
            losses.append(loss)

    valid_acc = np.zeros((len(epochs), 2))
    valid_loss = np.zeros((len(epochs), 2))
    for i in range(len(epochs)):
        valid_acc[i, :] = [epochs[i], acc[i]]
        valid_loss[i, :] = [epochs[i], losses[i]]

    plt.clf()
    plt.plot(valid_acc[:, 0], valid_acc[:, 1])
    plt.savefig(os.path.join(OUTPUT_DIR, 'valid_acc.png'))
    plt.clf()

    plt.clf()
    plt.plot(valid_loss[:, 0], valid_loss[:, 1])
    plt.savefig(os.path.join(OUTPUT_DIR, 'valid_loss.png'))
    plt.clf()

    # Load validation data
    valid_file_path = os.path.join(OUTPUT_DIR, TRAINING_FILE)
    with open(valid_file_path, 'r') as file:
        lines = file.readlines()
        acc = []
        epochs = []
        losses = []
        for line in lines:
            line = line.strip()
            tokens = line.split(',')
            if tokens[0] == 'epoch':
                continue
            epoch = int(tokens[0])
            accuracy = float(tokens[1])
            loss = float(tokens[2])

            acc.append(accuracy)
            epochs.append(epoch)
            losses.append(loss)

    valid_acc = np.zeros((len(epochs), 2))
    valid_loss = np.zeros((len(epochs), 2))
    for i in range(len(epochs)):
        valid_acc[i, :] = [epochs[i], acc[i]]
        valid_loss[i, :] = [epochs[i], losses[i]]

    plt.clf()
    plt.plot(valid_acc[:, 0], valid_acc[:, 1])
    plt.savefig(os.path.join(OUTPUT_DIR, 'train_acc.png'))
    plt.clf()

    plt.clf()
    plt.plot(valid_loss[:, 0], valid_loss[:, 1])
    plt.savefig(os.path.join(OUTPUT_DIR, 'train_loss.png'))
    plt.clf()


if __name__ == '__main__':
    main()

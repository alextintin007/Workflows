import awkward as ak
from coffea.nanoevents import NanoEventsFactory, PFNanoAODSchema
import matplotlib.pyplot as plt
import os
import sys


def save_plot(output_file_path1, output_file_path2):
    fname = "doubleeg_nanoaod_eg.root"
    events = NanoEventsFactory.from_root(
        fname,
        schemaclass=PFNanoAODSchema.v6,
        metadata={"dataset": "DoubleEg"},
    ).events()

    # Number of PF candidates, print and save to a text file
    n_pfcands = ak.num(events.PFCands, axis=1)
    print(n_pfcands)
    print(events.PFCands.fields)

    # Plot PF candidate pt and their number and save the images
    fig, ax = plt.subplots()
    ax.set_yscale('log')
    ax.hist(ak.flatten(events.PFCands.pt), bins=200)
    ax.set_title('PF candidate p_t')
    output_directory = os.path.dirname(output_file_path1)
    png_filename = os.path.join(output_directory, "PF_pt.png")
    fig.savefig(png_filename)

    fig, ax = plt.subplots()
    ax.hist(ak.num(events.PFCands, axis=1), bins=50)
    ax.set_title('n PF candidates')
    output_directory = os.path.dirname(output_file_path2)
    png_filename = os.path.join(output_directory, "PF_n.png")
    fig.savefig(png_filename)

if __name__ == "__main__":
    output_file1 = sys.argv[1]
    output_file2 = sys.argv[2]
    save_plot(output_file1, output_file2)
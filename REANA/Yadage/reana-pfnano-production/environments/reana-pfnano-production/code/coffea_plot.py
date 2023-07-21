import awkward as ak
from coffea.nanoevents import NanoEventsFactory, PFNanoAODSchema
import matplotlib.pyplot as plt
import json
import os
import sys


def save_plot(output_file_path):
    #fname = "https://raw.githubusercontent.com/cms-dpoa/cat-hackathon/main/data/doubleeg_nanoaod_eg.root"
    fname = "doubleeg_nanoaod_eg.root"
    events = NanoEventsFactory.from_root(
        fname,
        schemaclass=PFNanoAODSchema.v6,
        metadata={"dataset": "DoubleEg"},
    ).events()

    # PF candidate collection for jets
    # print(events.Jet.nConstituents)

    # Number of PF candidates, print and save to a text file
    n_pfcands = ak.num(events.PFCands, axis=1)

    print(n_pfcands)
    print(events.PFCands.fields)

    output_dir = "output_directory"  # Replace with the desired directory path for output files

    # Save the number of PF candidates to a text file
    # with open(os.path.join(output_dir, 'PF_n.txt'), 'w') as filehandle:
    #     json.dump(n_pfcands.tolist(), filehandle)

    # Plot PF candidate pt and their number and save the images
    fig, ax = plt.subplots()
    ax.set_yscale('log')
    ax.hist(ak.flatten(events.PFCands.pt), bins=200)
    # ax.set_title('PF candidate p_t')

    # fig.savefig(os.path.join(output_dir, "PF_pt.png"))

    fig, ax = plt.subplots()
    ax.hist(ak.num(events.PFCands, axis=1), bins=50)
    ax.set_title('n PF candidates')

    output_directory = os.path.dirname(output_file_path)
    png_filename = os.path.join(output_directory, "PF_n.png")
    fig.savefig(png_filename)

if __name__ == "__main__":
    output_file = sys.argv[1]
    save_plot(output_file)
    print("Done!")
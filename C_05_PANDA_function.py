import pandas
from tabulate import tabulate


def panda_frame_maker(dictionary):
    # Pandas Data frame
    frame = pandas.DataFrame(dictionary)

    # Add total amount needed for all batches.
    frame['Batch Amount'] = frame['Amount'] * frame['batch count']

    frame_string = tabulate(frame, headers="keys", tablefmt="psql")

    return frame_string






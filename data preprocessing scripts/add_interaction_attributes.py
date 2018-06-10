import filter_round
import pandas as pd


def add_interaction_attributes(inFile):
    # get list of positions and zscore attributes
    csv_input = pd.read_csv(inFile)
    positions = set(csv_input.Pos)
    zscore_attributes = [attribute for attribute in csv_input.head() if "zscore" in attribute]

    # make interaction attributes
    interaction_attributes = [pos + "_" + attr for pos in positions for attr in zscore_attributes]
    position_attributes = {pos: [attr for attr in interaction_attributes if attr[:len(pos) + 1] == pos + "_"] for pos in positions}

    # add interaction attribute columns to csv, initialized to "?"
    for attr in interaction_attributes:
        csv_input[attr] = "?"

    # fill in relevant zscores to corresponding position interaction attributes
    for index, player in csv_input.iterrows():
        pos = player["Pos"]
        pos_attributes = position_attributes[pos]
        for attr in pos_attributes:
            #player[attr] = player[attr[len(pos) + 1:]]
            zscore = player[attr[len(pos) + 1:]]
            csv_input.at[index, attr] = zscore

    # delete original zscore attributes and raw combine statistics
    prefix_length = len("zscore_")
    for attr in zscore_attributes:
        csv_input.drop(attr, 1, inplace=True)
        csv_input.drop(attr[prefix_length:], 1, inplace=True)

    # delete "College Stats" column
    csv_input.drop("College", 1, inplace=True)

    # output csv
    csv_input.to_csv('./normalized combine data (with z-scores & interaction attributes)/combined_stats_binary_with_interaction_attributes.csv', sep=",", encoding="utf-8", index=False)


def main():
    # make data binary
    filter_round.drafted_or_not("./normalized combine data (with z-scores & interaction attributes)/combined_stats.csv", "./normalized combine data (with z-scores & interaction attributes)/combined_stats_binary.csv")

    # add interaction attributes, remove pos and original zscore attributes
    add_interaction_attributes("./normalized combine data (with z-scores & interaction attributes)/combined_stats_binary.csv")


if __name__ == '__main__':
    main()

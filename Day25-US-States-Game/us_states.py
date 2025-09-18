import pandas
CSV_PATH = "50_states.csv"
class States:
    def __init__(self):
        self.data = pandas.read_csv(CSV_PATH)

    def existing_state(self, state):
        if self.data[self.data["state"] == state].empty:
            return False
        else:
           return True

    def get_coordinates(self, state):
        if self.data[self.data["state"] == state].empty:
            return False
        else:
            row = self.data[self.data["state"] == state]
            x = row["x"]
            y = row["y"]
            index_row = (x.iloc[0],y.iloc[0])
            return index_row

    def get_all_states(self):
        number_of_states = self.data["state"].to_list()
        return number_of_states

    def remaining_states(self, list_state):
        self.data = pandas.DataFrame(list_state)
        self.data.to_csv("Remaining_states.csv")
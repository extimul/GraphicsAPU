import matplotlib.pyplot as plt

from helpers.strings import COLORS


class APUGraphic:
    def __init__(self, time_line):
        self.time_line = time_line
        plt.style.use('seaborn-bright')
        # plt.tight_layout()

    def create_graphic(self, graphic_name, args):
        fig, ax = plt.subplots(figsize=(10, 6))
        if len(args) == 4:
            ax.plot(self.time_line, args[0], color=COLORS[0], marker='*', label=args[2])
            ax.plot(self.time_line, args[1], color=COLORS[1], marker='o', label=args[3])
        else:
            ax.plot(self.time_line, args[0], color=COLORS[0], marker='*', label=args[3])
            ax.plot(self.time_line, args[1], color=COLORS[1], marker='o', label=args[4])
            ax.plot(self.time_line, args[2], color=COLORS[2], marker='|', label=args[5])
        ax.set_xlabel('Time')
        ax.set_ylabel('Data')
        ax.legend(loc='best')
        ax.tick_params(axis='x', which='minor', labelsize=3)
        plt.xticks(self.time_line, rotation=90)
        plt.show()
        fig.savefig(f'files/graphics/{graphic_name}.png', bbox_inches='tight')
        plt.close(fig)



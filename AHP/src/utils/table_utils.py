# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                table_utils
# FILE VERSION:             1.0
# DATE:                     05.04.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains set of static methods responsible for plotting output of AHP calculations
# in form of table
# ======================================================================================================================

import curses


class Table:

    def __init__(self, screen, start_row, start_column):
        self.start_row = start_row
        self.start_column = start_column
        self.screen = screen
        self.columns_names = []
        self.columns_values = []
        self.columns_borders = [0]
        self.columns_padding = 3

    def add_column(self, column_name, column_values, column_width):
        self.columns_names.append(column_name)
        self.columns_values.append(column_values)
        self.columns_borders.append(self.columns_borders[-1] + column_width)

    def draw_table(self):
        self.draw_header()

        for i in range(len(self.columns_values[0])):
            self.draw_raw(i)

    def draw_header(self):
        horizontal_border = ['-'] * (self.columns_borders[-1] + 1)
        for index in self.columns_borders:
            horizontal_border[index] = '+'
        horizontal_border = ''.join(horizontal_border)

        self.screen.addstr(self.start_row, self.start_column, horizontal_border)

        for val in self.columns_borders:
            self.screen.addstr(self.start_row + 1, self.start_column + val, "|")

        for index, val in enumerate(self.columns_names):
            self.screen.addstr(self.start_row + 1,
                               self.start_column + self.columns_padding + self.columns_borders[index],
                               val,
                               curses.A_BOLD)

        self.screen.addstr(self.start_row + 2, self.start_column, horizontal_border)

    def draw_raw(self, index):
        current_row_index = self.start_row + 3 + 2 * index

        horizontal_border = ['-'] * (self.columns_borders[-1] + 1)
        for border_index in self.columns_borders:
            horizontal_border[border_index] = '+'
        horizontal_border = ''.join(horizontal_border)

        self.screen.addstr(current_row_index + 1, self.start_column, horizontal_border)

        for val in self.columns_borders:
            self.screen.addstr(current_row_index, self.start_column + val, "|")

        for column_index, column_value in enumerate(self.columns_values):
            self.screen.addstr(current_row_index,
                               self.start_column + self.columns_borders[column_index] + self.columns_padding,
                               str(self.columns_values[column_index][index])[:8])

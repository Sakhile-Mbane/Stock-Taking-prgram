# Create a Shoe class, create a function (read_data()) that will
# implement a try-except block for reading the following information
# from the file:
# ● country,
# ● code,
# ● product,
# ● cost, and
# ● quantity.
# Create at least 5 shoe objects and store these in a list. Add
# functionality to search products in the objects list by code.
# Write code to determine the product with the lowest quantity, and
# restock it.
# Write code to determine the product with the highest quantity and
# mark it up as being for sale.
# You will have noticed that in the original data, there are only five
# columns. Write a function, value_per_item(), to calculate the value
# (or total worth) of each item entered. (Please keep the formula for
# value in mind; value = cost * quantity.) This function should then
# create a sixth column for each product, named value.

from tabulate import tabulate


class Shoe(object):

    @staticmethod
    def read_data():

        try:
            with open('inventory.txt', 'r+') as f:  # Open the inventory file

                shoe_object = {}
                quantity_dict = {}

                for lines in f:
                    newline = lines.strip('\n')  # Strip and new line on the file
                    split_line = newline.split(",")  # Split the newline using a ', '

                    # Make key be the code, and values the a list [country, code, product, cost, quantity]
                    shoe_object[split_line[1]] = [split_line[0], split_line[1], split_line[2], split_line[3],
                                                  split_line[4]]

                    # Make Key be product and values quantity
                    if split_line[4].isdigit():
                        quantity_dict[split_line[2]] = int(split_line[4])

                    else:
                        pass

                #  Request user to input code
                code = input('Enter the code to search: ')

                # Print the products for the searched code
                if code in shoe_object.keys():
                    print(f'The code results to the shoe with {shoe_object[code]}')

                # Write code to determine the product with the lowest quantity, and
                # restock it
                min_value = min(quantity_dict.values())
                print('The product which needs to be restocked is ' + str(
                    {key: value for key, value in quantity_dict.items() if value == min_value}))

                # Write code to determine the product with the highest quantity and
                # mark it up as being for sale.

                max_value = max(quantity_dict.values())
                print('The product with the highest quantity ' + str(
                    {key: value for key, value in quantity_dict.items() if value == max_value}))

        except AttributeError:
            print(f'The file is not available')

    @staticmethod
    def value_per_item():
        with open('inventory.txt', 'r+') as f1:  # Open the inventory file
            #
            new_data = {}
            # Skip the first line
            next(f1)
            for line in f1:
                newlines = line.strip('\n')  # Strip and new line on the file
                split_lines = newlines.split(",")  # Split the newline using a ', '

                # new data with new column named Value
                new_data[split_lines[1]] = [split_lines[0], split_lines[1], split_lines[2], split_lines[3],
                                            split_lines[4], int(split_lines[3]) * int(split_lines[4])]
        # Add the first row with the sixth column.
        # Add the first line, using update

        table_dict = {'Code': ['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Value']}
        table_dict.update(new_data)

        # Putting the values in a nested list
        data = []
        for i in table_dict:
            data.append(table_dict[i])

        print(tabulate(data))


class_object1 = Shoe().read_data()
class_object2 = Shoe().value_per_item()

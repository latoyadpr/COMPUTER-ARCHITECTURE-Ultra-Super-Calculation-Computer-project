#-------------------------------------------
# USCC Headquarter's Instruction Set Architecture
#  System Design:
#   - Four function calculator
#   - Can only operate on numbers stored in registers
#   - Processor receives binary data as 32-bit strings
#   - Returns results to the terminal
#   - Can operate on 10-bit numbers (0 thru 1023)
#   - Results can be negative (5 - 10 = -5)
#  Instruction format:
#   - 32 bit's in length
#   - Binary data will come to the CPU as a string
#   - Registers (32 total on CPU, 0-indexed)
#      - 0 thru 21:  Available for number storage
#        - 0: Constant 0
#      - 22 thru 31: Available for history storage
# +=======+=======+=======+=======+=======+=======+=======+=======+
# | 0: 0  | 1:    | 2:    | 3:    | 4:    | 5:    | 6:    | 7:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# | 8:    | 9:    |10:    |11:    |12:    |13:    |14:    |15:    |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |16:    |17:    |18:    |19:    |20:    |21:    |22: H0 |23: H1 |
# +-------+-------+-------+-------+-------+-------+-------+-------+
# |24: H2 |25: H3 |26: H4 |27: H5 |28: H6 |29: H7 |30: H8 |31: H9 |
# +=======+=======+=======+=======+=======+=======+=======+=======+
#   - Bits 0-5 are OPCODEs
#     - use variable 'opcode' in program
#   - Bits 6-10 & 11-15 are source register locations
#     - use variables 'source_one' and 'source_two' in program
#   - Bits 16-25 are reserved for adding a new value to the registers
#     - use variable 'store' in program
#   - Bits 26-31 are functions
#     - use variable 'function_code' in program
# +--------+----------+-------------------------------------+
# | OPCODE | FUNCTION | Definition                          |
# | 000000 |  100000  | Add two numbers from registers      |
# | 000000 |  100010  | Subtract two numbers from registers |
# | 000000 |  011000  | Multiply two numbers from registers |
# | 000000 |  011010  | Divide two numbers from registers   |
# | 000001 |  000000  | Store value to next register        |
# | 100001 |  000000  | Return previous calculation         |
# +--------+----------+-------------------------------------+

# Your code below here:
# USCC Headquarter's Instruction Set Architecture
# System Design:
# ...
# +--------+----------+-------------------------------------+

# Your code below here:
number_registers = [0] * 22
history_registers = [0] * 10

numbers_index = 1
history_index = 0
temp_history_index = 0

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

# Instantiate the UltraSuperCalculator class
your_calculator = UltraSuperCalculator("Your Name")


class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        pass

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

def load_value_from_register(self, register_address):
    index = int(register_address, 2)

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value
class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        pass

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0


class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        pass

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value

    def divide(self, address_num1, address_num2):
        pass

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value
    def divide(self, address_num1, address_num2):
        pass

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

    def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value

            def divide(self, address_num1, address_num2):
s_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print("Division by 0 error")

class UltraSuperCalculator:
    def __init__(self, name) -> None:
        self.name = name
        self.number_registers = [0] * 22
        self.history_registers = [0] * 10
        self.numbers_index = 1
        self.history_index = 0
        self.temp_history_index = 0
        self.user_display = ''
        self.update_display(f"Welcome to {self.name}'s Calculator!")

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)

    def store_value_to_register(self, value_to_store):
        if self.numbers_index > 21:
            self.numbers_index = 1
        self.number_registers[self.numbers_index] = int(value_to_store, 2)
        print(f"Value: {int(value_to_store, 2)} stored in Register: {self.numbers_index}.")
        self.numbers_index += 1

    def load_value_from_register(self, register_address):
        index = int(register_address, 2)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index > 9:
            self.history_index = 0
        self.history_registers[self.history_index] = bin(result_to_store)
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

        def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

        def subtract(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value

    def divide(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        if num2 != 0:
            calculated_value = int(num1 / num2)
        else:
            print("Division by 0 error") 
        
#Using the calculator
# Instantiate the UltraSuperCalculator class
your_calculator = UltraSuperCalculator("Latoya L Dupree")

# Store values in the number registers
your_calculator.binary_reader("00000100000000000000000101000000")  # Store 5
your_calculator.binary_reader("00000100000000000000001010000000")  # Store 10

# Perform operations on the stored values
your_calculator.binary_reader("00000000001000100000000000100000")  # Add 5 and 10
your_calculator.binary_reader("00000000001000100000000000100010")  # Subtract 10 from 5
your_calculator.binary_reader("00000000001000100000000000011000")  # Multiply 5 and 10
your_calculator.binary_reader("00000000001000100000000000011010")  # Divide 10 by 5

# Retrieve the last three calculations
your_calculator.binary_reader("10000100000000000000000000000000")
your_calculator.binary_reader("10000100000000000000000000000000")
your_calculator.binary_reader("10000100000000000000000000000000")



    


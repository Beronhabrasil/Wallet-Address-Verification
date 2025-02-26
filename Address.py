import easygui

class Address:
    def compare(self):
        while True:
            previous_address = easygui.enterbox("Enter the previous address: ", "Wallet Address Comparison")
            if previous_address is None:
                break

            new_address = easygui.enterbox("Enter the new address: ")
            if new_address is None:  # User clicked cancel
                break

            if previous_address == new_address:
                message = "Addresses are the same:\n{} and {}".format(previous_address, new_address)
            else:
                message = "Addresses are not the same:\n{} and {}".format(previous_address, new_address)

            easygui.msgbox(message, "Comparison Result")
            choice = easygui.ynbox("Do you want to compare another address?", "Continue?", ["Yes", "No"])
            if not choice:
                break

address = Address()
address.compare()

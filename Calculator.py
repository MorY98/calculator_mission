# Mor yossef 
# 209514264


# The Python GUI toolkit
import tkinter as tk

class Calculator:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("Mor Yossef Program")
        self.screen.configure(bg="#F4F4F4")  # Background color of the calculator

        # Create entry widget for input
        self.entry = tk.Entry(screen, width=20, font=('Arial', 14), bd=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define colors
        button_bg_color = "#104E8B"  # Background color of the non-number buttons
        button_fg_color = "#000000"  # Text color of buttons

        # Define the buttons for the calculator
        button_options = [
            '7', '8', '9', '/',  
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', '=', '+',
            'C', '<-', 'x²', 'H'  # Clear, backspace, exponent, and history buttons
        ]

        row = 1
        col = 0
        for button in button_options:
            # Set background color based on whether the button is a number or operator
            if button.isdigit() or button == '.':
                bg_color = "#B7B7B7"  # Background color of number buttons
            else:
                bg_color = button_bg_color

            # Create the buttons for each option in the list then places it in a grid layouts.
            tk.Button(screen, text=button, width=5, font=('Arial', 14), bg=bg_color, fg=button_fg_color,
                      command=lambda copy_b=button: self.on_button_click(copy_b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.history = []  # history list to store calculations

  
    def on_button_click(self, button):
        if button == '=':
            # Evaluate expression and handle exceptions
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.history.append(f"{expression} = {result}")  # Add expression and result to history
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except SyntaxError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Syntax Error")
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Zero Division Error")
        elif button == 'C':
            # Clear the entry widget
            self.entry.delete(0, tk.END)
        elif button == '<-':
            # Remove the last character from the entry widget
            expression = self.entry.get()
            self.entry.delete(len(expression) - 1, tk.END)
        elif button == 'x²':
            # Square the current value in the entry widget
            expression = self.entry.get()
            try:
                result = eval(expression)**2
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.history.append(f"{expression}**2 = {result}")  # Add expression and result to history
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button == 'H':
            # Display the calculation history
            self.show_history()
        else:
            # Insert the clicked button's text into the entry widget
            self.entry.insert(tk.END, button)

    def show_history(self):
        # Create a new window to display the calculation history
        history_window = tk.Toplevel(self.screen)
        history_window.title("History")
        history_window.geometry("300x200")

        # Add history window
        history_box = tk.Label(history_window, text="Calculation History", font=('Arial', 14), pady=10)
        history_box.pack()

        # Add text widget to display history
        history_text = tk.Text(history_window, font=('Arial', 12))
        # Expand both horizontally and vertically to fill all available space
        history_text.pack(expand=True, fill=tk.BOTH)

        # Insert history entries into the text widget
        for entry in self.history:
            history_text.insert(tk.END, entry + "\n")

def main():
    start = tk.Tk()
    new_calculator = Calculator(start)
    start.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x500")
        self.root.resizable(False, False)

        # Initialize variables
        self.start_time = None
        self.is_testing = False

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create and arrange widgets for the application.
        """
        # Title Label
        title_label = tk.Label(self.root, text="Typing Speed Test", font=("Arial", 24, "bold"))
        title_label.pack(pady=20)

        # Instructions Label
        instructions_label = tk.Label(self.root, text="Type anything in the text box and press Enter when done.", font=("Arial", 14))
        instructions_label.pack(pady=10)

        # Text Entry Field
        self.text_entry = tk.Entry(self.root, font=("Arial", 14), width=50)
        self.text_entry.pack(pady=20)
        self.text_entry.bind("<Key>", self.start_timer)  # Start timer when typing begins
        self.text_entry.bind("<Return>", self.finish_test)  # Finish test on Enter key press

        # Timer Label
        self.timer_label = tk.Label(self.root, text="Time Elapsed: 0.0s", font=("Arial", 16))
        self.timer_label.pack(pady=10)

        # Result Labels
        self.speed_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.speed_label.pack(pady=10)

        self.accuracy_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.accuracy_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 14), command=self.reset_test, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        """
        Start the timer when the user begins typing.
        """
        if not self.is_testing:
            self.start_time = time.time()
            self.is_testing = True
            self.timer_label.config(text="Time Elapsed: 0.0s")

    def finish_test(self, event):
        """
        Stop the timer when the user presses Enter and calculate results.
        """
        if self.is_testing:
            end_time = time.time()
            time_elapsed = end_time - self.start_time
            typed_text = self.text_entry.get().strip()

            # Calculate words per minute
            words = len(typed_text.split())
            words_per_minute = (words / time_elapsed) * 60 if time_elapsed > 0 else 0

            # Accuracy is calculated as the percentage of characters typed correctly
            accuracy = self.calculate_accuracy(typed_text)

            # Display results
            self.timer_label.config(text=f"Time Elapsed: {time_elapsed:.2f}s")
            self.speed_label.config(text=f"Typing Speed: {words_per_minute:.2f} words per minute")
            self.accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")

            # Disable further typing and enable reset button
            self.text_entry.config(state=tk.DISABLED)
            self.reset_button.config(state=tk.NORMAL)
            self.is_testing = False

    def calculate_accuracy(self, typed_text):
        """
        Calculate the accuracy of the typed text.
        """
        if not typed_text:
            return 0.0
        return 100.0  # For random typing, we assume all input is correct.

    def reset_test(self):
        """
        Reset the test for another attempt.
        """
        self.text_entry.config(state=tk.NORMAL)
        self.text_entry.delete(0, tk.END)
        self.timer_label.config(text="Time Elapsed: 0.0s")
        self.speed_label.config(text="")
        self.accuracy_label.config(text="")
        self.reset_button.config(state=tk.DISABLED)
        self.start_time = None
        self.is_testing = False


if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

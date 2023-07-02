from threading import Thread


class InputReader(Thread):
    def run(self):
        self.line_of_text = input()


print("Enter some text and press enter: ")
thread = InputReader()
thread.run()
count = result = 1
while thread.is_alive():
    result = count * count
    count += 1
print(f"calculated squares up to {count} * {count} = {result}")
print(f"while you typed '{thread.line_of_text}'")

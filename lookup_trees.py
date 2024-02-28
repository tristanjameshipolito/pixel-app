import subprocess

def open_brave(start_num):
    try:
        for i in range(start_num, start_num + 10):
            url = f"https://play.pixels.xyz/pixels/share/{i}"
            # Specify the command to open Brave browser on macOS with the URL
            subprocess.Popen(['open', '-a', 'Brave Browser', url])
        print("Brave browser tabs are opened successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        start_num_input = input("Enter the starting number (or 'q' to quit): ")
        if start_num_input.lower() == 'q':
            break
        try:
            start_num = int(start_num_input)
            open_brave(start_num)
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
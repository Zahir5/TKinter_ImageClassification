import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from trained_model import ImageClassifier

class GUIComponent:
    # Class variable to hold the ImageClassifier instance
    classifier = ImageClassifier()

    def __init__(self, root, title, column):
        self.root = root
        self.root.title(title)

        # Create a frame
        self.frame = tk.Frame(root, borderwidth=2, relief="solid")
        self.frame.grid(row=0, column=column, padx=10, pady=10)

        # Create a button
        self.button = tk.Button(self.frame, text="Upload Image", command=self.upload_and_display)
        self.button.pack(pady=10)

        # Create label to display the uploaded image
        self.image_label = tk.Label(self.frame)
        self.image_label.pack()

        # Create label for success message
        self.success_label = tk.Label(self.frame, text="")
        self.success_label.pack()

    def upload_and_display(self):
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        if file_path:
            # Display the uploaded image in the GUI
            self.display_uploaded_image(file_path)

            # Classify the uploaded image using the ImageClassifier
            predictions = self.classifier.classify_image(file_path)

            # Display the top prediction label in the GUI
            self.success_label.config(text=f"Prediction: {predictions[0][0]}")

    def display_uploaded_image(self, file_path):
        image = Image.open(file_path)
        # Change the size to make the block larger
        image = image.resize((200, 200), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image=image)

        # Update the label with the uploaded image
        self.image_label.config(image=photo)
        self.image_label.image = photo


class Frame1(GUIComponent):
    def __init__(self, root):
        super().__init__(root, "Frame 1 - Image Uploader", 0)

    # Override the upload_and_display method for Frame1
    def upload_and_display(self):
            print("Frame 1 specific behavior and for simplicity purpose nothing was implemented here")

            # Call the base class method
            super().upload_and_display()


class Frame2(GUIComponent):
    def __init__(self, root):
        super().__init__(root, "Frame 2 - Image Uploader", 1)

    # Override the upload_and_display method for Frame2
    def upload_and_display(self):
            print("Frame 2 specific behavior")

            # Call the base class method
            super().upload_and_display()


class Frame3(GUIComponent):
    def __init__(self, root):
        super().__init__(root, "Frame 3 - Image Uploader", 2)

    # Override the upload_and_display method for Frame3
    def upload_and_display(self):
            print("Frame 3 specific behavior")

            # Call the base class method
            super().upload_and_display()


class ImageUploaderClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x300")  # Adjust the dimensions as needed

        # Create frames using subclasses
        self.frame1 = Frame1(root)
        self.frame2 = Frame2(root)
        self.frame3 = Frame3(root)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageUploaderClassifierApp(root)
    root.mainloop()

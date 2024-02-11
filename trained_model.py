import torch
from torchvision import models, transforms
from PIL import Image

class ImageClassifier:
    def __init__(self, model_name="resnet101", labels_path="imagenet_classes.txt"):
        # Loading the model
        if model_name == "resnet101":
            self.model = models.resnet101(pretrained=True)
        else:
            raise ValueError("Unsupported model name")

        # Setting the model to evaluation mode
        self.model.eval()

        # Loading labels
        with open(labels_path) as f:
            self.classes = [line.strip() for line in f.readlines()]

        # Defining the image transformation
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )
        ])

    def classify_image(self, image_path):
        # Open and transform the image
        img = Image.open(image_path)
        img_t = self.transform(img)
        batch_t = torch.unsqueeze(img_t, 0)

        # Carry out inference
        out = self.model(batch_t)

        # Processing the results
        _, indices = torch.sort(out, descending=True)
        percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100
        result = [(self.classes[idx], percentage[idx].item()) for idx in indices[0][:5]]

        return result


if __name__ == "__main__":
    classifier = ImageClassifier()

    image_path = "dog.jpg"
    predictions = classifier.classify_image(image_path)
    print(predictions[0][0])

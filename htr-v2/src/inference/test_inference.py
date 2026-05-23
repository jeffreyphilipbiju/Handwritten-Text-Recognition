from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load processor and model
processor = TrOCRProcessor.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

model = VisionEncoderDecoderModel.from_pretrained(
    "microsoft/trocr-base-handwritten"
)

# Load image
image = Image.open("sample.png").convert("RGB")

# Resize image
image = image.resize((384, 128))

# Display image
plt.imshow(image)
plt.axis("off")
plt.show()

# Convert image to model input
pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

# Generate text
generated_ids = model.generate(
    pixel_values,
    max_new_tokens=50
)

# Decode prediction
generated_text = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True
)[0]

print("\nPrediction:", generated_text)
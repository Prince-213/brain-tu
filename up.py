import cv2

# Load the pre-trained super-resolution model
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Read the image
print("Reading image")
image = cv2.imread('images/Curious.Caterer.Forbidden.Fruit.2024.jpg')
# Read the model
print("Reading Model")
model_path = "models/EDSR_x4.pb"  # You can choose from various models: EDSR, ESPCN, FSRCNN, etc.
#You would need to install the model.
sr.readModel(model_path)

# Set the model and scale to be used
print("Setting Model scale")
sr.setModel("edsr", 4)  # EDSR model with a scaling factor of 4

# Upscale the image
print("upscalling the image")
upscaled_image = sr.upsample(image)

# Save the output
print("scaling upscaled image")
cv2.imwrite('upscaled_image.jpg', upscaled_image)

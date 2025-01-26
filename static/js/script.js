function viewImage(imageName) {
  // Get the modal and image elements
  const modal = document.getElementById('fullImageModal');
  const fullImage = document.getElementById('fullImage');
  
  // Set the image source to the clicked image's URL
  fullImage.src = '/image/' + imageName;

  // Show the modal
  modal.style.display = 'flex';
}

function closeModal() {
  // Hide the modal when clicked
  const modal = document.getElementById('fullImageModal');
  modal.style.display = 'none';
}

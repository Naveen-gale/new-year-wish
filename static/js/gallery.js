let currentIndex = 0;

// Open the Modal
function openModal(index) {
    currentIndex = parseInt(index);
    updateModalContent();
    document.getElementById('modal').style.display = "block";
}

// Close the Modal
function closeModal() {
    document.getElementById('modal').style.display = "none";
}

// Next/Prev Controls
function changeSlide(n) {
    currentIndex += n;
    
    // Loop back to start if at the end
    if (currentIndex >= friendsData.length) {
        currentIndex = 0;
    } 
    // Loop to end if at the start
    if (currentIndex < 0) {
        currentIndex = friendsData.length - 1;
    }
    
    updateModalContent();
}

// Helper to update Image & Name
function updateModalContent() {
    const friend = friendsData[currentIndex];
    const imgElement = document.getElementById("full-image");
    const captionElement = document.getElementById("caption");
    
    // Add fade effect
    imgElement.style.opacity = 0;
    
    setTimeout(() => {
        imgElement.src = friend.src;
        captionElement.innerText = friend.name;
        imgElement.style.opacity = 1;
    }, 200);
}

// Keyboard Navigation (Optional handy feature)
document.addEventListener('keydown', function(event) {
    if (document.getElementById('modal').style.display === "block") {
        if (event.key === "ArrowLeft") changeSlide(-1);
        if (event.key === "ArrowRight") changeSlide(1);
        if (event.key === "Escape") closeModal();
    }
});
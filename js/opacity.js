const shareButtons = document.getElementById('share-buttons');
const fadeThreshold = 0.90; // Adjust as needed

window.addEventListener('scroll', () => {
  const scrollHeight = document.documentElement.scrollHeight;
  const viewportHeight = window.innerHeight;
  const scrollPosition = window.scrollY;

  if (scrollPosition >= (scrollHeight - viewportHeight) * fadeThreshold) {
    shareButtons.style.opacity = 0;
    shareButtons.style.pointerEvents = 'none'; // Disable button interaction
  } else {
    shareButtons.style.opacity = 1;
    shareButtons.style.pointerEvents = 'auto'; // Enable button interaction
  }
});
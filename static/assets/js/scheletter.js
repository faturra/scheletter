// Loading Bar
document.onreadystatechange = function () {
  var loadingBar = document.getElementById('loading-bar');
  if (document.readyState === 'complete') {
    setTimeout(function() {
      loadingBar.style.width = '100%';
      setTimeout(function() {
        loadingBar.classList.add('loaded');
        setTimeout(function() {
          loadingBar.style.opacity = '0';
        }, 500);
      }, 300);
    }, 500);
  } else {
    loadingBar.style.width = '0';
    loadingBar.style.opacity = '1';
    loadingBar.classList.remove('loaded');
  }
};

// Tooltip
$(document).ready(function () {
  $('[data-bs-toggle="tooltip"]').tooltip();
});
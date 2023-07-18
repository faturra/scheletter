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
        }, 500); // Mengubah opacity menjadi 0 setelah 500ms
      }, 300); // Tambahkan kelas 'loaded' setelah 300ms
    }, 500); // Tunda perubahan lebar selama 500ms
  } else {
    loadingBar.style.width = '0';
    loadingBar.style.opacity = '1'; // Set opacity menjadi 1 saat halaman sedang dimuat
    loadingBar.classList.remove('loaded');
  }
};

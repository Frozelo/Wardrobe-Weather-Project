<script>
  function loadContent(contentId) {
    var contentContainer = document.getElementById('content-container');
    contentContainer.innerHTML = '';

    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/' + contentId + '/', true); // Здесь предполагается, что у вас есть URL для каждого контента
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        contentContainer.innerHTML = xhr.responseText;
      }
    };
    xhr.send();
  }

  // Обработчики кликов на ссылках навигации
  document.getElementById('profile-link').addEventListener('click', function (e) {
    e.preventDefault();
    loadContent('profile');
  });

  document.getElementById('settings-link').addEventListener('click', function (e) {
    e.preventDefault();
    loadContent('settings');
  });

  document.getElementById('activity-link').addEventListener('click', function (e) {
    e.preventDefault();
    loadContent('activity');
  });


  loadContent('profile');
</script>

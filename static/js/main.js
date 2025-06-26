document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = '<i class="bi bi-sun"></i>';
    const moonIcon = '<i class="bi bi-moon"></i>';

    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            document.body.classList.toggle('dark-mode');
            document.body.classList.toggle('light-mode');

            let theme = 'light';
            if (document.body.classList.contains('dark-mode')) {
                theme = 'dark';
            }
            localStorage.setItem('theme', theme);
            updateIcon(theme);
        });
    }

    function updateIcon(theme) {
        if (theme === 'dark') {
            themeToggle.innerHTML = moonIcon;
        } else {
            themeToggle.innerHTML = sunIcon;
        }
    }

    // Apply saved theme and icon
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.classList.add(savedTheme + '-mode');
    updateIcon(savedTheme);
});

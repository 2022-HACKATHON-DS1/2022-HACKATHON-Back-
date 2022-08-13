const button = document.querySelector('#drop');

button.addEventListener('click', () => {
    const dropdown = document.querySelector('.dropdown');
    dropdown.classList.toggle('dis');
});

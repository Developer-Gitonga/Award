let exit = document.getElementById('exit');
let show = document.getElementById('show');
let reopen = document.getElementById('reopen');

show.style.display = 'none';

reopen.addEventListener('click', () => {
    show.style.display = 'flex';
});

exit.addEventListener('click', function() {
    show.style.display = 'none';
});

let sharebtn = document.getElementById('sharebtn');
let share = document.getElementById('share');

sharebtn.addEventListener('click', function() {
    share.select()
    document.execCommand('copy');
});
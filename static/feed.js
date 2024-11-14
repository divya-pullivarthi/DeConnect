document.addEventListener('DOMContentLoaded', function() {
    const dropbtn = document.querySelector('.dropbtn');
    const dropdownContent = document.querySelector('.dropdown-content');

    dropbtn.addEventListener('click', function(event) {
        event.preventDefault();
        dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
    });

    window.addEventListener('click', function(event) {
        if (!event.target.closest('.dropdown')) {
            if (dropdownContent.style.display === 'block') {
                dropdownContent.style.display = 'none';
            }
        }
    });

    
    const likeButton = document.querySelector('.like-button');
    const likeCount = document.getElementById('like-count');
    const likeIcon = document.getElementById('like-icon');
    let liked = false;

    likeButton.addEventListener('click', function() {
        let count = parseInt(likeCount.textContent);
        if (liked) {
            count--;
            likeIcon.classList.remove('fas');
            likeIcon.classList.add('far');
        } else {
            count++;
            likeIcon.classList.remove('far');
            likeIcon.classList.add('fas');
        }
        liked = !liked;
        likeCount.textContent = `${count} Likes`;
    });
});

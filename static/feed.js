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

    
    const likeButton1 = document.querySelector('.like-button-1');
    const likeCount1 = document.getElementById('like-count-1');
    const likeIcon1 = document.getElementById('like-icon-1');
    let liked1 = false;

    likeButton1.addEventListener('click', function() {
        let count = parseInt(likeCount1.textContent);
        if (liked1) {
            count--;
            likeIcon1.classList.remove('fas');
            likeIcon1.classList.add('far');
        } else {
            count++;
            likeIcon1.classList.remove('far');
            likeIcon1.classList.add('fas');
        }
        liked1 = !liked1;
        likeCount1.textContent = `${count} Likes`;
    });

    const likeButton2 = document.querySelector('.like-button-2');
    const likeCount2 = document.getElementById('like-count-2');
    const likeIcon2 = document.getElementById('like-icon-2');
    let liked2 = false;

    likeButton2.addEventListener('click', function() {
        let count = parseInt(likeCount2.textContent);
        if (liked2) {
            count--;
            likeIcon2.classList.remove('fas');
            likeIcon2.classList.add('far');
        } else {
            count++;
            likeIcon2.classList.remove('far');
            likeIcon2.classList.add('fas');
        }
        liked2 = !liked2;
        likeCount2.textContent = `${count} Likes`;
    });
});

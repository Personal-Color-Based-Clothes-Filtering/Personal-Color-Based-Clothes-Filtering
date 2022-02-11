function slideCarousel(e){
    const clickedButton = document.getElementById(e.target.id)
    const productList = clickedButton.parentNode.previousSibling.previousSibling
    
    switch(clickedButton.className){
        case 'next':
            productList.style.transform = 'translateX(-101%)';
            productList.style.transitionDuration = '500ms';
            break;
        case 'prev':
            productList.style.transform = `translateX(0%)`;
            productList.style.transitionDuration = '500ms';
            break;
    }
}

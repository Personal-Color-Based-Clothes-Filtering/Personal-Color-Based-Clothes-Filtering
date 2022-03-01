function createPagingUrl(pageNumber){
    let current = window.location.href
    let pageUrl = ''
    if(current.includes('?')){
        if(current.includes('?page')){
            pageUrl = current.split('=')[0] + '=' + pageNumber 
        }else{
            pageUrl = current + '&page=' + pageNumber
        }
    }else{
        pageUrl = current + '?page=' + pageNumber
    }
    location.href = pageUrl
}
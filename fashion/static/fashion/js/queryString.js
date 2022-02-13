/*
필터링 요소에 onchange 혹은 onclick 이벤트를 건다
onclick 이벤트=
category,tone,color의 값을 클릭 요소의 id로 설정. 이를 쿼리스트링으로 만들어 ajax로 서버에 요청

onclick collar => setCategory() => $category.change(function(){
    getFiltering()
})
 */


let category='all';
let tone='all';
let color='all';
function setOption(e){
    alert(e.target.className)
    switch(e.target.className){
        case 'category':
            alert('category')
            category = e.target.id;
            break;
        case 'tone':
            alert('tone')
            tone = e.target.id;
            break;
        case 'color':
            alert('color')
            color = e.target.id;
            break;
    }
    console.log(category,tone,color);
    requestFilteringObjects(category,tone,color);
}

function requestFilteringObjects(category,tone,color){
    $.ajax({
        url:`/shopping/?category=${category}&tone=${tone}&color=${color}`,
        type:'GET',
        data:{
            //생략 가능
        },
        success:function(response){
            $("body").html(response)
        }
    })
    
}
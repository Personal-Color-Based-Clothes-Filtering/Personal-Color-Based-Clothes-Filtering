$(document).ready(function(){
    // 파일명 불러오기
    var fileTarget = $('.filebox .upload-hidden');
 
     fileTarget.on('change', function(){
         if(window.FileReader){
             // 파일명 추출
             var filename = $(this)[0].files[0].name;
         } 
 
         else {
             // Old IE 파일명 추출
             var filename = $(this).val().split('/').pop().split('\\').pop();
         };
         $(this).siblings('.upload-name').val(filename);
     });
 
     // 썸네일 불러오기
     var imgTarget = $('.preview-image .upload-hidden');
 
     imgTarget.on('change', function(){
         var parent = $(this).parent();
         parent.children('.upload-display').remove();
 
         if(window.FileReader){
             //image 파일만
             if (!$(this)[0].files[0].type.match(/image\//)) return;
             
             var reader = new FileReader();
             reader.onload = function(e){
                 var src = e.target.result;
                 document.getElementById("preview-image").src=src;
             }
             reader.readAsDataURL($(this)[0].files[0]);
         }
     });
 });

//로딩중 구성 js.
function test(imageName) {
    LoadingWithMask('./face/static/face/image' + imageName);
    setTimeout("closeLoadingWithMask()", 19000);
}
 
function LoadingWithMask(gif) {
    //화면의 높이와 너비 구하기.
    var maskHeight = $(document).height();
    var maskWidth  = window.document.body.clientWidth;
     
    //화면에 출력할 마스크 설정하기.
    var mask       ="<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
    var loadingImg ='';
    
    loadingImg +=" <img src='.face/static/face/image"+ gif +"' style='position: absolute; display: block; margin: 0px auto;'/>";

    //화면에 레이어 추가
    $('body')
        .append(mask)
 
    //마스크의 높이와 너비를 화면 것으로 만들어 전체 화면을 채우기.
    $('#mask').css({
            'width' : maskWidth,
            'height': maskHeight,
            'opacity' :'0.3'
    });
  
    //마스크 표시
    $('#mask').show();
  
    //로딩중 이미지 표시
    $('#loadingImg').append(loadingImg);
    $('#loadingImg').show();
}
 
function closeLoadingWithMask() {
    $('#mask, #loadingImg').hide();
    $('#mask, #loadingImg').empty(); 
}
//로딩중 구성 js 끝
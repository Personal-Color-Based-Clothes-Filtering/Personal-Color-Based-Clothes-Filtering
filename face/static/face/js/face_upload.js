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

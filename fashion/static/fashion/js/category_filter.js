const url = window.location.href;

var category = url.href.split('#').pop(); //collar
//document.getElementById("") 

if (category == 'collar'){
    document.write(category);
  }
  else {
    document.write('category');
  }

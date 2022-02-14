function reducer(state,action){
    if(state === undefined){
        return {category:'all',color:'all'}
    }

    let newState;
    if(action.type === 'CHANGE_COLOR'){
        newState = Object.assign({},state,{color:action.color});
    }
    if(action.type === 'CHANGE_CATEGORY'){
        newState = Object.assign({},state,{category:action.category});
    }
    console.log(action.type,action,state,newState);
    return newState;
}

let store = Redux.createStore(
    reducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)
console.log(store.getState());


function setOption(e,tone){
    let category='all';
    let color='all';

    switch(e.target.className){
        case 'category':
            category = e.target.id;
            store.dispatch({type:'CHANGE_CATEGORY',category:category});
            break;
        case 'color':
            color = e.target.id;
            store.dispatch({type:'CHANGE_COLOR',color:color});
            console.log(color)
            break;
    }

    requestFilteringObjects(tone);
}

function requestFilteringObjects(tone){
    let category = store.getState().category;
    let color = store.getState().color;
    $.ajax({
        url:`/shopping/list/${tone}/`,
        type:'GET',
        data:{
            category:category,
            color:color
        },
        success:function(response){
            let clothes_list = document.createElement('div');
            clothes_list.setAttribute('id','clothes-list');
            clothes_list.className = 'clothes-list';
            response = JSON.parse(response);

            if(!response.length){
                console.log('No product')
                $('#clothes-list').html(`
                    <div class="no-product">해당하는 상품이 존재하지 않습니다.</div>
                `)
            }else{
                response.map((item,index)=>{
                let id = item.pk;
                let url = item.fields.url;
                let thumbnail = item.fields.thumbnail;
                let brand = item.fields.brand;
                let name = item.fields.name;
                let category = item.fields.category;
                let color = item.fields.color;
                let tone = item.fields.tone;
                let price = item.fields.price;
                let discount_price = item.fields.discount_price;

                let clothes_item = document.createElement('div');
                clothes_item.className = 'clothes-item';

                let clothes_url = document.createElement('a');
                clothes_url.setAttribute('href',url);

                let clothes_img = document.createElement('img');
                clothes_img.setAttribute('src',thumbnail);
                clothes_img.setAttribute('alt',name);
                clothes_img.className = 'thumbnail';

                let clothes_brand = document.createElement('p');
                clothes_brand.innerText = brand;
                clothes_brand.className = 'brand';

                let clothes_name = document.createElement('p');
                clothes_name.innerText = name;
                clothes_name.className = 'name';

                let clothes_price = document.createElement('p');
                clothes_price.innerText = `${price}원`;
                clothes_price.className = 'price';

                let clothes_discount_price = document.createElement('p');
                clothes_discount_price.innerText = `${discount_price}원`;
                clothes_discount_price.className = 'discount_price';
                

                clothes_url.appendChild(clothes_img)
                clothes_url.appendChild(clothes_brand)
                clothes_url.appendChild(clothes_name)
                clothes_url.appendChild(clothes_price)
                clothes_url.appendChild(clothes_discount_price)
                clothes_item.appendChild(clothes_url)
                clothes_list.appendChild(clothes_item)
            })

            $('#clothes-container').html(clothes_list)
            }
        }
    })
}

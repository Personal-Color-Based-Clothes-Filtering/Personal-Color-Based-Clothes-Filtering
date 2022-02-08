import data from './sweater.js';

window.onload = () => {
    loadImage()
}

//console.log(data[3])
const container = document.getElementById('container')
const loadImage = () => {
    for(let i=0;i<data.length;i++){
        /* 엘리먼트 생성 */
        let item = document.createElement('div')
        let thumbnail = document.createElement('img')
        let info = document.createElement('p')
        let tone = document.createElement('p')

        /* 속성 설정 */
        item.setAttribute('class','item')
        thumbnail.setAttribute('class','thumbnail')
        thumbnail.setAttribute('src',data[i].thumbnail)
        info.setAttribute('class','info')
        tone.setAttribute('class','tone')

        /* 정보 삽입 */
        info.textContent = data[i].index + ') '+ data[i].name
        tone.textContent = data[i].tone

        /* dom에 추가 */
        item.appendChild(thumbnail)
        item.appendChild(info)
        item.appendChild(tone)
        container.appendChild(item)
    }
}
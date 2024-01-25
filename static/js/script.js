function Request(){
  return {
       fio : document.querySelector('#input_fio').value,
       organization : document.querySelector('#input_organization').value,
       description : document.querySelector('#input_description').value,
       contact : document.querySelector('#input_contact').value,
       price : Number(document.querySelector('#input_price').value),
  }
}

const requestURL = 'http://192.168.0.109:2000/'

function sendRequest(method, url, body = null) {
const requestOptions = {
method: method,
headers: {
       'Content-Type': 'application/json'
       }
};

if (body !== null) {
requestOptions.body = JSON.stringify(body);
}

 return fetch(url, requestOptions)
               .then(response => {
return response.json();
});
}

document.getElementById('button_1').addEventListener('click', () => {
  document.getElementById('application').style = 'display: flex;animation: appearAnimation 1s ease;'
   });

document.getElementById('button_2').addEventListener('click', () =>{
    if (Request().fio.length >=10 ){
      document.getElementById("p1").style.color = 'rgba(255, 251, 0, 0)'
      if(Request().organization.length >=3){
        document.getElementById("p2").style.color = 'rgba(255, 251, 0, 0)'
        if(Request().description.length >=25 && Request().description.length <=255 ){
          document.getElementById("p3").style.color = 'rgba(255, 251, 0, 0)'
          if(Request().contact.length >=10){
            document.getElementById("p4").style.color = 'rgba(255, 251, 0, 0)'
            if(isNaN(Request().price-0)){
              document.getElementById("p5").innerHTML='Введите стоимость'
            }else{
                document.getElementById("p5").style.color = 'rgba(255, 251, 0, 0)'
                sendRequest('POST', requestURL, Request()).then(data=>console.log(data)).catch(err=>console.log(err))
                document.getElementById("h3_true").innerHTML='Ваша заявка на расмотрении '
                document.getElementById("application").style = 'display: none; '
            }
          }else{document.getElementById("p4").innerHTML='неполные даннвые'}
        }else if(Request().description.length >= 255){
          document.getElementById("p3").innerHTML='Количество символов не должно привышать 255'  
        }else{
          document.getElementById("p3").innerHTML='Количество символов не должно быть мение 25'
        }
      }else{
        document.getElementById("p2").innerHTML='неполные даннвые'  
      }
    }else{
      document.getElementById("p1").innerHTML='неполные даннвые'
    }
  });


  document.getElementById('exit').addEventListener('click',()=>{
    document.getElementById('application').style.display = 'none'
  })



if(window.location.pathname=='/level/'){
    if(sessionStorage.getItem('point') !=undefined ){}


}

if(window.location.pathname=='/game/1/'|| window.location.pathname=='/game/2/'|| window.location.pathname=='/game/3/'){

    if(sessionStorage.getItem('win')==undefined  ){

        let gw=0
        sessionStorage.setItem('win', gw);
    }
    if(sessionStorage.getItem('point')==undefined ){
        let pt=0
        sessionStorage.setItem('point', pt);
    }
    let point = sessionStorage.getItem('point');
    console.log("Nombre de point :"+point)
    let data = sessionStorage.getItem('win');

    console.log(data)
    console.log("Nombre de victoire "+data)
    let findW= document.getElementById('findW')
    findW.innerHTML="Vous avez trouver "+data+"/5 ! "

    if(data ==5){
        sessionStorage.removeItem('win');

        console.log("Vous êtes le super vainqueur")
    }
    let url=window.location.pathname
    url=url.split('')
    console.log(url)
    let urlId=""
    for(let i=0;i<url.length;i++){
        let ur= parseInt(url[i])
        if(Number.isInteger(ur)){
            urlId=url[i]
        }
    }
    console.log(urlId)

    let sn=0
    let mn=0
    let hn=0
    function time(){
        sn = sn+1

        if(sn==60){
            sn=0
            mn=mn+1
        }
        if(mn==60){
            mn=0
            hn=hn +1
        }
        if(hn>0){
            if(sn<10){
                timer.innerHTML=hn+":"+mn+":0"+sn
            }
            else{
                timer.innerHTML=hn+":"+mn+":"+sn
            }
        }
        else{
            if(sn<10){
                timer.innerHTML=mn+":0"+sn
            }
            else{
                timer.innerHTML=mn+":"+sn
            }

        }


    }

    setInterval(time,1000)




    let word= document.getElementById('word')
    let tab= document.getElementById('tabW')
    let pendu= document.getElementById('pendu')
    let err= document.getElementById('err')
    let timer= document.getElementById('timer')
    let cont=word.innerHTML
    tab=tab.innerHTML
    console.log(cont)
    console.log(tab)
    cont=cont.toUpperCase()
    let arr=cont.split('')
    let verif=[].concat(arr)
    let arr_replace=[]
    for(let i=0;i<verif.length;i++){
        arr_replace.push('_')
    }
    let newArr=[].concat(arr_replace)
    arr_replace=arr_replace.join(" ")
    console.log(arr_replace)
    pendu.innerHTML=arr_replace
    tab=tab.toUpperCase()
    tab=tab.split('')
    console.log(tab)
    let key = document.getElementById('keyboard')

    let countEr=0
    //let finPendu=[]

    Array.prototype.push.apply(arr, tab);
    console.log(arr)

    function shuffleArray(inputArray){
        inputArray.sort(()=> Math.random() - 0.5);
    }

    shuffleArray(arr);
    let try_2=3
    function addKey(texte){
        console.log(texte)
      key.innerHTML +="<button class='evClick btn btn-primary'>"+texte+"</button>";
    }
    function getAllIndexes(arr, val) {
        var indexes = [], i;
        for(i = 0; i < arr.length; i++)
            if (arr[i] === val)
                indexes.push(i);
         return indexes
    }
    for(let i = 0;i<arr.length;i++){
       addKey(arr[i]);
    }
    let but= document.querySelectorAll('.evClick')
    console.log(but)
    err.innerHTML= "Vous avez le droit à "+ try_2+ " essaie"
    for(let i = 0;i<but.length;i++){

        but[i].addEventListener("click", function (event) {
            let letter=event.target.innerText
            console.log(verif)
            let resp=verif.find(element => element == letter)
            if(resp==undefined){
                console.log('faux')
                try_2 -=1
                err.innerHTML= "Vous avez le droit à "+ try_2+ " essaie"
                countEr +=1
                console.log(countEr)

                if(countEr == 3){
                    timer.style.display = "none";
                    err.innerHTML= "Vous avez perdu!! LOOOOOOSER"
                    countEr=0
                }

            }
            else{
                let  finPendu=getAllIndexes(verif,resp)
                console.log(finPendu.length)
                for(let i =0; i<finPendu.length;i++){
                    newArr[finPendu[i]]=resp
                    console.log(resp)
                    console.log(newArr[finPendu[i]])
                    console.log(finPendu[i])

                }
                const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);

                equals(verif, newArr);
                if(equals(verif, newArr) ==true){
                    let timeWin=[]
                    if(hn<1){
                        timeWin=[mn,sn];
                    }
                    else{
                        timeWin=[hn,mn,sn];
                    }

                    let tt=timeWin.join(':')
                    timer.style.display = "none";
                    console.log(timeWin)
                    console.log(tt)
                    let dataW=sessionStorage.getItem('win');
                    dataW=parseInt(dataW)
                    console.log(typeof(dataW))
                    dataW=dataW+1
                    console.log(dataW)
                    sessionStorage.setItem('win', dataW);
                    console.log("Victoire = "+sessionStorage.getItem('win'))
                     let pointU=sessionStorage.getItem('point');
                     pointU=parseInt(pointU)
                     if(urlId==1){
                        pointU +=20
                    }
                    else if(urlId==2){
                        pointU +=40
                    }
                    else{
                        pointU +=80
                    }
                    sessionStorage.setItem('point', pointU);
                    err.innerHTML= "Vous avez Gagner en   "+tt

                }
            }
            console.log(newArr)

            pendu.innerHTML=newArr.join(' ')
            console.log(event.target.innerText)
        }, false);

    }
}
console.log(window.location.pathname);
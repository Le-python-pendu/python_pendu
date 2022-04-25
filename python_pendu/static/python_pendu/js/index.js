console.log(5899)
console.log("la vue est chaude")
let word= document.getElementById('word')
let pendu= document.getElementById('pendu')
let cont=word.innerHTML
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
let tab=["a",'b','c','d','e','f','g'];
tab=tab.join('')
tab=tab.toUpperCase()
tab=tab.split('')
let key = document.getElementById('keyboard')

let countEr=0
//let finPendu=[]

Array.prototype.push.apply(arr, tab);
console.log(arr)

function shuffleArray(inputArray){
    inputArray.sort(()=> Math.random() - 0.5);
}

shuffleArray(arr);

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
for(let i = 0;i<but.length;i++){

    but[i].addEventListener("click", function (event) {
        let letter=event.target.innerText
        console.log(verif)
        let resp=verif.find(element => element == letter)
        if(resp==undefined){
            console.log('faux')
            countEr +=1
            console.log(countEr)

        if(countEr == 3){
            console.log("Vous avez perdu");
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


            console.log('Vrai')

        }
        console.log(newArr)
        pendu.innerHTML=newArr.join(' ')
		console.log(event.target.innerText)
	}, false);

}



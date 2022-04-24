console.log(5899)
console.log("la vue est chaude")
let word= document.getElementById('word')
let cont=word.innerHTML
cont=cont.toUpperCase()
let arr=cont.split('')
let verif=[].concat(arr)
let tab=["a",'b','c','d','e','f','g'];
tab=tab.join('')
tab=tab.toUpperCase()
tab=tab.split('')
let key = document.getElementById('keyboard')

let countEr=0

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
            console.log('Vrai')
        }
		console.log(event.target.innerText)
	}, false);

}


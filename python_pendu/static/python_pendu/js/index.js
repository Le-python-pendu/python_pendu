console.log(5899)
console.log("la vue est chaude")

let tab=["a",'b','c','d','e','f','g'];
let key = document.getElementById('keyboard')
let word= document.getElementById('word')
let cont=word.innerHTML
cont=cont.toUpperCase()
let arr=cont.split('')
console.log(cont)

function shuffleArray(inputArray){
    inputArray.sort(()=> Math.random() - 0.5);
}


shuffleArray(arr);

function ajoutElementTexte(texte){

  key.innerHTML +="<button class='btn btn-primary'>"+texte+"</button>";
}

for(let i = 0;i<arr.length;i++){
   ajoutElementTexte(arr[i]);
}
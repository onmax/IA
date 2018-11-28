const stations = ["Beruni","Tinchlik", "Chorsu","Gafur Golum", "Pakhtakor", "Uzbekistan","Kosmonavtlar", "Oybek", "Toskent", "Mashinasozlar", "Dostlik", "Olmazor", "Chilonzor", "Mirzo Ulugbek", " Novza", "MilliyBog", "Bunyodkor", "Mustakillik Maydoni", "Amir Temur Hiyoboni", "Khamid Alimjan", "Pushkin", "Buyuj Ipak Yuli", "Shakhirston", "Bodomzor", "Minor", "Abdulla Kodiriy", "Alisher Navoi", "Ming Urik", "Yunus Rajably"]
console.table(stations)
const img = document.querySelector('img')


res = []
img.addEventListener('click', (e) => {
    x = e.clientX;
    y = e.clientY;
    const index = prompt("Indice de la estacion?");
    if(index >= 0 && index < stations.length){
        station = stations[index];
        res.push({x,y,station});
        console.log(res);
    }else{
        console.error("NO existe ese indice, vuelve a intentarlo.")
    }

})
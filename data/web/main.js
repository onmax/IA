const stations = ["Beruni", "Tinchlik", "Chorsu", "Gafur Golum", "Pakhtakor", "Uzbekistan", "Kosmonavtlar", "Oybek", "Toskent", "Mashinasozlar", "Dostlik", "Olmazor", "Chilonzor", "Mirzo Ulugbek", " Novza", "MilliyBog", "Bunyodkor", "Mustakillik Maydoni", "Amir Temur Hiyoboni", "Khamid Alimjan", "Pushkin", "Buyuj Ipak Yuli", "Shakhirston", "Bodomzor", "Minor", "Abdulla Kodiriy", "Alisher Navoi", "Ming Urik", "Yunus Rajably"]
console.table(stations)
const img = document.querySelector('img')


res = []
img.addEventListener('click', (e) => {

    x = e.offsetX;
    y = img.offsetHeight - e.offsetY;

    const index = prompt("Indice de la estacion?");
    if (index >= 0 && index < stations.length) {
        station = stations[index];
        res.push({
            x,
            y,
            station
        });
        console.log(res);
        document.getElementById('data').innerHTML = JSON.stringify(res);
    } else {
        console.error("NO existe ese indice, vuelve a intentarlo.")
    }

})
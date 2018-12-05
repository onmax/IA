console.log(simpleRoute);

const time = simpleRoute.flat().reduce((t,station) =>  t + station.time,0);
const h3 = document.createElement('h3');
h3.innerHTML = `${time} minutos`;
const results = document.querySelector('.results')

const timeTaken = document.createElement('div')
timeTaken.classList.add('time-taken')
const icon = document.createElement('i')
icon.className = 'far fa-clock'
timeTaken.appendChild(icon)

let date = new Date(new Date().getTime() + time*60000)
const h5 = document.createElement('h5');
h5.innerHTML = `${date.getHours()}:${date.getMinutes()}`
timeTaken.appendChild(h5)

results.append(h3);
results.append(timeTaken);


const routeDiv = document.createElement('div');
routeDiv.classList.add('routeDiv')
simpleRoute.map((station,i) => {
	const stationDiv = document.createElement('div'); 
	//<div></div>

	stationDiv.classList.add('station');
	//<div class="station"></div>

	const dot = document.createElement('div');
	//<div></div>
	const top = document.createElement('div');
	top.classList.add('top');

	const bottom = document.createElement('div');
	bottom.classList.add('bottom');

	dot.classList.add('dot');

	if(station.length == 1){
		top.classList.add(station[0].line);
		bottom.classList.add(station[0].line);
	} else{
		top.classList.add(station[0].line);
		bottom.classList.add(station[1].line);
	}

	dot.appendChild(top)
	dot.appendChild(bottom)

	const h6 = document.createElement('h6');
	//<h6></h6>
	h6.innerHTML = station[0].name;

	stationDiv.appendChild(dot)
	stationDiv.appendChild(h6)

	routeDiv.appendChild(stationDiv);
	results.append(routeDiv);
	if (i < simpleRoute.length - 1){
		const line = document.createElement('div');
		line.classList.add('line');
		routeDiv.appendChild(line);
	}
})

maxWidth = simpleRoute.length * 100;
routeDiv.style.maxWidth = maxWidth + 'px';

const simpleRoute_names = ["sol","Atocha","Gran Vías"]

// The app instance creator
new autoComplete({
	dataSrc: simpleRoute_names,

	placeHolderLength: 26,
	maxResults: 9,
	highlight: true,
	dataAttribute: {
		tag: "set",
		value: "value"
	},
	onSelection: value => {
		document.querySelector(".selection").innerHTML = value.id;
	}
});

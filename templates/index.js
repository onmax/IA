const stations =[
	[
		{
			name: 'Sol',
			line: 'blue',
			time: 0,
			nstation: 0
		}
	],
	
	[
		{
			name: 'Atocha',
			line:'blue',
			time: 10,
			nstation: 4
		},{
			name:'Estación del Arte',
			line: 'green',
			time: 10,
			nstation: 5
		}
	],
	
	[
		{
			name: 'Gran via',
			line: 'green',
			time: 15,
			nstation: 8
		}
	]
]
const time = stations.flat().reduce((t,station) =>  t + station.time,0);
const h3 = document.createElement('h3');
h3.innerHTML = `${time} minutos`;
const results = document.querySelector('.results')

let date = new Date(new Date().getTime() + time*60000)
const h5 = document.createElement('h5');
h5.innerHTML = `${date.getHours()}:${date.getMinutes()}`

results.append(h3);
results.append(h5);

const route = document.createElement('div');
route.classList.add('route')
stations.map((station,i) => {
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

	route.appendChild(stationDiv);
	results.append(route);
	if (i < stations.length - 1){
		const line = document.createElement('div');
		line.classList.add('line');
		route.appendChild(line);
	}
})

maxWidth = stations.length * 100;
route.style.maxWidth = maxWidth;





/*
// The app instance creator
new autoComplete({
	dataSrc: stations,
	placeHolder: "Try me...",
	placeHolderLength: 26,
	maxResults: 10,
	highlight: true,
	dataAttribute: {
		tag: "set",
		value: "value"
	},
	onSelection: value => {
		document.querySelector(".selection").innerHTML = value.id;
	}
});
*/
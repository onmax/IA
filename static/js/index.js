if (simpleRoute.length) {
  console.log(time);
  time = Math.ceil(time);
  const h3 = document.createElement('h3');
  h3.innerHTML = `${time} minutos`;
  const results = document.querySelector('.results');
  const timeTaken = document.createElement('div');
  timeTaken.classList.add('time-taken');

  const icon = document.createElement('i');
  icon.className = 'far fa-clock';
  timeTaken.appendChild(icon);

  let date = new Date(new Date().getTime() + time * 60000);
  const h5 = document.createElement('h5');
  let hour = date.getHours();
  if (hour < 10) {
    hour = '0' + hour;
  }
  let min = date.getMinutes();
  if (min < 10) {
    min = '0' + min;
  }
  h5.innerHTML = `Hora de llegada: ${hour}:${min}`; // hour + ':' + min
  timeTaken.appendChild(h5);

  results.append(h3);
  results.append(timeTaken);

  const routeDiv = document.createElement('div');
  routeDiv.classList.add('route');
  simpleRoute.map((station, i) => {
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

    if (station.length == 1) {
      top.classList.add(station[0].line);
      bottom.classList.add(station[0].line);
    } else {
      top.classList.add(station[0].line);
      bottom.classList.add(station[1].line);
    }

    dot.appendChild(top);
    dot.appendChild(bottom);
    stationDiv.appendChild(dot);

    const h6_1 = document.createElement('h6');
    //<h6></h6>
    stationDiv.appendChild(h6_1);
    h6_1.innerHTML = station[0].name;
    if (station.length === 2) {
      const h6_2 = document.createElement('h6');
      h6_2.innerHTML = station[1].name;
      h6_2.style.top = '70px';

      const i = document.createElement('i');
      i.className = 'fas fa-long-arrow-alt-down';
      i.style = 'font-size:18px;margin-top: 20px;color:#c0c0c0';
      stationDiv.appendChild(i);
      stationDiv.appendChild(h6_2);
    }

    routeDiv.appendChild(stationDiv);
    results.append(routeDiv);
    if (i < simpleRoute.length - 1) {
      const lineDiv = document.createElement('div');
      lineDiv.classList.add('line-box');
      const line = document.createElement('div');
      line.classList.add('line');
      const span = document.createElement('span');

      let paradas = simpleRoute[i + 1][0].nstations;
      if (i !== 0) {
        paradas -= 1;
      }
      span.innerHTML = paradas + ' paradas';
      lineDiv.appendChild(span);
      lineDiv.appendChild(line);
      routeDiv.appendChild(lineDiv);
    }
  });

  maxWidth = simpleRoute.length * 150;
  routeDiv.style.maxWidth = maxWidth + 'px';
} else {
  document.querySelector('.results').style = 'display: none;';
}

function shuffleArray(array) {
  for (var i = array.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
  return array;
}

let origin = '',
  destination = '';
// The app instance creator
new autoCompleteOrigin({
  dataSrc: shuffleArray(stations),
  placeHolderLength: 26,
  maxResults: 9,
  highlight: true,
  dataAttribute: {
    tag: 'set',
    value: 'value'
  },
  onSelection: value => {
    origin = value.id;
    sendRequest();
    document.getElementById('autoCompleteOrigin').value = value.id;
  }
});

new autoCompleteDestination({
  dataSrc: shuffleArray(stations),
  placeHolderLength: 26,
  maxResults: 9,
  highlight: true,
  dataAttribute: {
    tag: 'set',
    value: 'value'
  },
  onSelection: value => {
    destination = value.id;
    sendRequest();
    document.getElementById('autoCompleteDestination').value = value.id;
  }
});

function sendRequest() {
  if (origin === destination) {
    document.getElementById('msg').innerHTML =
      'No se puede poner el mismo origen y destino';
    return;
  }
  document.getElementById('msg').innerHTML = '';
  if (origin !== '' && destination !== '') {
    window.location.href = `/route?origin=${origin}&destination=${destination}`;
  }
}

function setTable() {
  const table = document.querySelector('.table');
  table.style.gridTemplateRows = `repeat(${scores.length}, 1fr)`;
  scores.map((a, i) => {
    const row = document.createElement('div');
    row.classList.add('row');

    const container = document.createElement('div');
    a.candidates.map(candidate => {
      const index = document.createElement('span');
      index.innerHTML = i;
      container.appendChild(index);

      const stationName = document.createElement('span');
      if (candidate.name === a.selected) {
        stationName.style.background = 'rgb(218, 214, 214)';
      }
      stationName.innerHTML = candidate.name;
      container.appendChild(stationName);

      const gScore = document.createElement('span');
      gScore.innerHTML = Math.floor(candidate.g_score);
      container.appendChild(gScore);

      const hScore = document.createElement('span');
      hScore.innerHTML = Math.floor(candidate.h_score);
      container.appendChild(hScore);

      const fScore = document.createElement('span');
      fScore.innerHTML = Math.floor(candidate.f_score);
      container.appendChild(fScore);
    });

    row.appendChild(container);
    table.appendChild(row);
  });
}
setTable();

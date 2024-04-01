const sidebar = document.getElementsByClassName("sidebar");

// Creates components of outlets that match the search result
function createOutletElement(outlet) {
  const outletContainer = document.createElement("div");
  outletContainer.classList.add("outlet");

  const outletName = document.createElement("h4");
  outletName.textContent = outlet.name;
  outletContainer.appendChild(outletName);

  const infobox = document.createElement("div");
  infobox.classList.add("infobox");
  outletContainer.appendChild(infobox);
  //
  // console.log("add_info");
  // console.log(typeof outlet.add_info);
  // for (i in outlet.add_info) {
  //   console.log(add_info[i]);
  // }
  outlet.add_info.forEach((o) => {
    const info = document.createElement("p");
    info.textContent = o;
    infobox.appendChild(info);
  });

  const waze = document.createElement("a");
  waze.title = "Waze";
  waze.href = outlet.waze;
  infobox.appendChild(waze);

  const parent = document.getElementById("sidebar");
  console.log(parent);
  parent.appendChild(outletContainer);
}

const search_form = document.getElementById("search_form");
search_form.addEventListener("submit", (event) => {
  event.preventDefault();

  const search_term = document.getElementById("search").value;
  // console.log(search_term);
  fetch("/outlets/?name=" + search_term)
    .then((response) => response.json())
    .then((data) => {
      console.log(data.add_info);
      const outletContainer = createOutletElement(data);
      initMap(data);
    })
    .catch((error) => {
      console.error("Error fetching result: ", error);
    });
});

let map;

// Function to create the embedded google map in the browser
async function initMap(data) {
  const { Map } = await google.maps.importLibrary("maps");

  const position = { lat: data.latitude, lng: data.longitude };

  map = new Map(document.getElementById("map"), {
    center: { lat: data.latitude, lng: data.longitude },
    zoom: 50,
  });

  const marker = new google.maps.Marker({
    position: { lat: data.latitude, lng: data.longitude },
    map: map,
    title: data.name,
  });
}

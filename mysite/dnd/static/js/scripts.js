

$(document).ready(function() {
  $("#generateStatsBtn").click(function() {
    var statsResult = generateStats(); // Call the function to generate stats
    $("#statsResult").html(statsResult); // Update the HTML content of the div
  });
});

function generateStats() {
  // Define an array of available values
  var availableValues = [15, 14, 13, 12, 10, 8];

  // Shuffle the array to randomize the order
  var shuffledValues = shuffleArray(availableValues);

  // Create an object to store the assigned stats
  var stats = {};

  // Assign the shuffled values to each stat
  var statNames = ["Síla", "Obratnost", "Výdrž", "Inteligence", "Moudrost", "Charisma"];
  for (var i = 0; i < statNames.length; i++) {
    var statName = statNames[i];
    stats[statName] = shuffledValues[i];
  }

  // Format the stats as HTML string
  var statsHTML = "<table class='table table-striped table-bordered forest-green'>";
  statsHTML += "<thead><tr><th>Stat</th><th>Value</th><th>Modifier</th></tr></thead>";
  statsHTML += "<tbody>";

  for (var key in stats) {
    var value = stats[key];
    var modifier = Math.floor((value - 10) / 2);

    statsHTML += "<tr>";
    statsHTML += "<td><b>" + key + "</b></td>";
    statsHTML += "<td>" + value + "</td>";
    if(modifier>0){
       statsHTML += "<td>" + "+" + modifier + "</td>";
    }else{
      statsHTML += "<td>" + modifier + "</td>";
    }

    statsHTML += "</tr>";
  }

  statsHTML += "</tbody></table>";

  return statsHTML;
}

function shuffleArray(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle
  while (0 !== currentIndex) {

    // Pick a remaining element
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // Swap it with the current element
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}




$(document).ready(function() {
    // Define arrays for classes and races
    // var classes = ["Barbar", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"];
    // var races = ["Dwarf", "Elf", "Halfling", "Human", "Dragonborn", "Gnome", "Half-Elf", "Half-Orc", "Tiefling"];

    var classes = ["Barbar", "Bard", "Klerik", "Druid", "Bojovník", "Mnich", "Paladin", "Hraničář", "Zloděj", "Čaroděj", "Černokěžník", "Kouzelník"];
    var races = ["Trpaslík", "Elf", "Halfling", "Člověk", "Drakorozený", "Gnóm", "Půl-elf", "Půl-orc", "Tiefling"];
    // Function to generate random class and race
    function generateResults() {
        var randomClass = classes[Math.floor(Math.random() * classes.length)];
        var randomRace = races[Math.floor(Math.random() * races.length)];
        return "Povolání: " + randomClass + "<br>Rasa: " + randomRace;
    }

    // Event handler for button click
    $("#generateClassRaceBtn").click(function() {
        var results = generateResults();
        $("#raceResult").html(results);
    });
});


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

//generate class and race
$(document).ready(function() {
    var classTranslations = {
        "Barbarian": "Barbar",
        "Bard": "Bard",
        "Cleric": "Klerik",
        "Druid": "Druid",
        "Fighter": "Bojovník",
        "Monk": "Mnich",
        "Paladin": "Paladin",
        "Ranger": "Hraničář",
        "Rogue": "Tulák",
        "Sorcerer": "Čaroděj",
        "Warlock": "Černokněžník",
        "Wizard": "Kouzelník"
    };

    var raceTranslations = {
        "Dwarf": "Trpaslík",
        "Elf": "Elf",
        "Halfling": "Půlčík",
        "Human": "Člověk",
        "Dragonborn": "Drakorozený",
        "Gnome": "Gnóm",
        "Half-Elf": "Půl-elf",
        "Half-Orc": "Půl-orc",
        "Tiefling": "Tiefling"
    };

    // Function to generate random class and race
    function generateResults() {
        // Fetch class data from API
        fetch('https://www.dnd5eapi.co/api/classes/')
            .then(response => response.json())
            .then(data => {
                // Get a random class from the API response
                var randomClassIndex = Math.floor(Math.random() * data.results.length);
                var randomClass = data.results[randomClassIndex].name;
                var translatedClass = classTranslations[randomClass];

                // Fetch race data from API
                fetch('https://www.dnd5eapi.co/api/races/')
                    .then(response => response.json())
                    .then(data => {
                        // Get a random race from the API response
                        var randomRaceIndex = Math.floor(Math.random() * data.results.length);
                        var randomRace = data.results[randomRaceIndex].name;
                        var translatedRace = raceTranslations[randomRace];

                        fetch('https://www.dnd5eapi.co/api/classes/' + randomClass.toLowerCase() +"/")
                            .then(response => response.json())
                            .then(classData => {
                            // Generate the result HTML
                            var resultHTML = "<h1 class='display-4'>Povolání a Rasa</h1>";
                            resultHTML += "<hr><div class='row'>";
                            resultHTML += "<div class='details col-md-8'>";
                            resultHTML += "<table class='table table-striped'>";
                            resultHTML += "<thead><tr><th scope='col'>Název</th><th scope='col'>Hodnota</th></tr></thead>";
                            resultHTML += "<tbody>";
                            resultHTML += "<tr><td>Povolání</td><td>" + translatedClass + "</td></tr>";
                            resultHTML += "<tr><td>Rasa</td><td>" + translatedRace + "</td></tr>";
                            resultHTML += "<tr><td>Životů na 1. úrovni</td><td>" + classData.hit_die + " (mám radši 2* základ)->" + 2*classData.hit_die + "</td></tr>";
                            resultHTML += "<tr><td>Kostky životů</td><td>" + classData.hit_die + "k + Odolnost</td></tr>";
                            resultHTML += "<tr><td>Odbornosti</td><td>";
                            classData.proficiency_choices.forEach(choice => {
                              resultHTML += choice.desc + "<br>";
                            });
                            resultHTML += "</td></tr>";
                            resultHTML += "</tbody>";
                            resultHTML += "</table>";
                            resultHTML += "</div>";
                            resultHTML += "<div class='col-md-4'><img src='./static/img/race_class/" + randomClass.toLowerCase() + ".jpg' width='100%' alt='povolani'></div>";
                            resultHTML += "</div>";

                            // Display the result HTML
                            $("#raceResult").html(resultHTML);
                        })
                    })
                    .catch(error => console.log(error));
            })
            .catch(error => console.log(error));
    }

    // Event handler for button click
    $("#generateClassRaceBtn").click(function() {
        generateResults();
    });
});

//throw generator
$(document).ready(function() {
  var previousRoll = null; // Variable to store the previous roll result

  $('#throwDiceBtn').click(function() {
    var diceType = parseInt($('#diceType').val());
    var diceCount = parseInt($('#diceCount').val());
    var throwResults = [];
    var sumResult = 0;

    // Generate throw results
    for (var i = 0; i < diceCount; i++) {
      var throwValue = Math.floor(Math.random() * diceType) + 1;
      throwResults.push(throwValue);
      sumResult += throwValue;
    }

    // Update previous roll
    previousRoll = {
      throwResults: throwResults,
      sumResult: sumResult,
        dice: diceType
    };

    // Show popup with results

    // Update previous roll table
    updatePreviousRollTable(previousRoll);
  });

  // Update previous roll table function
  function updatePreviousRollTable(roll) {
    var tableHTML = '<table class="table table-bordered table-striped text-center"><tr><th>Kostka</th><th>Výsledky hodů</th><th>Sečtení výsledků hodů</th></tr>';
    tableHTML += '<tr><td>' + roll.dice + '-stranná </td><td class="text-danger text-center">' + roll.throwResults.join(', ') + '</td><td class="text-center">=' + roll.sumResult + '</td></tr></table>';
    $('#previousRollTable').html(tableHTML);
  }
});






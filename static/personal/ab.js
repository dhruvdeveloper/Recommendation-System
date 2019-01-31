<!--Scripts Starts-->

function openNav() {
    document.getElementById("for_break").style.clear = "both";
}

var songByName = false;
var songByAlbum = false;
var songByArtist = false;
var MovieByGenre = false;
var MovieByTitle = false;
var ArticleByTag = false;
var FoodByIngredients = false;

function funForSongByName() {
    songByName = true;
    songByAlbum = false;
    songByArtist = false;
}

function funForSongByAlbum() {
    songByAlbum = true;
    songByName = false;
    songByArtist = false;
}

function funForSongByArtist() {
    songByArtist = true;
    songByName = false;
    songByAlbum = false;
}

function funForMoviesByGenre() {
    MovieByGenre = true;
    MovieByTitle = false;
}

function funForMoviesByTitle() {
    MovieByTitle = true;
    MovieByGenre = false;
}

function funForArticalByTag() {
    ArticleByTag = true;
}

function funForFoodByIngredients() {
    FoodByIngredients = true;
}

function counter() {
    if (songByName == true){
        document.getElementById("counter_id").innerHTML = "By Name...";
    }
    else if (songByAlbum == true){
        document.getElementById("counter_id").innerHTML = "By Album...";
    }
    else if (songByArtist == true){
        document.getElementById("counter_id").innerHTML = "By Artist...";
    }
    else {}
}

function counter_Movies() {
    if (MovieByGenre == true){
        document.getElementById("counter_id_Movies").innerHTML = "By Genre...";
    }
    else if (MovieByTitle == true){
        document.getElementById("counter_id_Movies").innerHTML = "By Title...";
    }
    else {}
}
function counter_Artical() {
    if (ArticleByTag == true){
        document.getElementById("counter_id_Artical").innerHTML = "By Tag Name...";
    }
    else {}
}
function counter_Food() {
    if (FoodByIngredients == true){
        document.getElementById("counter_id_Food").innerHTML = "By Ingredients...";
    }
    else {}
}
function hide() {
    document.getElementById("Music_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_2").style.display = "block";
    document.getElementById("input_song_name_id").style.display = "none";
    document.getElementById("input_song_Album_id").style.display = "none";
    document.getElementById("input_song_Artist_id").style.display = "none";
    if (songByName == true)
    {
        document.getElementById("input_song_name_id").style.display = "block";
    }
    else if(songByAlbum == true)
    {
        document.getElementById("input_song_Album_id").style.display = "block";
    }
    else if(songByArtist == true)
    {
        document.getElementById("input_song_Artist_id").style.display = "block";
    }
    else{
        document.getElementById("Music_div_id_2").style.display = "none";
        document.getElementById("Music_div_id_1").style.display = "block";
    }
}

function hide1() {
    document.getElementById("Movies_div_id_1").style.display = "none";
    document.getElementById("Movies_div_id_2").style.display = "block";
    document.getElementById("input_Movies_Genre_Id").style.display = "none";
    document.getElementById("input_Movies_Title_Id").style.display = "none";
    if (MovieByGenre == true)
    {
        document.getElementById("input_Movies_Genre_Id").style.display = "block";
    }
    else if(MovieByTitle == true)
    {
        document.getElementById("input_Movies_Title_Id").style.display = "block";
    }
    else{
        document.getElementById("Movies_div_id_2").style.display = "none";
        document.getElementById("Movies_div_id_1").style.display = "block";
    }
}

function hide2() {
    document.getElementById("Artical_div_id_1").style.display = "none";
    document.getElementById("Artical_div_id_2").style.display = "block";
    document.getElementById("input_Artical_Tag_Id").style.display = "none";
    if (ArticleByTag == true)
    {
        document.getElementById("input_Artical_Tag_Id").style.display = "block";
    }
    else{
        document.getElementById("Artical_div_id_2").style.display = "none";
        document.getElementById("Artical_div_id_1").style.display = "block";
    }
}

function hide3() {
    document.getElementById("Food_div_id_1").style.display = "none";
    document.getElementById("Food_div_id_2").style.display = "block";
    document.getElementById("input_Food_Ingredients_Id").style.display = "none";
    if (FoodByIngredients == true)
    {
        document.getElementById("input_Food_Ingredients_Id").style.display = "block";
    }
    else{
        document.getElementById("Food_div_id_2").style.display = "none";
        document.getElementById("Food_div_id_1").style.display = "block";
    }
}

function music_div() {
    document.getElementById("Music_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_2").style.display = "block";
    document.getElementById("Movies_div_id_2").style.display = "none";
    document.getElementById("Movies_div_id_1").style.display = "none";
    document.getElementById("Artical_div_id_2").style.display = "none";
    document.getElementById("Artical_div_id_1").style.display = "none";
    document.getElementById("Food_div_id_2").style.display = "none";
    document.getElementById("Food_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_3").style.display = "none";
    document.getElementById("Movies_div_id_3").style.display = "none";
    document.getElementById("Artical_div_id_3").style.display = "none";
    document.getElementById("Food_div_id_3").style.display = "none";
}

function Movies_div() {
    document.getElementById("Music_div_id_2").style.display = "none";
    document.getElementById("Music_div_id_1").style.display = "none";
    document.getElementById("Movies_div_id_1").style.display = "none";
    document.getElementById("Movies_div_id_2").style.display = "block";
    document.getElementById("Artical_div_id_2").style.display = "none";
    document.getElementById("Artical_div_id_1").style.display = "none";
    document.getElementById("Food_div_id_2").style.display = "none";
    document.getElementById("Food_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_3").style.display = "none";
    document.getElementById("Movies_div_id_3").style.display = "none";
    document.getElementById("Artical_div_id_3").style.display = "none";
    document.getElementById("Food_div_id_3").style.display = "none";
    document.getElementById("input_Movies_Genre_Id").style.display = "none";

}

function Artical_div() {
    document.getElementById("Music_div_id_2").style.display = "none";
    document.getElementById("Music_div_id_1").style.display = "none";
    document.getElementById("Movies_div_id_2").style.display = "none";
    document.getElementById("Movies_div_id_1").style.display = "none";
    document.getElementById("Artical_div_id_1").style.display = "none";
    document.getElementById("Artical_div_id_2").style.display = "block";
    document.getElementById("Food_div_id_2").style.display = "none";
    document.getElementById("Food_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_3").style.display = "none";
    document.getElementById("Movies_div_id_3").style.display = "none";
    document.getElementById("Artical_div_id_3").style.display = "none";
    document.getElementById("Food_div_id_3").style.display = "none";
}

function Food_div() {
    document.getElementById("Music_div_id_1").style.display = "none";
    document.getElementById("Music_div_id_2").style.display = "none";
    document.getElementById("Movies_div_id_1").style.display = "none";
    document.getElementById("Movies_div_id_2").style.display = "none";
    document.getElementById("Artical_div_id_1").style.display = "none";
    document.getElementById("Artical_div_id_2").style.display = "none";
    document.getElementById("Food_div_id_1").style.display = "none";
    document.getElementById("Food_div_id_2").style.display = "block";
    document.getElementById("Music_div_id_3").style.display = "none";
    document.getElementById("Movies_div_id_3").style.display = "none";
    document.getElementById("Artical_div_id_3").style.display = "none";
    document.getElementById("Food_div_id_3").style.display = "none";
}

function clickOnSignUp(){
    document.getElementById("signup_id_div").style.display = "block";
    document.getElementById("body_id").style.opacity = "0.2";
    document.getElementById("body_id_2").style.opacity = "0.2";
}


function clickOnLogin(){
    document.getElementById("login_id_div").style.display = "block";
    document.getElementById("body_id").style.opacity = "0.2";
    document.getElementById("body_id_2").style.opacity = "0.2";
}

function closeLogin() {
    document.getElementById("login_id_div").style.display = "none";
    document.getElementById("body_id").style.opacity = "1";
    document.getElementById("body_id_2").style.opacity = "1";
}

function recoFun() {
    document.getElementById("reco").style.backgroundColor = "white";

}

function Music_div_3() {
    document.getElementById("Music_div_id_2").style.display = "none";
    document.getElementById("Music_div_id_3").style.display = "block";
}

function Movies_div_3() {
    document.getElementById("Movies_div_id_2").style.display = "none";
    document.getElementById("Movies_div_id_3").style.display = "block";
}

function Article_div_3() {
    document.getElementById("Artical_div_id_2").style.display = "none";
    document.getElementById("Artical_div_id_3").style.display = "block";
}

function Food_div_3() {
    document.getElementById("Food_div_id_2").style.display = "none";
    document.getElementById("Food_div_id_3").style.display = "block";
}

$(function () {
    function validateForm(){
        return false;
    }
});


function myFunction() {
    var pass1 = document.getElementById("pass1").value;
    var pass2 = document.getElementById("pass2").value;
    var ok = true;
    if (pass1 != pass2) {
        //alert("Passwords Do not match");
        document.getElementById("pass1").style.borderColor = "#E34234";
        document.getElementById("pass2").style.borderColor = "#E34234";
        ok = false;
    }
    else {
        alert("Passwords Match!!!");
    }
    return ok;
}
function closeSignup() {
    document.getElementById("signup_id_div").style.display = "none";
    document.getElementById("body_id").style.opacity = "1";
    document.getElementById("body_id_2").style.opacity = "1";
}


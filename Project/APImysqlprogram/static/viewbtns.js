

function viewMore(){
var div = document.getElementById("tasksList");
var two = document.getElementById("tableTwo");
var display = 1;
    
    if(display == 1)
    {
        div.style.display = 'block';
        two.style.display = 'none';
        display = 1;
    }
    else
    {
        div.style.display = 'none';
        two.style.display = 'block';
        display = 1;
    }
}



function viewLess(){
var div = document.getElementById("tasksList");
var two = document.getElementById("tableTwo");
var display = 1;
    
    if(display == 1)
    {
        div.style.display = 'none';
        two.style.display = 'block';
        display = 1;
    }
    else
    {
        div.style.display = 'block';
        two.style.display = 'none';
        display = 1;
    }
}



function filterTable(){
var div = document.getElementById("tasksList");
var filter = document.getElementById("tableFilter");
var two = document.getElementById("tableTwo");
var display = 1;
    
    if(display == 1)
    {
        div.style.display = 'none';
        two.style.display = 'none';
        filter.style.display = 'block';
        display = 1;
    }
    else
    {
        div.style.display = 'block';
        two.style.display = 'none';
        filter.style.display = 'none';
        display = 1;
    }
}



function closeFilter(){
var div = document.getElementById("tasksList");
var filter = document.getElementById("tableFilter");
var two = document.getElementById("tableTwo");
var display = 1;
    
    if(display == 1)
    {
        div.style.display = 'block';
        two.style.display = 'none';
        filter.style.display = 'none';
        display = 1;
    }
    else
    {
        div.style.display = 'none';
        two.style.display = 'none';
        filter.style.display = 'block';
        display = 1;
    }
}
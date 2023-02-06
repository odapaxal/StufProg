let firstclick = true;
function openSidebar(){
    if (firstclick){
        document.getElementsByClassName("sidebar").style.width = "25vw";
        document.getElementsByClassName("Topbar").style.marginRight = "25vw";
        firstclick=false;
    }
    else{
        document.getElementsByClassName("sidebar").style.width = "0vw";
        document.getElementsByClassName("header").style.marginLeft = "0vw";
        firstclick=true;
    } 
}
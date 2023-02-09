function ukedag(date){
    if (date.getDay()==0){
        return "Søndag "
    }else if (date.getDay()==1){
        return "Mandag "
    }else if (date.getDay()==2){
        return "Tirsdag "
    }else if (date.getDay()==3){
        return "Onsdag "
    }else if (date.getDay()==4){
        return "Torsdag "
    }else if (date.getDay()==5){
        return "Fredag "
    }else if (date.getDay()==6){
        return "Lørdag "
    }else return "Error"
}
let d = Date.now()
document.getElementById("hva").innerHTML = ukedag("July 21, 1983 01:15:00");

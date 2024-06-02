// шрифты

console.log("[INFO] connect JS");

function page2(){
    var heightWindow = document.documentElement.clientHeight;
    document.documentElement.scrollBy(0, heightWindow);
    console.log(heightWindow);
    console.log(window.scrollY); // узнаём текущую позицию экрана
}


// получаем текущую позицию и в зависимости от того, куда ближе,туда и крутим

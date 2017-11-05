class Sharpie {

    constructor(color, width) {
        this.color = color;
        this.width = width;
        this.ink = 100;
    }

    use() {
        this.ink -= this.width;
    }
}

var first_sharpie = new Sharpie("purple", 15);
var second_sharpie = new Sharpie("pink", 1);
first_sharpie.use();
first_sharpie.use();
console.log(first_sharpie.width);
console.log(first_sharpie.ink);

console.log(second_sharpie.ink);
while (second_sharpie.ink > 0) {
  second_sharpie.use();
  console.log(second_sharpie.ink);
}
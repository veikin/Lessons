1.2 function testComment(a, b) {     
    var x;
    x = a * b;
    
    return x;
}

1.3 function testA(a) {         

    var x="";

    x = a

    return x;
}

1.4 function testSum(a, b) {
    var x;
    x = a+b
    return x;
}

function testOperation(a, b) {
    var x;
    x=2*((a*b)%(a+b))
    return x;
}

1.5 function testIf(a, b) {
    var x;
    if (a>b){
    x = a+b
    } else {
    x = a*b
    }
    return x;
}

function testIf(a, b) {
    var x;
    if (a<b) {
    x = a+b
    } else if (a>b) {
    x = a-b
    } else {
    x = a*b
    }
    return x;
}

function testCase(a) {
    var x;
    switch (a) {
        case 0:
            x = "Ноль";
            break;
        case 1:
            x = "Один";
            break
        case 2:
            x = "Два";
            break;
        case 3:
            x = "Три";
            break;
        case 4:
            x = "Четыре";
            break;
        case 5:
            x = "Пять";
            break;
        case 6:
            x = "Шесть";
            break;
        case 7:
            x = "Семь";
            break
        case 8:
            x = "Восемь";
            break;
        case 9:
            x = "Девять";
            break;
        default:
            x = "Переменная a не равна 1, 2 или 3!";
    }
    return x;
}

1.6 function testFactorial(a) {
    var x=1;
    for (i=1; i<=a; i++) 
       x*=i
    return x;
}

function testWhile(a) {
    var x = 0;
    var i = 0;
    while (i <= a) {
        if (i % 2 == 0) {
            x += i;
        }
        i++;
    }
    return x;
}
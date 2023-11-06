from api.models import *
dataNumeros = [
    {
        'name': "Ensayo numeros",
        'type': "numeros",
        'questions': [
            {
                'question':
                "¿Cuál es el valor de: [(1 - \\frac{1}{2})(1 - \\frac{1}{3})(1 - \\frac{1}{4})(1 - \\frac{1}{5})]?",
                'subject': "numeros",
                'link_resolution': "https://youtube.com/embed/OxgnJ-IgxA0?start=124",
                'answer': [
                    {
                        'label': "[\\frac{1}{5}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{119}{120}]",
                        'right': 0,
                    },
                    {
                        'label': "[0]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{599}{120}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cual es el valor de: [1 - (\\frac{1}{2})^{-3}]?",
                'subject': "numeros",
                'link_resolution': "https://youtube.com/embed/OxgnJ-IgxA0?start=383",
                'answer': [
                    {
                        'label': "[-7]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{1}{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{9}{8}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{8}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "Un numero aumentado en su [30]% es igual a [910].",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=1682",
                'answer': [
                    {
                        'label': "[700]",
                        'right': 1,
                    },
                    {
                        'label': "[637]",
                        'right': 0,
                    },
                    {
                        'label': "[273]",
                        'right': 0,
                    },
                    {
                        'label': "[1.183]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cual es el resultado de: [\\sqrt{2}\\ - \\sqrt{8} + \\sqrt{18}] ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=1895",
                'answer': [
                    {
                        'label': "[2\\sqrt{2}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\sqrt{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\sqrt{12}]",
                        'right': 0,
                    },
                    {
                        'label': "[6\\sqrt{2}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Si [log_m\\lparen\\frac {8} {125}\\rparen = -3], ¿cual es el valor de m?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=2031",
                'answer': [
                    {
                        'label': "[\\frac {5} {2}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac {2} {5}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\lparen\\frac {8} {125}\\rparen^-3]",
                        'right': 0,
                    },
                    {
                        'label': "-[\\frac {2} {5}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cual de las siguientes cantidades corresponde al [5]% del precio de un articulo? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=1540",
                'answer': [
                    {
                        'label':
                        "El precio del articulo divido por [100], y luego multiplicado por [5]",
                        'right': 1,
                    },
                    {
                        'label': "Un quinto del precio del articulo.",
                        'right': 0,
                    },
                    {
                        'label': "El precio del articulo multiplicado por cinco decimos",
                        'right': 0,
                    },
                    {
                        'label':
                        "El precio del articulo divido por [5], y luego multiplicado por [100]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cual es el valor de [2,32 + 17,4]?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/nKR73i6zASg?start=38",
                'answer': [
                    {
                        'label': "[(232 + 1740):100]",
                        'right': 1,
                    },
                    {
                        'label': "[(232 + 174):10]",
                        'right': 0,
                    },
                    {
                        'label': "[(2320 + 174):100]",
                        'right': 0,
                    },
                    {
                        'label': "[(232 + 1740):1000]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cual de las siguientes expresiones representa el [22]%  del [15]% de P?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/nKR73i6zASg?start=577",
                'answer': [
                    {
                        'label': "[\\frac{33}{1000}P]",
                        'right': 1,
                    },
                    {
                        'label': "[3,3P]",
                        'right': 0,
                    },
                    {
                        'label': "[0,37P]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{33}{100}P]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cual de las siguientes opciones presenta una resolución correcta de [\\frac{27^\\frac{1}{3}}{8}\\cdot\\frac{16^\\frac{1}{2}}{9}]?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/nKR73i6zASg?start=755",
                'answer': [
                    {
                        'label':
                        "[\\frac{27^\\frac{1}{3}}{8}\\cdot\\frac{16^\\frac{1}{2}}{9} =\\frac{(27^3)^\\frac{1}{3}}{8}\\cdot\\frac{(4^2)\\frac{1}{2}}{9} = \\frac{3}{8}\\cdot\\frac{4}{9} = \\frac{12}{72} = \\frac{1}{6}]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[\\frac{27^\\frac{1}{3}}{8}\\cdot\\frac{16^\\frac{1}{2}}{9} = (\\frac{27}{8})^\\frac{1}{3}\\cdot(\\frac{16}{9})^\\frac{1}{2} = \\frac{3}{2}\\cdot\\frac{4}{3} = 2]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\frac{27^\\frac{1}{3}}{8}\\cdot\\frac{16^\\frac{1}{2}}{9} = (\\frac{27\\cdot16}{8\\cdot9})^{\\frac{1}{3}\\cdot\\frac{1}{2}} = 6^\\frac{1}{6}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\frac{27^\\frac{1}{3}}{8}\\cdot\\frac{16^\\frac{1}{2}}{9} = \\frac{27^\\frac{1}{3}\\cdot 16^\\frac{1}{2}}{8\cdot 9} = \\frac{9}{8}\cdot\\frac{8}{9} = 1]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cual es el valor de [\\sqrt{8}]([\\sqrt{18}]-[\\sqrt{8})]?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/nKR73i6zASg?start=1154",
                'answer': [
                    {
                        'label': "[4]",
                        'right': 1,
                    },
                    {
                        'label': "[8]",
                        'right': 0,
                    },
                    {
                        'label': "[\\sqrt{80}]",
                        'right': 0,
                    },
                    {
                        'label': "[80]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Por el arriendo de un juego inflable se cobra una cuota fija de $120.000 por cuatro horas, más $25.000 por cada hora adicional.[\\newline]¿Cuántas horas como máximo puede arrendar una empresa el juego inflable si tiene un presupuesto de $240.000 para este efecto?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=6",
                'answer': [
                    {
                        'label': "[8]",
                        'right': 1,
                    },
                    {
                        'label': "[4]",
                        'right': 0,
                    },
                    {
                        'label': "[9]",
                        'right': 0,
                    },
                    {
                        'label': "[10]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera el número [p] distinto de cero que es multiplicado dos veces por 1,25 y luego, dos veces por 0,75, tal como se representa a continuación:[\\newline p \\cdot 1,25 \\cdot 1,25 \\cdot 0,75 \\cdot 0,75 \\newline] ¿Qué pueden representar dichas multiplicaciones, respecto del número original [p] ?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=71",
                'answer': [
                    {
                        'label':
                        "Que hubo dos aumentos del 25 % y luego, dos disminuciones del 25 %",
                        'right': 1,
                    },
                    {
                        'label': "Que no hubo aumento de p ni disminución de p",
                        'right': 0,
                    },
                    {
                        'label':
                        "Que hubo dos aumentos de 0,25 y luego, dos disminuciones de 0,75",
                        'right': 0,
                    },
                    {
                        'label':
                        "Que hubo dos aumentos del 25 % y luego, dos disminuciones del 75 %",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "El modelo RVA de colores, permite crear cualquier color mediante la mezcla de los distintos tonos de tres olores: rojo, verde y azul. Los valores de la intensidad decada uno de estos colores van desde el 0 al 255 y cada color creado tiene un código de tres números donde el primero representa al rojo, el segundo al verde y el tercero al azul.[\\newline]El código de la mezcla de dos colores se obtiene haciendo el promedio de cada uno de los valores de los colores originales tal como se presenta a continuación:[\\newline \\begin{array}{c:c} \\text{Colores para mezclar} & \\text{Color resultante} \\newline \\hline (a,b,c),(m,n,t) & (\\frac{a + m}{2} \\cdot \\frac{b + n}{2} \\cdot \\frac{c + t}{2}) \\newline \\hline \\end{array} \\newline]¿Con qué color hay que mezclar el color (160, 60, 120) para obtener el color (170, 80, 60)?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=298",
                'answer': [
                    {
                        'label': "(180,100,0)",
                        'right': 1,
                    },
                    {
                        'label': "(180,100,60)",
                        'right': 0,
                    },
                    {
                        'label': "(10,20,60)",
                        'right': 0,
                    },
                    {
                        'label': "(165,70,90)",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En la temporada de invierno, la diferencia horaria entre Nueva Zelanda y Chile es de 16 h , desde Chile. Por ejemplo, si en Chile son las 11 de la mañana de un lunes, en Nueva Zelanda son las 3 de la mañana del martes.[\\newline]En la misma temporada la diferencia horaria entre México y Chile es de -1 h , desde Chile. Es decir, cuando en Chile son las 11 de la mañana de un lunes, en México son las 10 de la mañana del mismo día.[\\newline]¿Cuál es la diferencia horaria entre Nueva Zelanda y México, desde México, en la temporada de invierno?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=430",
                'answer': [
                    {
                        'label': "17",
                        'right': 1,
                    },
                    {
                        'label': "-17",
                        'right': 0,
                    },
                    {
                        'label': "-15",
                        'right': 0,
                    },
                    {
                        'label': "15",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Un comerciante compra una cantidad de naranjas a razón de 3 kilogramos por $600 y las vende todas a razón de 4 kilogramos por $1000.[\\newline]Si obtuvo una ganancia de $3000 , ¿cuántos kilogramos de naranjas compró?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=500",
                'answer': [
                    {
                        'label': "60",
                        'right': 1,
                    },
                    {
                        'label': "25",
                        'right': 0,
                    },
                    {
                        'label': "12",
                        'right': 0,
                    },
                    {
                        'label': "8",
                        'right': 0,
                    },
                ],
            },

            {
                'question': "¿Cuál es el [40]% del [15]% de 300 ?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=611",
                'answer': [
                    {
                        'label': "18",
                        'right': 1,
                    },
                    {
                        'label': "75",
                        'right': 0,
                    },
                    {
                        'label': "165",
                        'right': 0,
                    },
                    {
                        'label': "180",
                        'right': 0,
                    },
                ],
            },

            {
                'question':
                "Si el precio de un helado es $500 , ¿cuál de las siguientes expresiones representa el valor del helado aumentado en su [120]%?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=653",
                'answer': [
                    {
                        'label': "[2,2 \\cdot 500]",
                        'right': 1,
                    },
                    {
                        'label': "[1,2 \\cdot 500]",
                        'right': 0,
                    },
                    {
                        'label': "[50 + 20 \\cdot 500]",
                        'right': 0,
                    },
                    {
                        'label': "[50 + 120 \\cdot 500]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Qué porcentaje es 4740 de 15800 ?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/2nghljBMp1k?start=814",
                'answer': [
                    {
                        'label': "[30]%",
                        'right': 1,
                    },
                    {
                        'label': "[3,\\bar{3}]%",
                        'right': 0,
                    },
                    {
                        'label': "[3]%",
                        'right': 0,
                    },
                    {
                        'label': "[0,3]%",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cuál es el valor de [\\frac{\\left(0{,}002\\right) \\cdot \\left(0{,}02\\right)}{0{,}01}]?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=42",
                'answer': [
                    {
                        'label': "[0{,}04]",
                        'right': 0,
                    },
                    {
                        'label': "[0{,}004]",
                        'right': 1,
                    },
                    {
                        'label': "[0{,}0004]",
                        'right': 0,
                    },
                    {
                        'label': "[0{,}00004]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "¿Cuál es el valor de [1^2 + (-1 )^2 + (0,1)^2]?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=65",
                'answer': [
                    {
                        'label': "[0{,}01]",
                        'right': 0,
                    },
                    {
                        'label': "[0{,}2]",
                        'right': 0,
                    },
                    {
                        'label': "[2{,}01]",
                        'right': 1,
                    },
                    {
                        'label': "[2{,}1]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "Una aplicación de celular dispone al usuario una rutina de ejercicios distinta cada día. Esta aplicación es gratuita por un mes, pero luego se debe pagar una suscripción. Para esta aplicación existen dos formas de pago: [\\newline][\\rule{0pt}{0pt}] [\\newline][\\bullet] Suscripción mensual: $10 000 al inicio de cada mes [\\newline][\\bullet] Suscripción por 12 meses: $96000 [\\newline][\\rule{0pt}{0pt}] [\\newline]Si una persona escogió la suscripción mensual, ¿cuántos meses como máximo puede pagar para que esta sea económicamente más conveniente que la suscripción por 12 meses? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=121",
                'answer': [
                    {
                        'label': "9 meses",
                        'right': 1,
                    },
                    {
                        'label': "10 meses",
                        'right': 0,
                    },
                    {
                        'label': "11 meses",
                        'right': 0,
                    },
                    {
                        'label': "13 meses",
                        'right': 0,
                    },
                ],
            },
            {  # nuevas del 15_07
                'question': #6 FORMA 111 - 2024
                "En la tabla adjunta se presenta la cantidad de metros cuadrados recomendados para la crianza de cerdo de acuerdo con su masa. [\\newline] [\\rule{0pt}{0pt}] [\\newline] [\\begin{array}{|c|c|} \\hline \\text{Masa del cerdo} & \\text{Cantidad mínima de metros cuadrados por cerdo} \\\ \\hline \\text{Menos de 10 kg} & 0.15 \\\ \\text{Entre 10 kg y 20 kg} & 0.2 \\\ \\text{Entre 20 kg y 30 kg} & 0.3 \\\ \\text{Entre 30 kg y 50 kg} & 0.4 \\\ \\text{Entre 50 kg y 85 kg} & 0.55 \\\ \\text{Entre 85 kg y 110 kg} & 0.65 \\\ \\text{110 kg o más} & 1 \\\ \\hline \\end{array}] [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si se quiere hacer un chiquero para [12] cerdos del tipo Göttingen, que llegan a tener una masa de entre [35] kg y [45] kg en edad adulta, ¿cuál es la cantidad mínima de metros cuadrados que debe tener el chiquero para cumplir con la recomendación? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=130",
                'answer': [
                    {
                        'label': "[2{,}4]",
                        'right': 0,
                    },
                    {
                        'label': "[3{,}6]",
                        'right': 0,
                    },
                    {
                        'label': "[4{,}8]",
                        'right': 1,
                    },
                    {
                        'label': "[6{,}6]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': #1 FORMA 111 - 2024
                "Una persona selecciona un número de dos dígitos, luego resta este número a [200] y, finalmente, duplica el resultado. ¿Cuál es el mayor número que puede obtener mediante esta serie de operaciones?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=17",
                'answer': [
                    {
                        'label':
                        "[200]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[301]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[380]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[398]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': #4 FORMA 111 - 2024
                "Si la suma de [3] números enteros consecutivos es igual a [p], ¿cuál de las siguientes afirmaciones es siempre verdadera respecto al valor de [p]? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=80",
                'answer': [
                    {
                        'label':
                        "Es un número impar.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Es un múltiplo de [3].",
                        'right': 1,
                    },
                    {
                        'label':
                        "Es un número positivo.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Es un número distinto de cero.",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "La temperatura en una cámara de frigorífico es de [12^\\circ \\text{C}]. Se necesita variar esta temperatura hasta alcanzar los [36^\\circ \\text{C}]. [\\newline] [\\rule{0pt}{0pt}] [\\newline]Si la temperatura desciende [3^\\circ \\text{C}] cada cinco minutos, ¿cuánto tiempo se tardará en alcanzar dicha temperatura? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=177",
                'answer': [
                    {
                        'label':
                        "[85] minutos",
                        'right': 0,
                    },
                    {
                        'label':
                        "[80] minutos",
                        'right': 1,
                    },
                    {
                        'label':
                        "[60] minutos",
                        'right': 0,
                    },
                    {
                        'label':
                        "[48] minutos",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Una estudiante dedica en total 6h a estudiar los primeros cinco días de la semana  y las distribuye de la siguiente manera: [\\newline] [\\rule{0pt}{0pt}] [\\newline] [\\begin{array}{|c|c|c|c|c|} \\hline \\text{Lunes} & \\text{Martes} & \\text{Miércoles} & \\text{Jueves} & \\text{Viernes} \\\ \hline\\text{Matemática} & \\text{Física} & \\text{Lenguaje} & \\text{Física} & \\text{Historia} \\\ \\hline\\text{1 h} & \\text{1 h} & \\text{2 h} & \\text{1 h} & \\text{1 h} \\\ \\hline \\end{array}] [\\newline] [\\rule{0pt}{0pt}] [\\newline] El sábado estudiará 3h dividiendo ese tiempo en estudiar Matemática, Física y Lenguaje. Esa división del tiempo la hace de modo que sea proporcional a las horas de estudio de los días lunes, martes y miércoles. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuánto tiempo estudiará Matemática el día sábado?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=199",
                'answer': [
                    {
                        'label':
                        "[20] [\\text{min}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[30] [\\text{min}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[45] [\\text{min}]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[60] [\\text{min}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Una pelota se deja caer desde una altura de [100] [\\text{cm}]. Después de cada rebote la altura máxima alcanzada por la pelota es [\\dfrac{4}{5}] de la altura anterior. [\\newline][\\rule{0pt}{0pt}][\\newline] En el tercer rebote, ¿cuál es la altura máxima que alcanzará la pelota, aproximada al entero más cercano? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=249",
                'answer': [
                    {
                        'label':
                        "[51] [\\text{cm}]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[64] [\\text{cm}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[80] [\\text{cm}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[96] [\\text{cm}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cuál es el [1\\%] del [200\\% ] de [200] ?",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=298",
                'answer': [
                    {
                        'label':
                        "[0{,}4]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[4]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[40]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[400]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera los números enteros positivos menores o iguales que [50] .[\\newline]¿Cuál es el porcentaje de estos números que son múltiplos de [8]? ",
                'subject': "numeros",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=320",
                'answer': [
                    {
                        'label':
                        "[10\% ]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[12\% ]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[12{,}5\% ]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[16{,}5\% ]",
                        'right': 0,
                    },
                ],
            },
             {  #20 
                'question': #20 FORMA 111 - 2024
                "Camilo le propone a su mamá que cada día ella le deposite en una alcancía el doble de la cantidad depositada el día anterior. La mamá acepta la propuesta, pero solo hasta haberle depositado diez veces. Si la mamá comienza depositándole $[20], ¿cuánto le depositará al décimo día?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=678",
                'answer': [
                    {
                        'label':
                        "$[180]",
                        'right': 0,
                    },
                    {
                        'label':
                        "$[200]",
                        'right': 0,
                    },
                    {
                        'label':
                        "$[10240]",
                        'right': 1,
                    },
                    {
                        'label':
                        "$[20480]",
                        'right': 0,
                    },
                ],
            },




        ],
    },
]
dataAlgebra = [
    {
        'name': "Ensayo algebra",
        'type': "algebra",
        'questions': [
            {
                'question': "¿Cual es el valor de [x] en la ecuacion [0,3 + 10x = 0,5]?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=4092",
                'answer': [
                    {
                        'label': "[0,02]",
                        'right': 1,
                    },
                    {
                        'label': "[8]",
                        'right': 0,
                    },
                    {
                        'label': "[2]",
                        'right': 0,
                    },
                    {
                        'label': "[0,08]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Un bidon tiene ocupada con gasolina la mitad de su capacidad maxima. Al agregar 8L de gasolina se llega a las [\\frac{5}{6}] partes de su capacidad. ¿Cual es la capacidad maxima del bidon?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=4290",
                'answer': [
                    {
                        'label': "[24 L]",
                        'right': 1,
                    },
                    {
                        'label': "[10 L]",
                        'right': 0,
                    },
                    {
                        'label': "[12 L]",
                        'right': 0,
                    },
                    {
                        'label': "[20 L]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Si [log_2{(-2x + 3p)} = 3] y [log_3{(x +2p)} = 1] ¿Cual es el valor de (x - 2p)?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=5349",
                'answer': [
                    {
                        'label': "[-5]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{-13}{7}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{-27}{7}]",
                        'right': 0,
                    },
                    {
                        'label': "[3]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': "Si  [a \\cdot b = 10] y [a^2 + b^2 = 29]",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/jZGMcWoN-_M?start=582",
                'answer': [
                    {
                        'label': "[9]",
                        'right': 1,
                    },
                    {
                        'label': "[19]",
                        'right': 0,
                    },
                    {
                        'label': "[29]",
                        'right': 0,
                    },
                    {
                        'label': "[49]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Para que el doble de [(a + c)] sea igual a [18], le faltan [4] unidades, se expresa como:",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/jZGMcWoN-_M?start=1382",
                'answer': [
                    {
                        'label': "[2(a + c) + 4 = 18]",
                        'right': 1,
                    },
                    {
                        'label': "[2(a + c) - 4 = 18]",
                        'right': 0,
                    },
                    {
                        'label': "[2a + c + 4 = 18]",
                        'right': 0,
                    },
                    {
                        'label': "[4 - 2(a + c) = 18]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "La expresión [(a + 2)^{2} + (a + 1)(a - 3)] se factoriza como el producto de dos factores, tal que uno de ellos es [(a + 1)].[\\newline]¿Cuál de las siguientes expresiones corresponde al otro factor de la expresión?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/fhSir6Yd4pQ?start=196",
                'answer': [
                    {
                        'label': "[(2a - 2)]",
                        'right': 1,
                    },
                    {
                        'label': "[a^{2} - a - 2]",
                        'right': 0,
                    },
                    {
                        'label': "[a - 2]",
                        'right': 0,
                    },
                    {
                        'label': "[a^{2} + 3a - 2]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cuál de las siguientes expresiones es igual que [(a + (b + c)) \\cdot (a + (b - c))]?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/fhSir6Yd4pQ?start=1",
                'answer': [
                    {
                        'label': "[a^{2} + 2ab + b^{2} - c^{2}]",
                        'right': 1,
                    },
                    {
                        'label': "[a^{2} + b^{2} - c^{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[a^{2} + a^{2}b^{2} + b^{2} - c^{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[a^{2} + (b - c)^{2}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En una tienda de mascotas se dispone de un monto máximo de $50000 para pagar la electricidad que se onsume en un mes.[\\newline]La empresa eléctrica que suministra este servicio realiza el cobro, en pesos, mediante la función [c(x) = 100x + 5000] , siendo [x] la cantidad de kWh consumidos en el mes.[\\newline]¿Cuál de los siguientes conjuntos contiene a todos y únicamente los posiblesvalores del consumo en kWh en el mes que se puede solventar con el montodisponible en esa tienda?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/fhSir6Yd4pQ?start=525",
                'answer': [
                    {
                        'label': "[\\lbrack 0, 450\\rbrack]",
                        'right': 1,
                    },
                    {
                        'label': "[\\lbrack 0, 450\\lbrack]",
                        'right': 0,
                    },
                    {
                        'label': "[\\lbrack 0, 550\\lbrack]",
                        'right': 0,
                    },
                    {
                        'label': "[\\lbrack 0, 5500\\rbrack]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En una frutería cada durazno cuesta $480 y cada mango cuesta $400 . Una persona gastó $6800 en total comprando solo 16 frutas entre duraznos y mangos.[\\newline]¿Cuál de las siguientes ecuaciones permite determinar la cantidad [x] de duraznos que compró la persona?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/APzM_Ein_bE?start=2",
                'answer': [
                    {
                        'label': "[480x + 400(16 - x) = 6800]",
                        'right': 1,
                    },
                    {
                        'label': "[480x + 400(x - 16) = 6800]",
                        'right': 0,
                    },
                    {
                        'label': "[480x + 400x = 16]",
                        'right': 0,
                    },
                    {
                        'label': "[(480 + 400)x = 6800 + 16]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cuáles son las soluciones de la ecuación [x^{2} -12x +35 = 0] ?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/APzM_Ein_bE?start=197",
                'answer': [
                    {
                      'label': "[7] y [5]",
                      'right': 1,
                    },
                    {
                      'label': "[-7] y [-5]",
                      'right': 0,
                    },
                    {
                      'label': "[-14] y [-10]",
                      'right': 0,
                    },
                    {
                      'label': "[14] y [10]",
                      'right': 0,
                    },
                ],
            },
            {
                'question':
                "Ignacio se dedica a vender productos encargados por sus clientes, que importa mediante una aplicación móvil. El precio de venta al que Ignacio vende los productos lo determina según la función [P(x) = 1,5x + 2500] , tal que [x] representa el precio, en pesos, al que compra el producto en la aplicación.[\\newline]¿Cuál de las siguientes afirmaciones es verdadera?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/APzM_Ein_bE?start=496",
                'answer': [
                    {
                        'label':
                        "Ignacio realiza un recargo de un [50]% del precio del producto importado sin considerar ese recargo en el cargo fijo.",
                        'right': 1,
                    },
                    {
                        'label':
                        "Ignacio cobra un costo fijo de $[(1,5 + 2500)] a todos los productos que vende.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Ignacio cobra un costo fijo de $[(1,5 \\cdot 2500)] a todos los productos que vende.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Ignacio realiza un recargo de [1,5]% del precio del producto importado sin considerar el cargo fijo.",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En una distribuidora envasaron 360 L de detergente líquido en bidones de 3 L y de 5 L de capacidad.[\\newline]Si se ocuparon en total 100 bidones, ¿cuál de los siguientes valores es la diferencia entre la cantidad de bidones de distinta capacidad que se usaron?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/APzM_Ein_bE?start=550",
                'answer': [
                    {
                        'label': "[40]",
                        'right': 1,
                    },
                    {
                        'label': "[25]",
                        'right': 0,
                    },
                    {
                        'label': "[48]",
                        'right': 0,
                    },
                    {
                        'label': "[50]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera la ecuación [3x - p = 2x + p + 1].[\\newline]¿Cuál es el menor valor que puede tomar x para que p sea un número entero positivo?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=762",
                'answer': [
                    {
                        'label': "[3]",
                        'right': 1,
                    },
                    {
                        'label': "[0]",
                        'right': 0,
                    },
                    {
                        'label': "[1]",
                        'right': 0,
                    },
                    {
                        'label': "[2]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera el sistema [\\begin{rcases} ax + by + 1 = 0 \\newline bx + ay + 1 = 0 \\end{rcases}]., en x e y , con a y b números reales distintos entre sí, distintos de cero y [a \\mathrlap{/}{=} -b].[\\newline]¿Cuál es la solución del sistema?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=1083",
                'answer': [
                    {
                        'label': "[x = \\frac{-1}{a + b}; y = \\frac{-1}{a + b}]",
                        'right': 1,
                    },
                    {
                        'label': "[x = \\frac{1}{a + b}; y = \\frac{1}{a + b}]",
                        'right': 0,
                    },
                    {
                        'label': "[x = \\frac{-1}{a - b}; y = \\frac{-1}{a - b}]",
                        'right': 0,
                    },
                    {
                        'label': "[x = \\frac{-1}{a + b}; y = \\frac{1}{a + b}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera la ecuación [(x -3)(x - 4) = 2].[\\newline]¿Cuál de los siguientes argumentos es válido?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=1227",
                'answer': [
                    {
                        'label':
                        "Las soluciones de la ecuación son [x = 2] y [x = 5] , porque [(2 - 3)(2 - 4) = 2] y [(5 - 3)(5 - 4) = 2].",
                        'right': 1,
                    },
                    {
                        'label':
                        "La ecuación posee dos soluciones, porque [x = 3] y [x = 4] satisfacen la igualdad.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Las soluciones de la ecuación son ambas positivas, porque el discriminante asociado a la ecuación es positivo.",
                        'right': 0,
                    },
                    {
                        'label':
                        "Las soluciones son [x = 2] y [x = 5] , porque ambos valores satisfacen la ecuación [x^{2} -7x +12 = 0].",
                        'right': 0,
                    },
                ],
            },
            {  # 16
                'question':
                "Una empresa vende crema para las manos en envases con forma de cilindros rectos de 20 cm de altura y de distintos diámetros.[\\newline] Por una promoción se decide aumentar en su [20]% la capacidad de cada envase, manteniendo la altura de los envases cilíndricos. [\\newline]¿Cuál de las siguientes funciones permite determinar el volumen de los nuevos envases, en [cm^{3}] , con r el radio del envase sin promoción, en cm?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/GFcXxDORRvo?start=162",
                'answer': [
                    {
                        'label':
                        "g(r) = [24 \\cdot r^{2} \\cdot \\pi]",
                        'right': 1,
                    },
                    {
                        'label':
                        "p(r) = [16 \\cdot r^{2} \\cdot \\pi]",
                        'right': 0,
                    },
                    {
                        'label':
                        "f(r) = [28,8 \\cdot r^{2} \\cdot \\pi]",
                        'right': 0,
                    },
                    {
                        'label':
                        "h(r) = [24 \\cdot r^{2} \\cdot \\pi]",
                        'right': 0,
                    },
                ],
            },
            {  # 17
                'question':
                "Para cierta actividad se aconseja beber diariamente al menos 1 L de agua por cada 35 kg de masa corporal.[\\newline] Para una persona de masa corporal P kg que tiene una botella de forma cilíndrica de diámetro 6 cm y altura 20 cm, ¿cuál de las siguientes expresiones permite determinar la cantidad de veces, en un día, que debe consumir el contenido de la botella llena de agua, para cumplir lo que se aconseja?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/GFcXxDORRvo?start=285",
                'answer': [
                    {
                        'label':
                        "[\\frac{\\frac{P}{35} \\cdot 1000}{\\pi \\cdot 9 \\cdot 20}]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[\\frac{P}{\\pi \\cdot 36 \\cdot 20}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\frac{P}{\\pi \\cdot 9 \\cdot 20}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\frac{P}{35 \\pi \\cdot 9 \\cdot 20}]",
                        'right': 0,
                    },
                ],
            },
            {  # 18
                'question':
                "Dos ciclistas viajan en sentidos opuestos en una misma carretera y en línea recta, uno al encuentro del otro. Se encuentran separados inicialmente por una distancia d , y la rapidez a la que se desplazan son v y w . ¿Cuál de las siguientes funciones permite calcular la distancia a la que están los dos ciclistas, antes de encontrarse, en función del tiempo t ?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=1168",
                'answer': [
                    {
                        'label':
                        "m(t) = d - (v + w)t",
                        'right': 1,
                    },
                    {
                        'label':
                        "f(t) = (v -w)t - d",
                        'right': 0,
                    },
                    {
                        'label':
                        "p(t) = d - (v - w)t",
                        'right': 0,
                    },
                    {
                        'label':
                        "n(t) = (v -w)t - d",
                        'right': 0,
                    },
                ],
            },
            #FORMA 111 - 2024 
            { 
                'question': #27 FORMA 111 - 2024 
                "Considera el siguiente gráfico en el que se presenta un modelo para la relación entre la cantidad de kilogramos de lentejas que se venden a granel en un almacén y su monto total a pagar. https://res.cloudinary.com/dohtxxlbe/image/upload/v1689830182/ImagenesPrePAES/27_111_2024_fwcbqb.png ¿Cuántos kilogramos de lentejas compró en total una persona que pagó $3300?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=924",
                'answer': [
                    {
                        'label':
                        "2 kg",
                        'right': 0,
                    },
                    {
                        'label':
                        "2,2 kg",
                        'right': 1,
                    },
                    {
                        'label':
                        "2,3 kg",
                        'right': 0,
                    },
                    {
                        'label':
                        "2,5 kg",
                        'right': 0,
                    },
                ],
            },
           
            {  # 19-07 #21
                'question': #21 FORMA 111 - 2024  
                "El tiempo máximo en microsegundos que tarda un programa de computador en ordenar alfabéticamente una lista con [n] nombres se puede modelar mediante la expresión [0,001 * n * \\sqrt{n}] . Si una lista tiene [10000] nombres, ¿cuántos microsegundos tardará como máximo el programa en ordenar alfabéticamente los nombres de esta lista? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=729",
                'answer': [
                    {
                        'label':
                        "[10]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[1000]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[10000]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[50000]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #22
                'question': #22 FORMA 111 - 2024 
                "Una persona diseña un programa computacional que crea una copia de todos los archivos del computador cada una hora.[\\newline] [\\rule{0pt}{0pt}] [\\newline] La persona ejecuta el programa en su computador y al cabo de [m] horas este posee un total de [k * 2^{m}] archivos, con [m] y [k] números enteros positivos. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si la persona durante ese tiempo no elimina ni adiciona archivos, ¿cuál de las siguientes afirmaciones es siempre verdadera?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=750",
                'answer': [
                    {
                        'label':
                        "[k]  es el tiempo que el programa tarda en llenar totalmente el disco duro del computador.",
                        'right': 0,
                    },
                    {
                        'label':
                        "[2^m]  representa la cantidad de veces que el programa copia todos los archivos. ",
                        'right': 0,
                    },
                    {
                        'label':
                        "[k * 2^{m-1}]  representa el total de archivos nuevos que se crearon con el programa",
                        'right': 0,
                    },
                    {
                        'label':
                        "[k]  corresponde a la cantidad inicial de archivos que posee el computador antes de ejecutar el programa.",
                        'right': 1,
                    },
                ],
            },
            {  # 19-07 #23
                'question': #23 FORMA 111 - 2024 
                "Una persona compró cierta cantidad de un mismo artículo con $[350000] , sin ningún tipo de descuento y no le sobró dinero. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si cada artículo tiene precio $[A] , ¿cuántos artículos compró?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=810",
                'answer': [
                    {
                        'label':
                        "[\\dfrac{350000}{A}]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[350000 * A]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[350000 - A]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\dfrac{A}{350000}]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #24
                'question': #24 FORMA 111 - 2024 
                "¿Cuál de las siguientes expresiones representa la tercera parte del sucesor de [p]? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=826",
                'answer': [
                    {
                        'label':
                        "[\\dfrac{p}{3}+1]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[3(p+1)]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[p + \\dfrac{1}{3}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\dfrac{p+1}{3}]",
                        'right': 1,
                    },
                ],
            },
            {  # 19-07 #25
                'question': #25 FORMA 111 - 2024 
                "Para envasar cierta cantidad de agua mineral se necesitan [80] contenedores de [200] litros de capacidad cada uno. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuántos contenedores de [50] litros de capacidad se necesitarán para envasar la misma cantidad de agua? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=843",
                'answer': [
                    {
                        'label':
                        "[20]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[125]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[320]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[12000]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #26
                'question': #26 FORMA 111 - 2024  
                "Una persona gastó $[(a+1600)] en ocho días. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si todos los días gastó lo mismo, ¿cuál de las siguientes expresiones representa lo que gastó la persona en dos días? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=879",
                'answer': [
                    {
                        'label':
                        "$[(\\dfrac{1}{4}a+400)]",
                        'right': 1,
                    },
                    {
                        'label':
                        "$[(\\dfrac{1}{4}a+1600)]",
                        'right': 0,
                    },
                    {
                        'label':
                        "$[(2a+400)]",
                        'right': 0,
                    },
                    {
                        'label':
                        "$[(2a+200)]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #28
                'question': #28 FORMA 111 - 2024 
                "Bajo ciertas condiciones, la cantidad de kilómetros recorridos por un automóvil es directamente proporcional a la cantidad de litros de combustible que consume. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si un automóvil que cumple estas condiciones recorre [90] kilómetros con [15] litros de bencina, ¿cuántos kilómetros puede recorrer este automóvil con [25] litros de bencina?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=985",
                'answer': [
                    {
                        'label':
                        "[54]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[60]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[135]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[150]",
                        'right': 1,
                    },
                ],
            },
            {  # 19-07 #29
                'question': #29 FORMA 111 - 2024 
                "En una carrera se reparte un total de [12000] dólares a las primeras cuatro personas que lleguen a la meta. Este reparto se realiza a razón de [6 : 3 : 2 : 1] de modo que mientras mejor haya sido la posición de llegada, más dinero se gana. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál es la cantidad que le corresponde a la persona que llegó en segundo lugar?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1036",
                'answer': [
                    {
                        'label':
                        "[2000] dólares ",
                        'right': 0,
                    },
                    {
                        'label':
                        "[3000] dólares ",
                        'right': 1,
                    },
                    {
                        'label':
                        "[4000] dólares ",
                        'right': 0,
                    },
                    {
                        'label':
                        "[6000] dólares ",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #30
                'question': #30 FORMA 111 - 2024  
                "¿Cuál es la solución de la ecuación [\\dfrac{2}{3}+x=\\dfrac{3}{2}]?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1093",
                'answer': [
                    {
                        'label':
                        "[0]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\dfrac{1}{6}]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[-1]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\dfrac{5}{6}]",
                        'right': 1,
                    },
                ],
            },
            {  # 19-07 #31
                'question': #31 FORMA 111 - 2024  
                "Al finalizar un trayecto, la cantidad [L] de litros de combustible que quedan en el estanque de cierto vehículo, está dada por la expresión:[\\newline] [\\rule{0pt}{0pt}] [\\newline] [L=c-0,1*x] [\\newline] [\\rule{0pt}{0pt}] [\\newline] En la que [c] es la cantidad de litros que tenía el estanque de este vehículo al iniciar el trayecto, [x] es la cantidad de kilómetros que recorrió el vehículo y [0,1] es una constante medida en litros por kilómetro. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Este vehículo, al iniciar el trayecto tenía en el estanque [50] litros y al finalizarlo tenía [30] litros. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuántos kilómetros recorrió el vehículo en ese trayecto?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1107",
                'answer': [
                    {
                        'label':
                        "[800]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[250]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[200]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[2]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #32
                'question': #32 FORMA 111 - 2024 
                "Una torta está formada por capas alternadas de bizcocho y de manjar, de modo que la capa inferior y la capa superior tienen que ser de bizcocho. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si cada capa de bizcocho tiene una masa de [100 g] y cada capa de manjar tiene una masa de [150 g] , ¿cuántas capas de manjar, como máximo, puede tener una torta para que esta no supere los [700 g] de masa?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1154",
                'answer': [
                    {
                        'label':
                        "[1]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[2]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[4]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[5]",
                        'right': 0,
                    },
                ],
            },
            {  # 19-07 #33
                'question': #33 FORMA 111 - 2024 
                "Al organizar un seminario, una persona recibe dos ofertas de dos centros de eventos. El primero, cobra $[2000] por invitado, más un cargo fijo de $[520000]. El segundo, cobra $[5000] por invitado, más un cargo fijo de $[310000]. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuántos invitados como mínimo deberían asistir al evento, para que el segundo centro de eventos sea más caro?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1208",
                'answer': [
                    {
                        'label':
                        "[70]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[71]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[118]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[119]",
                        'right': 0,
                    },
                ],
            },
            {  # 10-08 #34
                'question': #34 FORMA 111 - 2024 
                "Se hace una colecta para recaudar fondos, logrando recaudar $[30000] con [150] monedas de dos valores distintos. [\\newline] [\\rule{0pt}{0pt}] [\\newline] El siguiente sistema de ecuaciones es un modelo para determinar la cantidad de monedas de cada tipo: [\\newline] [\\rule{0pt}{0pt}] [\\newline] [\\begin{cases} x + y = 150 \\\ 500x - 50y = 30000 \\end{cases}] [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál de las siguientes afirmaciones es verdadera?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1302",
                'answer': [
                    {
                        'label':
                        "[x] e [y]  corresponden a la cantidad de monedas de $[500]  y de $[50] , respectivamente ",
                        'right': 1,
                    },
                    {
                        'label':
                        "Hay exactamente [500]  monedas del tipo [x] y [50]  monedas del tipo [y]",
                        'right': 0,
                    },
                    {
                        'label':
                        "Al considerar una moneda de cada tipo el valor total es $[150]",
                        'right': 0,
                    },
                    {
                        'label':
                        "Considerando solo las monedas de $[500]  se juntan $[5000]",
                        'right': 0,
                    },
                ],
            },
            {  # 10-08 #35
                'question': #35 FORMA 111 - 2024 
                "En una tienda de ropa se necesita incorporar las ventas por Internet con reparto a domicilio para aumentar sus ventas. Para el reparto se necesita contratar los servicios de una empresa de vehículos de transporte y la tienda recibe dos cotizaciones: [\\newline] [\\rule{0pt}{0pt}] [\\newline] [\\bullet] Cobro empresa A en un mes: [C_t ={\\dfrac {c} {d}} * t + 4000 ] [\\newline] [\\bullet] Cobro empresa B en un mes: [C_t =2000 * t ] [\\newline] [\\rule{0pt}{0pt}] [\\newline] con t el tiempo de uso del servicio, en horas, y C(t) el costo del servicio, en pesos. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuánto tiempo se debe usar el servicio en cada empresa para que el costo sea el mismo? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1338",
                'answer': [
                    {
                        'label':
                        "[1,2] horas",
                        'right': 0,
                    },
                    {
                        'label':
                        "[2] horas",
                        'right': 0,
                    },
                    {
                        'label':
                        "[6] horas",
                        'right': 1,
                    },
                    {
                        'label':
                        "[12] horas",
                        'right': 0,
                    },
                ],
            },

            {  # 10-08 #36
                'question': #36 FORMA 111 - 2024 
                "El índice de Masa Corporal (IMC) de una persona se relaciona con su masa, medida en kilogramos, y su estatura, medida en metros, a través de la expresión: [\\newline] [\\rule{0pt}{0pt}] [\\newline] [masa = estatura^2 * IMC] [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si una persona tiene una masa de [54 kg] y tiene un [IMC = 24], ¿cuál es su estatura según este modelo?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1384",
                'answer': [
                    {
                        'label':
                        "[1,05] m",
                        'right': 0,
                    },
                    {
                        'label':
                        "[1,125] m",
                        'right': 0,
                    },
                    {
                        'label':
                        "[1,5] m",
                        'right': 1,
                    },
                    {
                        'label':
                        "[2,25] m",
                        'right': 0,
                    },
                ],
            },
            {  # 10-08 #37
                'question': #37 FORMA 111 - 2024 
                "Una empresa ha desarrollado la fórmula [U(x) = - {\\dfrac {1} {2}} (x - 12)^2 + 100000] que le permite conocer la utilidad que tendrá, en pesos, al vender [x] unidades de un artículo. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuántos artículos se deben vender para que la utilidad de la empresa sea de $1000000?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1421",
                'answer': [
                    {
                        'label':
                        "[6]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[12]",
                        'right': 1,
                    },
                    {
                        'label':
                        "[13]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[14]",
                        'right': 0,
                    },
                ],
            },
            {  # 10-08 #38
                'question': #38 FORMA 111 - 2024 
                "En el siguiente gráfico se representa la rapidez de un automóvil a control remoto a medida que transcurre el tiempo. [\\newline] [\\rule{0pt}{0pt}] [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1692020636/ImagenesPrePAES/38_111_2024_y8ru2c.png [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál de las siguientes afirmaciones se puede deducir del gráfico? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1452",
                'answer': [
                    {
                        'label':
                        "Entre los [3] s y [7] s  el automóvil está detenido",
                        'right': 0,
                    },
                    {
                        'label':
                        "El automóvil cambia de dirección cuatro veces",
                        'right': 0,
                    },
                    {
                        'label':
                        "La distancia total recorrida por el automóvil es [20] km",
                        'right': 0,
                    },
                    {
                        'label':
                        "Entre los [8] s y [10] s  el automóvil disminuye su rapidez",
                        'right': 1,
                    },
                ],
            },
            {  # 10-08 #39
                'question': #39 FORMA 111 - 2024 
                "La relación entre el puntaje que una persona obtiene en cierta prueba y su notaestá dada por la siguiente expresión: NOTA = [{\\dfrac {puntaje} {14}} + 2] [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál de las siguientes afirmaciones es verdadera respecto a esta prueba?",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1497",
                'answer': [
                    {
                        'label':
                        "Para una nota [3,5] se necesita obtener un puntaje de [35] puntos",
                        'right': 0,
                    },
                    {
                        'label':
                        "Con [50] puntos se obtiene una nota superior a [6]",
                        'right': 0,
                    },
                    {
                        'label':
                        "Cuando el puntaje aumenta en un punto, la nota aumenta en [2]",
                        'right': 0,
                    },
                    {
                        'label':
                        "La mínima nota que se puede obtener en la prueba es un [2]",
                        'right': 1,
                    },
                ],
            },
            {  # 10-08 #40
                'question': #40 FORMA 111 - 2024 
                "En un computador se simula el lanzamiento de un objeto desde una altura de [8 cm]. La altura, en [cm], que alcanza dicho objeto se modela por la función [f] definida por [f(t) = -t^2 + 2t + 8], tal que [t] representa el tiempo transcurrido desde el lanzamiento, en [s] [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿A qué altura se encontraría el objeto a los [3 s] de ser lanzado? ",
                'subject': "algebra",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1554",
                'answer': [
                    {
                        'label':
                        "[5] cm",
                        'right': 1,
                    },
                    {
                        'label':
                        "[8] cm",
                        'right': 0,
                    },
                    {
                        'label':
                        "[13] cm",
                        'right': 0,
                    },
                    {
                        'label':
                        "[23] cm",
                        'right': 0,
                    },
                ],
            },
        ],
    },

]
dataProbabilidades = [
    {
        'name': "Ensayo probabilidades",
        'type': "probabilidades",
        'questions': [
            {
                'question':
                "El dinero total que tienen ahorrado tres amigas es  $[210.000]. Se sabe que Claudia aporto el doble que Maria y que Yasna aporto el doble que Claudia. ¿Cual es el promedio de dinero aportado por Claudia y Yasna?",
                'subject': "probabilidades",
                'link_resolution':
                "https://www.youtube.com/embed/OxgnJ-IgxA0?start=13136",
                'answer': [
                    {
                        'label': "$[90.000]",
                        'right': 1,
                    },
                    {
                        'label': "$[70.000]",
                        'right': 0,
                    },
                    {
                        'label': "$[45.000]",
                        'right': 0,
                    },
                    {
                        'label': "$[35.000]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En la siguiente tabla se muestra la distribucion de las edades, en años, de un grupo de niños.  [\\newline \\begin{array}{c:c} \\text{Edad} & \\text{Frecuencia} \\newline \\hline 2 & 5 \\newline \\hdashline 3 & 6 \\newline \\hdashline 4 & 9 \\newline \\hdashline 5 & 3 \\newline \\hline \\end{array} \\newline] ¿Cual es la mediana de edad de este grupo de niños?",
                'subject': "probabilidades",
                'link_resolution':
                "https://www.youtube.com/embed/OxgnJ-IgxA0?start=13314",
                'answer': [
                    {
                        'label': "[4 años]",
                        'right': 1,
                    },
                    {
                        'label': "[3,5 años]",
                        'right': 0,
                    },
                    {
                        'label': "[7,5 años]",
                        'right': 0,
                    },
                    {
                        'label': "[9 años]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Al lanzar un dado cargado, numerado del [1] al [6], la probabilidad de que salga un numero par es el doble de la probabilidad de que salga un numero impar. Si se lanza este dado, ¿cual es la probabilidad de que salga un numero impar?",
                'subject': "probabilidades",
                'link_resolution':
                "https://www.youtube.com/embed/OxgnJ-IgxA0?start=14765",
                'answer': [
                    {
                        'label': "[\\frac{1}{3}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{1}{9}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{2}{3}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{2}{9}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "En un mazo de cartas de naipes ingles [52] cartas, [13] de ellas son de trébol. Si se extraen del mazo dos cartas al azar, una después de la otra y sin reposición, ¿cual es la probabilidad de que ambas sean de trébol?",
                'subject': "probabilidades",
                'link_resolution':
                "https://www.youtube.com/embed/OxgnJ-IgxA0?start=14941",
                'answer': [
                    {
                        'label': "[\\frac{13}{52}\\cdot\\frac{12}{51}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{13}{52}\\cdot\\frac{12}{52}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{13}{52}]+[\\frac{12}{52}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{13}{52}] +[\\frac{12}{51}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "A un grupo de personas se le consultó acerca de la cantidad de películas vistas el último mes. En la tabla adjunta se presenta la distribución de los resultados de dicha consulta.[\\newline \\begin{array}{c:c} \\text{Cantidad de películas vistas el último mes} & \\text{Frecuencia} \\newline \\hline 1 & h \\newline \\hdashline 2 & 200 \\newline \\hdashline 3 & t \\newline \\hdashline 4 & 50 \\newline \\hline \\end{array} \\newline]Si se agregan personas al grupo de tal manera que la frecuencia de todos los datos aumenta en un [20]%, ¿cuál de las siguientes expresiones representa la cantidad total de personas que hay finalmente en el grupo?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/Kdr9QVeILdI?start=358",
                'answer': [
                    {
                        'label': "[300 + 1,2h + 1,2t]",
                        'right': 1,
                    },
                    {
                        'label': "[1,2h + 1,2t]",
                        'right': 0,
                    },
                    {
                        'label': "[300]",
                        'right': 0,
                    },
                    {
                        'label': "[12]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Los resultados de las dos primeras pruebas de matemática de Esteban son un 5,3 y un 5,9.[\\newline]¿Cuál de las siguientes notas es la mínima que debe obtener Esteban en la tercera prueba para que su promedio sea de al menos un 5,9 en las tres pruebas?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/Kdr9QVeILdI?start=570",
                'answer': [
                    {
                        'label': "[6,5]",
                        'right': 1,
                    },
                    {
                        'label': "[6,2]",
                        'right': 0,
                    },
                    {
                        'label': "[6,1]",
                        'right': 0,
                    },
                    {
                        'label': "[5,9]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Se consultó a un grupo de 50 personas acerca de su sabor favorito de cierto tipo de helado. En la tabla adjunta se registran los resultados obtenidos.[\\newline \\begin{array}{c:c} \\text{Sabor} & \\text{Frecuencia} \\newline \\hline Vainilla & 9 \\newline \\hdashline Chocolate & 15 \\newline \\hdashline Frutilla & 6 \\newline \\hdashline Manjar & 20 \\newline \\hline \\end{array} \\newline]Si se elige a una de estas personas al azar, ¿cuál es la probabilidad de que su sabor favorito sea de vainilla o de frutilla?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/4-FdwiMge7Y?start=226",
                'answer': [
                    {
                        'label': "[\\frac{3}{10}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{9}{50} \\cdot \\frac{6}{50}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{54}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{15}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Una caja contiene seis tarjetas todas del mismo tipo y en cada una de ellas hay una palabra escrita. Las palabras escritas en cuatro de las tar jetas son: CLASE, SOL, TEMPRANO y LEON.[\\newline]Se sabe que al extraer al azar una tarjeta de la caja la probabilidad de que la palabra escrita en ella tenga menos de tres letras vocales es [\\frac{2}{3}].[\\newline]¿Cuáles de las siguientes palabras podrían estar escritas en las otras dos tarjetas?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/4-FdwiMge7Y?start=275",
                'answer': [
                    {
                        'label': "CUADRILATERO y CANTO",
                        'right': 1,
                    },
                    {
                        'label': "VASO y RED",
                        'right': 0,
                    },
                    {
                        'label': "CINCO y SEIS",
                        'right': 0,
                    },
                    {
                        'label': "PARALELOGRAMO y GIGANTESCO",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Si se lanzan tres monedas, ¿cuál es la probabilidad de obtener al menos un sello?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/4-FdwiMge7Y?start=355",
                'answer': [
                    {
                        'label': "[\\frac{7}{8}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{1}{3}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{8}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{2}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Una caja M contiene solo 3 bolitas rojas y 2 verdes, todas del mismo tipo y una caja N contiene solo una bolita roja y 3 bolitas verdes, todas del mismo tipo.[\\newline]Un experimento aleatorio consiste en lanzar un dado común, si sale un número par se extrae una bolita desde la caja M, en caso contrario se extrae una bolita de la caja N.[\\newline]Si se realiza este experimento, ¿cuál es la probabilidad de extraer una bolita roja?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2875",
                'answer': [
                    {
                        'label': "[\\frac{17}{40}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{17}{20}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{8}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{4}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considera las tiendas A , B y C dedicadas a la venta de relojes. Si un cliente compra un reloj en una de estas tres tiendas, la probabilidad de que compre en A es 0,2 ; en B es 0,3 y en C es 0,5. Se sabe que la probabilidad de que cualquier reloj que se venda en las tiendas A, B y C tenga fallas es 0,3; 0,5 y 0,6 , respectivamente.[\\newline]Si Teresa compra un reloj que no tiene fallas, ¿cuál es la probabilidad de que lo haya comprado en la tienda A?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2931",
                'answer': [
                    {
                        'label':
                        "[\\frac{0,2 \\cdot 0,7}{0,2 \\cdot 0,7 + 0,3 \\cdot 0,5 + 0,5 \\cdot 0,4}]",
                        'right': 1,
                    },
                    {
                        'label': "[0,2 \\cdot 0,7]",
                        'right': 0,
                    },
                    {
                        'label': "[0,2 \\cdot 0,3]",
                        'right': 0,
                    },
                    {
                        'label':
                        "[\\frac{0,2 \\cdot 0,3}{0,2 \\cdot 0,3 + 0,3 \\cdot 0,5 + 0,5 \\cdot 0,6}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Cada uno de los estudiantes de los terceros medios de un colegio lleva una botella individual para hidratarse, ya sea de agua o jugo.[\\newline]Al seleccionar un estudiante de tercero medio de este colegio al azar, se puede determinar la probabilidad de que sea una mujer que lleva agua, si se sabe que:[\\newline](1) el [60]% de los estudiantes son hombres y de estos [\\frac{5}{6}] llevan agua.[\\newline](2) los [\\frac{2}{3}] de las mujeres llevan jugo.",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=3221",
                'answer': [
                    {
                        'label': "Ambas juntas, (1) y (2)",
                        'right': 1,
                    },
                    {
                        'label': "(1) por sí sola",
                        'right': 0,
                    },
                    {
                        'label': "(2) por sí sola",
                        'right': 0,
                    },
                    {
                        'label': "Se requiere información adicional",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "De un grupo de 100 personas, 40 de ellas son fumadores. Un [20]%  de los fumadores no presenta una enfermedad respiratoria. Al seleccionar una persona al azar del grupo total, la probabilidad de que presente una enfermedad respiratoria es 0,35.[\\newline]Al seleccionar una persona al azar del grupo total, ¿cuál es la probabilidad de que no fume dado que no tiene una enfermedad respiratoria?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=3006",
                'answer': [
                    {
                        'label': "[\\frac{57}{65}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{45}{60}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{57}{60}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{45}{65}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "De un grupo de 100 personas, 40 de ellas son fumadores. Un [20]%  de los fumadores no presenta una enfermedad respiratoria. Al seleccionar una persona al azar del grupo total, la probabilidad de que presente una enfermedad respiratoria es 0,35.[\\newline]Al seleccionar una persona al azar del grupo total, ¿cuál es la probabilidad de que no fume dado que no tiene una enfermedad respiratoria?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=3006",
                'answer': [
                    {
                        'label': "[\\frac{57}{65}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{45}{60}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{57}{60}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{45}{65}]",
                        'right': 0,
                    },
                ],
            },
            {  # 15
                'question':
                "Sean A y B  dos sucesos tales que P(A) = [\\frac{1}{2}, P(A \\cap B) = \\frac{1}{6} y 1 - P(B) = \\frac{2}{3}]. Entonces, P(A [\\cup] B) =",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/jeAxuYbpmZ4?start=137",
                'answer': [
                    {
                        'label': "[\\frac{2}{3}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{4}{9}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{2}{9}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{5}{12}]",
                        'right': 0,
                    },
                ],
            },
            {  # 16
                'question':
                "En un curso, todos los alumnos participan de por lo menos una actividad deportiva, que puede ser futbol, atletismo o ambas. En el grupo de fútbol hay 32 alumnos del curso y en el grupo de atletismo hay 24 alumnos del curso, de los cuales la mitad pertenece además al grupo de fútbol. Al escoger un alumno al azar, ¿cuál es la probabilidad de que petenezca solamente al grupo de fútbol?  ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/jeAxuYbpmZ4?start=732",
                'answer': [
                    {
                        'label': "[\\frac{5}{11}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{5}{10}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{4}{7}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{3}{5}]",
                        'right': 0,
                    },
                ],
            },
            {  # 17
                'question':
                "En un cajon hay 12 pañuelos azules y una cierta cantidad de pañuelos blancos, todos de idéntica forma y sin la presencia de pañuelos de otros colores. Si la probabilidad de sacar al azar un pañuelo blanco es de [\\frac{3}{5}], ¿cuántos pañuelos hay en total en el cajón?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/jeAxuYbpmZ4?start=1412",
                'answer': [
                    {
                        'label': "[30]",
                        'right': 1,
                    },
                    {
                        'label': "[18]",
                        'right': 0,
                    },
                    {
                        'label': "[20]",
                        'right': 0,
                    },
                    {
                        'label': "[24]",
                        'right': 0,
                    },
                ],
            },
            {  # 18
                'question':
                "Si se lanza dos veces un dado común y se suman los resultados, la probabilidad de que dicha suma sea multiplo de 5 es",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/jeAxuYbpmZ4?start=2437",
                'answer': [
                    {
                        'label': "[\\frac{7}{35}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{2}{9}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{1}{108}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{7}{12}]",
                        'right': 0,
                    },
                ],
            },
            #FORMA 111 - 2024 
            {  # 11-08-2023 #51
                'question': #51 FORMA 111 - 2024 
                "En un juego se sacan tarjetas al azar de un mazo que incluyen dos movimientos que debe realizar una ficha en un tablero cuadriculado. En la figura adjunta se presenta un ejemplo de un movimiento realizado con una de las tarjetas. [\\newline] [\\rule{0pt}{0pt}] [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1692021745/ImagenesPrePAES/51_111_2024_nmwdzd.png [\\newline] [\\rule{0pt}{0pt}] [\\newline]  La ficha de un jugador se encuentra en la casilla inicial que se encuentra en el centro del tablero y se mueve según la siguiente secuencia de tarjetas: [\\newline] [\\rule{0pt}{0pt}] [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1692021793/ImagenesPrePAES/51_111_2024_hinhw5.png [\\newline] [\\rule{0pt}{0pt}] [\\newline] Al sacar otra tarjeta, y realizar el movimiento correspondiente, la ficha del jugador vuelve a la casilla inicial. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál fue la cuarta tarjeta que sacó?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2131",
                'answer': [
                    {
                        'label': "[\\begin{bmatrix}    5 Norte \\\    2 Este \\end{bmatrix}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\begin{bmatrix}    5 Sur \\\    2 Oeste \\end{bmatrix}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\begin{bmatrix}    2 Norte \\\    2 Este \\end{bmatrix}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\begin{bmatrix}    2 Sur \\\    2 Oeste \\end{bmatrix}]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #52 FORMA 111 - 2024 
                "Ingrid representa las medidas de su casa en un plano a una escala en [1 : 100]. [\\newline] [\\rule{0pt}{0pt}] [\\newline]  ¿Cuál de las siguientes fórmulas permitió a Ingrid llevar las medidas de su casa a las medidas en el plano?. ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2185",
                'answer': [
                    {
                        'label': "Medidas en el plano = [\\dfrac{100}{\\text{medida en la realidad}}] ",
                        'right': 0,
                    },
                    {
                        'label': "Medidas en el plano = [(\\text{medida en la realidad}) * 100] ",
                        'right': 0,
                    },
                    {
                        'label': "Medidas en el plano = [\\dfrac{\\text{medida en la realidad}}{100^2}] ",
                        'right': 0,
                    },
                    {
                        'label': "Medidas en el plano = [\\dfrac{\\text{medida en la realidad}}{100}] ",
                        'right': 1,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #53 FORMA 111 - 2024 
                "En un taller de instrumentos se construirá una guitarra utilizando un plano que está en escala [1 : 8] . En el plano, el largo del mástil de la guitarra es de [95] mm. [\\newline] [\\rule{0pt}{0pt}] [\\newline]¿Cuál debe ser el largo del mástil de la guitarra que se construirá?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2215",
                'answer': [
                    {
                        'label': "[103] cm",
                        'right': 0,
                    },
                    {
                        'label': "[85,5] cm",
                        'right': 0,
                    },
                    {
                        'label': "[76] cm",
                        'right': 1,
                    },
                    {
                        'label': "[8,55] cm",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #54 FORMA 111 - 2024 
                "Un edificio vertical al suelo da una sombra de [12] metros, mientras que a la misma hora un árbol, que está en una posición vertical al suelo, y cuya altura es de [4] metros proyecta una sombra de [3] metros. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál de las siguientes igualdades permite determinar la altura [x], en metros, del edificio?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2264",
                'answer': [
                    {
                        'label': "[\\dfrac{3}{4} = \\dfrac{12}{x}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\dfrac{3}{4} = \\dfrac{x}{12}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\dfrac{3}{4} = \\dfrac{9}{x}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\dfrac{3}{4} = \\dfrac{x}{9}]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #55 FORMA 111 - 2024
                "Un carpintero construye una estantería triangular con repisas paralelas entre sí y de diferentes longitudes, tal como se representa en la figura adjunta. [\\newline] [\\rule{0pt}{0pt}] [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583914/ImagenesPrePAES/55_111_2024_chuabc.png [\\newline] [\\rule{0pt}{0pt}] [\\newline]¿Cuál es la medida [x] en la repisa de la estantería que el carpintero debe construir?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2281",
                'answer': [
                    {
                        'label': "[14] cm",
                        'right': 0,
                    },
                    {
                        'label': "[16] cm",
                        'right': 0,
                    },
                    {
                        'label': "[21] cm",
                        'right': 1,
                    },
                    {
                        'label': "[56] cm",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #56 FORMA 111 - 2024 
                "En el taller de literatura de un colegio, se les preguntó a los [25] estudiantes cuántos días tardaron en leer un libro. En base a las respuestas de los estudiantes se armó la siguiente tabla que está incompleta: [\\newline] [\\rule{0pt}{0pt}] [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583901/ImagenesPrePAES/56_111_2024_lgkbzi.png [\\newline] [\\rule{0pt}{0pt}] [\\newline]  ¿Cuántos estudiantes se demoraron tres días en leer el libro? ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2334",
                'answer': [
                    {
                        'label': "[5]",
                        'right': 0,
                    },
                    {
                        'label': "[7]",
                        'right': 1,
                    },
                    {
                        'label': "[8]",
                        'right': 0,
                    },
                    {
                        'label': "[10]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #57 FORMA 111 - 2024 
                "En la siguiente tabla se presenta la cantidad de hijos que tienen las familias que viven en un edificio: [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583898/ImagenesPrePAES/57_111_2024_zf2pdp.png  [\\newline] ¿Cuántas familias viven en total en ese edificio?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2386",
                'answer': [
                    {
                        'label': "[5]",
                        'right': 0,
                    },
                    {
                        'label': "[10]",
                        'right': 0,
                    },
                    {
                        'label': "[15]",
                        'right': 1,
                    },
                    {
                        'label': "[20]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #58 FORMA 111 - 2024 
                "Las calificaciones obtenidas por cinco estudiantes en una evaluación de matemática están registradas en la siguiente tabla: [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583895/ImagenesPrePAES/58_111_2024_khel01.png  [\\newline] El profesor ajusta las calificaciones obtenidas por cada estudiante de modo que la calificación máxima sea [6,0], para ello utilizará la relación [N] = [\\dfrac{6}{5}p], tal que [N] es la nueva calificación y [p] es la calificación actual obtenida por cada estudiante en la tabla. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál es el nuevo promedio de las calificaciones de estos estudiantes?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2404",
                'answer': [
                    {
                        'label': "[6,0]",
                        'right': 0,
                    },
                    {
                        'label': "[4,8]",
                        'right': 1,
                    },
                    {
                        'label': "[4,0]",
                        'right': 0,
                    },
                    {
                        'label': "[2,0]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #59 FORMA 111 - 2024 
                "En el gráfico adjunto se representan los resultados de una encuesta aplicada a los [50] estudiantes de dos cuartos medios de un colegio. Dicha encuesta tenía relación con la creación de un taller literario. [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583891/ImagenesPrePAES/59_111_2024_z5284o.png [\\newline] Si cada estudiante marcó una sola opción en la encuesta, ¿cuál de las siguientes afirmaciones es verdadera?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2444",
                'answer': [
                    {
                        'label': "Más de la cuarta parte de los estudiantes están “totalmente en desacuerdo” con la creación del taller",
                        'right': 1,
                    },
                    {
                        'label': "Más de la mitad de los estudiantes respondieron “en desacuerdo” en la encuesta",
                        'right': 0,
                    },
                    {
                        'label': "Las tres quintas partes de los estudiantes están “totalmente en desacuerdo” con la creación del taller",
                        'right': 0,
                    },
                    {
                        'label': "La octava parte de los estudiantes respondieron “ni de acuerdo ni en desacuerdo” con la creación del taller",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #60 FORMA 111 - 2024 
                "Un grupo de adolescentes se inscribió para recibir un regalo de Navidad. La entidad encargada de comprar los regalos necesita saber la cantidad de adolescentes que hay por cada una de las edades para hacerles regalos distintos por edad. Para ello, les preguntan qué edad tienen, registrando la siguiente lista:? [\\newline] [\\rule{0pt}{0pt}] [\\newline]  15, 15, 14, 14, 15, 15, 15, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 12, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14 y 12 [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Para qué adolescentes se debe comprar una mayor cantidad de regalos? ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2474",
                'answer': [
                    {
                        'label': "Para adolescentes de [12] años",
                        'right': 0,
                    },
                    {
                        'label': "Para adolescentes de [13] años",
                        'right': 0,
                    },
                    {
                        'label': "Para adolescentes de [14] años",
                        'right': 1,
                    },
                    {
                        'label': "Para adolescentes de [15] años",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #62 FORMA 111 - 2024 
                "Durante el año 2023 una fundación focalizará su ayuda al [25] % de los hogares con menores ingresos de una comuna. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál de las siguientes medidas de posición permite determinar el ingreso máximo que debe tener un hogar de la comuna para ser beneficiado?  ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2509",
                'answer': [
                    {
                        'label': "El segundo cuartil de los ingresos",
                        'right': 0,
                    },
                    {
                        'label': "El percentil [75] de los ingresos",
                        'right': 0,
                    },
                    {
                        'label': "El percentil [4] de los ingresos",
                        'right': 0,
                    },
                    {
                        'label': "El primer cuartil de los ingresos",
                        'right': 1,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #63 FORMA 111 - 2024 
                "En el curso de Francisca se vende una rifa para financiar la gira de estudios en la que el premio es una bicicleta. Francisca quiere ganar la bicicleta y solo pudo comprar [8] números de la lista que ella vendió.  [\\newline] [\\rule{0pt}{0pt}] [\\newline] Si se vendieron [100] listas completas y cada una con [20] números, ¿cuál es la probabilidad que tiene Francisca de ganarse la bicicleta si solo compró de una lista?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2527",
                'answer': [
                    {
                        'label': "[\\dfrac{8}{120}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\dfrac{8}{800}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\dfrac{8}{20}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\dfrac{8}{2000}]",
                        'right': 1,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #64 FORMA 111 - 2024 
                "Se realizó una encuesta sobre las preferencias de un grupo de personas respecto a su pasatiempo favorito, tal que cada persona eligió solo un pasatiempo. En esta encuesta [30] personas indicaron que su pasatiempo favorito es leer, [48] personas indicaron que es hacer deporte y [n] personas indicaron que es ver películas. [\\newline] [\\rule{0pt}{0pt}] [\\newline] Al elegir una persona al azar de este grupo, la probabilidad de que su pasatiempo favorito no sea hacer deporte es [0,6]. [\\newline] [\\rule{0pt}{0pt}] [\\newline] ¿Cuál es la cantidad de personas que indicaron ver películas?",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2547",
                'answer': [
                    {
                        'label': "[22]",
                        'right': 0,
                    },
                    {
                        'label': "[42]",
                        'right': 1,
                    },
                    {
                        'label': "[52]",
                        'right': 0,
                    },
                    {
                        'label': "[117]",
                        'right': 0,
                    },
                ],
            },
            {  # 11-08-2023
                'question': #65 111 2024
                "Un grupo de estudiantes quiere calcular la probabilidad de que al lanzar tres monedas resulten las tres caras o las tres sellos, realizando el siguiente procedimiento en el cual cometen un error. [\\newline] https://res.cloudinary.com/dohtxxlbe/image/upload/v1692022644/ImagenesPrePAES/65_111_2024_krjjvp.png [\\newline] ¿En cuál de los pasos se cometió el error? ",
                'subject': "probabilidades",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2607",
                'answer': [
                    {
                        'label': "En el Paso [1]",
                        'right': 1,
                    },
                    {
                        'label': "En el Paso [2]",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso [3]",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso [4]",
                        'right': 0,
                    },
                ],
            },
        ],
    },
]
dataGeometria = [
    {
        'name': "Ensayo geometria",
        'type': "geometria",
        'questions': [
            {
                'question':
                "Sean [A(1,1)], [B(5,3)] y [C] los vertices de un triangulo. Se pueden determinar las coordenadas del vertice [C] del triangulo si se sabe que:  [(1)] Angulo [BAC = 90°] [(2)] El triangulo es isosceles y el vertice [C] esta en el cuarto cuadrante.",
                'subject': "geometria",
                'link_resolution':
                "https://www.youtube.com/embed/OxgnJ-IgxA0?start=12325",
                'answer': [
                    {
                        'label': "Ambas juntas, [(1)] y [(2)]",
                        'right': 1,
                    },
                    {
                        'label': "[(2)] por si sola",
                        'right': 0,
                    },
                    {
                        'label': "[(1)] por si sola",
                        'right': 0,
                    },
                    {
                        'label': "Se requiere informacion adicional",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Considere los vectores [\\overrightarrow{u}] = [(-2,5)], [\\overrightarrow{v}] = [(3, -2)] y [\\overrightarrow{c}] = [(-1,-4)]. ¿Cual es el vector [\\overrightarrow{u}] + 2[\\overrightarrow{v}] - [\\overrightarrow{c}]?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=9560",
                'answer': [
                    {
                        'label': "[(5,5)]",
                        'right': 1,
                    },
                    {
                        'label': "[(3,5)]",
                        'right': 0,
                    },
                    {
                        'label': "[(4,9)]",
                        'right': 0,
                    },
                    {
                        'label': "[(2,1)]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Si el punto (a,b) es la imagen que se obtiene al trasladar el punto R segun el vector (m,n), ¿cuales son las coordenadas de R?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/OxgnJ-IgxA0?start=9691",
                'answer': [
                    {
                        'label': "[(a - m, b - n)]",
                        'right': 1,
                    },
                    {
                        'label': "[(am, bn)]",
                        'right': 0,
                    },
                    {
                        'label': "[(m - a, n - b)]",
                        'right': 0,
                    },
                    {
                        'label': "[(a + m, b + n)]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Con un cordel de largo d se forma un cuadrado. ¿Cuanto mide el area del un cuadrado?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/m4qRM2mtjHA?start=480",
                'answer': [
                    {
                        'label': "[\\frac{d^2}{16}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{d^2}{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{d^2}{4}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{d^2}{8}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Dos figuras geométricas son homotéticas con razón de homotecia -3.[\\newline]Si la figura original tiene un área de [b cm^{2} ], ¿cuál es el área de la imagen homotética?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2263",
                'answer': [
                    {
                        'label': "[9b cm^{2}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{b}{3} cm^{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[9b^{2} cm^{2}]",
                        'right': 0,
                    },
                    {
                        'label': "[3b cm^{2}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Para qué puntos (x, y) en el plano cartesiano se cumple [\\frac{3x + y}{3} = x + y]?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2348",
                'answer': [
                    {
                        'label': "Para los puntos de la forma (x, 0)",
                        'right': 1,
                    },
                    {
                        'label': "Para los puntos de la forma (x, y)",
                        'right': 0,
                    },
                    {
                        'label': "Solo para el punto (0, 0)",
                        'right': 0,
                    },
                    {
                        'label': "Para ningún punto",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "¿Cuántos vectores (a, b) con coordenadas enteras y magnitud [\\sqrt{5}] hay en el plano cartesiano?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2414",
                'answer': [
                    {
                        'label': "[8]",
                        'right': 1,
                    },
                    {
                        'label': "[2]",
                        'right': 0,
                    },
                    {
                        'label': "[4]",
                        'right': 0,
                    },
                    {
                        'label': "Infinitos",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Al trasladar el punto (x, y) según el vector (p, q) , se obtiene un punto en el segundo cuadrante.[\\newline]¿Cuál de las siguientes relaciones es verdadera?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=2382",
                'answer': [
                    {
                        'label': "[x] < [-p] e [y] > [-q]",
                        'right': 1,
                    },
                    {
                        'label': "[x] > [-p] e [y] < [-q]",
                        'right': 0,
                    },
                    {
                        'label': "[x] < [p] e [y] > [q]",
                        'right': 0,
                    },
                    {
                        'label': "[x] < [-p] e [y] < [-q]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "Se necesita determinar el perímetro del rectángulo ABCD, cuyo largo y ancho miden (4x por 1) cm y (x por 2) cm, respectivamente. Se sabe que ABCD es semejante a un rectángulo cuyo largo y ancho miden 10 cm y 8cm, respectivamente.[\\newline]Para determinar el perímetro del rectángulo ABCD se realiza el siguiente procedimiento, cometiéndose un error: [\\newline] Paso 1: como los rectángulos son semejantes se plantea la expresión: [\\frac{4x +\\ 1}{8} = \\frac{x + 2}{10}\\newline] Paso 2: se resuelve la expresión anterior, obteniéndose [x = \\frac{3}{16} \\newline]Paso 3: se reemplaza este valor de x en (4x + 1) cm y (x + 2) cm, obteniéndose que el largo y el ancho del rectángulo son [\\frac{7}{4}]cm y [\\frac{35}{16}]cm, respectivamente.[\\newline]Paso 4: se calcula el perímetro del rectángulo obteniéndose [\\frac{63}{8}]cm.[\\newline]¿En cuál de los pasos se cometió el error?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=1758",
                'answer': [
                    {
                        'label': "En el Paso 1",
                        'right': 1,
                    },
                    {
                        'label': "En el Paso 2",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso 3",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso 4",
                        'right': 0,
                    },
                ],
            },
            {
                'question':
                "La razón de semejanza entre las figuras P y Q, en ese orden, es [\\frac{3}{5}], mientras que la razón de semejanza entre las figuras R y P , en ese orden, es [\\frac{7}{3} \\newline]¿Cuál es la razón de semejanza entre las figuras R y Q, en ese orden?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/3-qEJz0wATs?start=1813",
                'answer': [
                    {
                        'label': "[\\frac{7}{5}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\frac{44}{15}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{35}{9}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\frac{26}{15}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': 
                "A un punto P del plano cartesiano se le aplica una reflexión respecto al origen de este obteniéndose el punto Q, luego el punto Q se traslada según el vector [\\overrightarrow{v} = (-2, 3)] obteniéndose el punto R.[\\newline] Si R tiene coordenadas [(5, 4)] , ¿cuáles son las coordenadas del punto P ?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/GFcXxDORRvo?start=560",
                'answer': [
                    {
                        'label': "[(-7,-1)]",
                        'right': 1,
                    },
                    {
                        'label': "[(3,7)]",
                        'right': 0,
                    },
                    {
                        'label': "[(7,-1)]",
                        'right': 0,
                    },
                    {
                        'label': "[(-3,-7)]",
                        'right': 0,
                    },
                ],
            },
            #FORMA 111 - 2024 
            {
                'question': #41 FORMA 111 - 2024 
                "Una persona necesita medir la altura de un árbol, para lo cual usa un medidor de distancia láser de la siguiente manera: [\\newline][\\rule{0pt}{0pt}] [\\newline][\\bullet] primero, se aleja del árbol [12\\text{ m}] en un tramo de camino recto y perfectamente horizontal. [\\newline][\\bullet] segundo, utiliza el medidor de distancia láser a ras del suelo apuntando al extremo superior del árbol el cual registra una distancia de [15\\text{ m}] .[\\newline][\\rule{0pt}{0pt}] [\\newline]En la figura adjunta se representa la situación anterior. https://res.cloudinary.com/dohtxxlbe/image/upload/v1690572243/ImagenesPrePAES/41_111_2024_koijbx.png",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1592",
                'answer': [
                    {
                        'label': "[9\\text{ m}]",
                        'right': 1,
                    },
                    {
                        'label': "[13{,}5\\text{ m}]",
                        'right': 0,
                    },
                    {
                        'label': "[15\\text{ m}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\sqrt{369}\\text{ m}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question': #42 FORMA 111 - 2024 
                "La medida [d] del diámetro de un círculo inscrito en un triángulo rectángulo se puede determinar con la fórmula de Poncelet: https://res.cloudinary.com/dohtxxlbe/image/upload/v1690574315/ImagenesPrePAES/42_111_2024_g1jupb.png en la cual [a] y [b] son las medidas de los catetos del triángulo  y [c] es la medida de la hipotenusa. [\\newline][\\rule{0pt}{0pt}] [\\newline] Si las medidas de los catetos de un triángulo rectángulo son [8 \\text{ cm}] y [6 \\text{ cm}], ¿cuál es el perímetro del círculo inscrito en él?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1614",
                'answer': [
                    {
                        'label': "[\\pi\\text{ cm}]",
                        'right': 0,
                    },
                    {
                        'label': "[2\\pi\\text{ cm}]",
                        'right': 0,
                    },
                    {
                        'label': "[4\\pi\\text{ cm}]",
                        'right': 1,
                    },
                    {
                        'label': "[8\\pi\\text{ cm}]",
                        'right': 0,
                    },
                ],
            },
            
            {
                'question':#43 FORMA 111 - 2024 
                "Una fábrica de espejos recibe un pedido para elaborar varios tamaños de espejos, con la particularidad de que todos deben ser cuadrados y que en las esquinas se sobrepongan triángulos rectángulos de madera iguales entre sí, como el que se representa en la figura adjunta. https://res.cloudinary.com/dohtxxlbe/image/upload/v1690576134/ImagenesPrePAES/43_111_2024_x5hnhp.png Considera [m] y [n] como las distintas medidas que pueden tener los catetos de los triángulos de madera y [p] como las distintas medidas que puede tener el lado del espejo. [\\newline][\\rule{0pt}{0pt}] [\\newline]Si todas las medidas están en cm, ¿cuál de las siguientes fórmulas permite determinar el área [(S)] que ocupa el vidrio que se ve en cada espejo, en [{cm}^2] ?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1674",
                'answer': [
                    {
                        'label': "[S = {p}^2 + 4 \\cdot m \\cdot n]",
                        'right': 0,
                    },
                    {
                        'label': "[S = {p}^2 - 4 \\cdot m \\cdot n]",
                        'right': 0,
                    },
                    {
                        'label': "[S = {p}^2 + 2 \\cdot m \\cdot n]",
                        'right': 0,
                    },
                    {
                        'label': "[S = {p}^2 - 2 \\cdot m \\cdot n]",
                        'right': 1,
                    },
                ],
            },
            {
                'question':#44 FORMA 111 - 2024 
                "Se tiene un paralelepípedo recto de base cuadrada de lado [5] [cm] y altura [8] [cm]. [\\newline] Si se aumentan al doble las medidas de sus aristas, ¿cuál es el volumen del nuevo prisma?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1708",
                'answer': [
                    {
                        'label': "[400\\text{ cm}^3]",
                        'right': 0,
                    },
                    {
                        'label': "[800\\text{ cm}^3]",
                        'right': 0,
                    },
                    {
                        'label': "[1600\\text{ cm}^3]",
                        'right': 1,
                    },
                    {
                        'label': "[40\\text{ }000\\text{ cm}^3]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#45 FORMA 111 - 2024 
                "En la siguiente imagen se presenta un diseño de un módulo formado por bloques de vidrio y un bloque de cemento. Los módulos se utilizan para hacer una pared decorativa. https://res.cloudinary.com/dohtxxlbe/image/upload/v1690577006/ImagenesPrePAES/45_111_2024_xjso52.png Cada bloque de vidrio tiene una cara con forma cuadrada con lado de [20\\text{ cm}]. La durabilidad de este módulo depende de su densidad y, para obtenerla, se requiere conocer el volumen del bloque de vidrio que tiene. [\\newline][\\rule{0pt}{0pt}] [\\newline] ¿Cuál es el volumen de los bloques de vidrio en cada módulo?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1766",
                'answer': [
                    {
                        'label': "[38\\text{ }400\\text{ cm}^3]",
                        'right': 0,
                    },
                    {
                        'label': "[35\\text{ }200\\text{ cm}^3]",
                        'right': 0,
                    },
                    {
                        'label': "[32\\text{ }000\\text{ cm}^3]",
                        'right': 1,
                    },
                    {
                        'label': "[12\\text{ }800\\text{ cm}^3]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#46 FORMA 111 - 2024 
                "El volumen de una esfera y de un cono están dados por las expresiones [\\dfrac{4\\pi R^3}{3}] y [\\dfrac{\\pi r^3 h}{3}], respectivamente, con [R] el radio de la esfera, [r] el radio basal del cono y [h] la altura del cono. [\\newline][\\rule{0pt}{0pt}] [\\newline] Si se designa por [\\text{M}] al volumen de la esfera, ¿cuál de las siguientes expresiones representa al volumen de un cono cuya altura y radio basal tienen la misma medida que el radio de la esfera?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1790",
                'answer': [
                    {
                        'label': "[\\dfrac{\\text{M}}{4}]",
                        'right': 1,
                    },
                    {
                        'label': "[\\dfrac{\\text{3M}}{4}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\text{M}]",
                        'right': 0,
                    },
                    {
                        'label': "[\\text{4M}]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#47 FORMA 111 - 2024 
                "El punto [(2, -3)] es un vértice común de cuatro cuadrados cuyos lados miden 2 unidades y son paralelos a los ejes coordenados del plano cartesiano. [\\newline  \\text{} \\newline] ¿Cuál de las siguientes coordenadas podría corresponder a un vértice de alguno de los cuadrados?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=1844",
                'answer': [
                    {
                        'label': "[(2,-2)]",
                        'right': 0,
                    },
                    {
                        'label': "[(4,-5)]",
                        'right': 1,
                    },
                    {
                        'label': "[(-1,-3)]",
                        'right': 0,
                    },
                    {
                        'label': "[(2,1)]",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#48 FORMA 111 - 2024 
                "Una figura se mueve con las siguientes transformaciones isométricas desde su posición inicial hasta su posición final como se presenta en la figura adjunta. [\\newline \\text{} \\newline] 1) La figura en la posición inicial se rota en [90^\\circ] en sentido horario con centro de rotación el centro de la figura. [\\newline] 2) Luego, se traslada [2] metros hacia el sur y [6] metros al este. [\\newline] 3) Por último, se vuelve a rotar en [90^\\circ] en sentido horario con centro de rotación el centro de la figura, resultando la figura en la posición final. https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583925/ImagenesPrePAES/48_111_2024_duvbi6.png ¿Cuál de las siguientes secuencias de transformaciones isométricas permite volver a dejar la figura en la posición inicial?",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2007",
                'answer': [
                    {
                        'label': "Rotar en [180^\\circ] en sentido horario con centro de rotación el centro de la figura y luego trasladar 2 metros al norte y 6 metros al oeste.",
                        'right': 1,
                    },
                    {
                        'label': "Rotar en [180^\\circ]  en sentido horario con centro de rotación el centro de la figura y luego trasladar 2  metros al sur y 6  metros al este. ",
                        'right': 0,
                    },
                    {
                        'label': "Rotar en [90^\\circ]  en sentido antihorario con centro de rotación el centro de la figura y luego trasladar 2  metros al sur y 6  metros al este. ",
                        'right': 0,
                    },
                    {
                        'label': "Rotar en [90^\\circ]en sentido antihorario con centro de rotación el centro de la figura y trasladar 2  metros al norte y 6  metros al oeste. ",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#49 FORMA 111 - 2024 
                "Se quiere obtener el punto [(12, 1)] a partir del punto [(-3, 5)] mediante cuatro transformaciones isométricas. Para esto se efectuaron los siguientes pasos, cometiendo un error en uno de ellos. [\\newline\\text{}\\newline][\\textbf{Paso 1: }]al punto [(-3, 5)] se le aplica una reflexión con respecto al eje [Y] , obteniendo el punto [(3, 5)].[\\newline][\\textbf{Paso 2: }]al punto [(3, 5)] se le aplica una traslación según el vector [(-2, 7)], obteniendo el punto [(1, 12)].[\\newline][\\textbf{Paso 3: }]al punto [(1, 12)] se le aplica una rotación en [90^\\circ] en sentido antihorario con centro en el origen, obteniendo el punto [(12, -1)].[\\newline][\\textbf{Paso 4: }]al punto [(12, -1)] se le aplica una reflexión con respecto al eje [X] , obteniendo el punto [(12, 1)]. [\\newline\\text{}\\newline]¿En cuál de los pasos se cometió el error? ",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2046",
                'answer': [
                    {
                        'label': "En el Paso 1 ",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso 2 ",
                        'right': 0,
                    },
                    {
                        'label': "En el Paso 3 ",
                        'right': 1,
                    },
                    {
                        'label': "En el Paso 4",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#50 FORMA 111 - 2024 
                "La siguiente imagen corresponde a un aparato que se usa para copiar dibujos, pues refleja el dibujo original de modo que el usuario logra realizar el dibujo en otro papel, de manera invertida.https://res.cloudinary.com/dohtxxlbe/image/upload/v1690583918/ImagenesPrePAES/50_111_2024_mw3clv.png ¿Cuál de las siguientes letras se lee igual al ser copiada en papel con este aparato si se coloca al lado izquierdo del papel? ",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2110",
                'answer': [
                    {
                        'label': "S",
                        'right': 0,
                    },
                    {
                        'label': "M",
                        'right': 1,
                    },
                    {
                        'label': "b",
                        'right': 0,
                    },
                    {
                        'label': "Q",
                        'right': 0,
                    },
                ],
            },
            {
                'question':#53 FORMA 111 - 2024 
                "En un taller de instrumentos se construirá una guitarra utilizando un plano que está en escala 1 : 8 . En el plano, el largo del mástil de la guitarra es de 95 mm . [\\newline\\text{}\\newline] ¿Cuál debe ser el largo del mástil de la guitarra que se construirá? ",
                'subject': "geometria",
                'link_resolution': "https://www.youtube.com/embed/6ojXnscOIT4?start=2215",
                'answer': [
                    {
                        'label': "103 cm",
                        'right': 0,
                    },
                    {
                        'label': "85,5, cm",
                        'right': 0,
                    },
                    {
                        'label': "76 cm",
                        'right': 1,
                    },
                    {
                        'label': "8,55 cm",
                        'right': 0,
                    },
                ],
            },
            
          
        ],
    },
]


def poblarBd(data):
    for essay_data in data:
        print('------------------------------------------------------------------')
        print(essay_data)
        print('------------------------------------------------------------------')
        question = essay_data.pop('questions')
        essay_object = MathType.objects.create(**essay_data)
        print(essay_object)
        print('------------------------------------------------------------------')
        for question_data in question:
            print(question_data)
            print('------------------------------------------------------------------')
            answers = question_data.pop('answer')
            question_object = Question.objects.create(**question_data, type_question=essay_object)
            print(question_object)
            print('------------------------------------------------------------------')
            for answer_data in answers:
                Answer.objects.create(**answer_data, questions=question_object)
                print(answer_data)
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')
                print('------------------------------------------------------------------')

def poblarDbLogros():
    logros_data = [{
    "name": "Iniciando el Viaje PrePAES",
    "description": "Practicaste por primera vez con el método PrePAES",
    "image_url": "https://res.cloudinary.com/dohtxxlbe/image/upload/v1698069605/Logros%20PrePAES/logro-iniciando-el-viaje-prepaes.png"
    },
    {
        "name": "Mi primer ensayo",
        "description": "Practicaste por primera vez con una simulación de ensayo",
        "image_url": "https://res.cloudinary.com/dohtxxlbe/image/upload/v1698069712/Logros%20PrePAES/logo-mi-primer-ensayo.png"
    },
    {
        "name": "Excelencia en Matemáticas",
        "description": "Tuviste el puntaje máximo en uno de los ensayos",
        "image_url": "https://res.cloudinary.com/dohtxxlbe/image/upload/v1698069771/Logros%20PrePAES/logro-excelencia-en-matemáticas.png"
    },
    {
        "name": "Dominio de la Fase Inicial",
        "description": "Completaste la primera fase del método PrePAES",
        "image_url": "https://res.cloudinary.com/dohtxxlbe/image/upload/v1698069842/Logros%20PrePAES/logro-fase-inicial-prepaes.png"
    },
    {
        "name": "Creador de Ensayos",
        "description": "Creaste tu primer ensayo personalizado",
        "image_url": "https://res.cloudinary.com/dohtxxlbe/image/upload/v1698069885/Logros%20PrePAES/logro-creador-de-ensayos.png"
    }]

    for logros in logros_data:
        logros_object = Achievement.objects.create(**logros)

def questionDificult():
    pass

poblarBd(dataAlgebra)
poblarBd(dataNumeros)
poblarBd(dataProbabilidades)
poblarBd(dataGeometria)
poblarDbLogros()
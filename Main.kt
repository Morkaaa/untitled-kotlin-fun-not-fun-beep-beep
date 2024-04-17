import java.io.File
import javax.sound.midi.MidiSystem
import javax.sound.midi.ShortMessage

fun main() {
    // Název souboru MIDI
    print("Zadejte cestu k souboru MIDI s názvem: ")
    var midiFileName: String = readLine() ?: return
    if (!midiFileName.contains('.')){
        midiFileName += ".mid"
    }
    println("Zdrojový soubor: $midiFileName")
    // Načti soubor MIDI
    val midiFile = File(midiFileName)

    if (midiFile.exists()) {
        val tonesWithDurationAndPause = mutableListOf<Triple<Int, Double, Double>>() // Tóny s délkou a pauzou
        // Načti obsah souboru MIDI
        val sequence = MidiSystem.getSequence(midiFile)

        // Pro každou stopu
        for (i in 0 until sequence.tracks.size) {
            val track = sequence.tracks[i]

            // Aktivní tóny s jejich počátečním časem
            val activeNotes = mutableMapOf<Int, Long>()

            // Pro každou událost ve stopě
            for (j in 0 until track.size()) {
                val event = track[j]
                val message = event.message

                // Přidej tóny a jejich délky do seznamu
                when (message) {
                    is ShortMessage -> {
                        val note = message.data1
                        // Pokud je událost zapnutí tónu
                        if (message.command == ShortMessage.NOTE_ON) {
                            activeNotes[note] = event.tick
                        }
                        // Pokud je událost vypnutí tónu
                        else if (message.command == ShortMessage.NOTE_OFF) {
                            val startTime = activeNotes.remove(note) ?: continue
                            val duration = (event.tick - startTime).toDouble() / sequence.resolution.toDouble()
                            val pause = if (j + 1 < track.size()) {
                                val nextEvent = track[j + 1]
                                (nextEvent.tick - event.tick).toDouble() / sequence.resolution.toDouble()
                            } else {
                                0.0
                            }
                            tonesWithDurationAndPause.add(Triple(note, duration, pause))
                        }
                    }
                }
            }
        }

        // Vytvoř Python skript pro tyto tóny
        createPythonScript(tonesWithDurationAndPause, midiFileName)

        println("Python skript byl vytvorený.")
    } else {
        println("Súbor $midiFileName neexistuje.")
    }
}

fun createPythonScript(tonesWithDurationAndPause: List<Triple<Int, Double, Double>>, filename: String) {
    // Mapa MIDI hodnot na konstanty v buzzer_sample.py
    val midiToConstant = mapOf(
        128 to "gis6",
        127 to "g6",
        126 to "fis6",
        125 to "f6",
        124 to "e6",
        123 to "dis6",
        122 to "d6",
        121 to "cis6",
        120 to "c6",
        119 to "h5",
        118 to "ais5",
        117 to "a5",
        116 to "gis5",
        115 to "g5",
        114 to "fis5",
        113 to "f5",
        112 to "e5",
        111 to "dis5",
        110 to "d5",
        109 to "cis5",
        108 to "c5",
        107 to "h4",
        106 to "ais4",
        105 to "a4",
        104 to "gis4",
        103 to "g4",
        102 to "fis4",
        101 to "f4",
        100 to "e4",
        99 to "dis4",
        98 to "d4",
        97 to "cis4",
        96 to "c4",
        95 to "h3",
        94 to "ais3",
        93 to "a3",
        92 to "gis3",
        91 to "g3",
        90 to "fis3",
        89 to "f3",
        88 to "e3",
        87 to "dis3",
        86 to "d3",
        85 to "cis3",
        84 to "c3",
        83 to "h2",
        82 to "ais2",
        81 to "a2",
        80 to "gis2",
        79 to "g2",
        78 to "fis2",
        77 to "f2",
        76 to "e2",
        75 to "dis2",
        74 to "d2",
        73 to "cis2",
        72 to "c2",
        71 to "h1",
        70 to "ais1",
        69 to "a1",
        68 to "gis1",
        67 to "g1",
        66 to "fis1",
        65 to "f1",
        64 to "e1",
        63 to "dis1",
        62 to "d1",
        61 to "cis1",
        60 to "c1",
        59 to "h",
        58 to "ais ",
        57 to "a",
        56 to "gis ",
        55 to "g",
        54 to "fis ",
        53 to "f",
        52 to "e",
        51 to "dis ",
        50 to "d",
        49 to "cis ",
        48 to "c",
        47 to "H",
        46 to "Ais ",
        45 to "A",
        44 to "Gis ",
        43 to "G",
        42 to "Fis ",
        41 to "F",
        40 to "E",
        39 to "Dis ",
        38 to "D",
        37 to "Cis ",
        36 to "C",
        35 to "H1",
        34 to "Ais1",
        33 to "A1",
        32 to "Gis1",
        31 to "G1",
        30 to "Fis1",
        29 to "F1",
        28 to "E1",
        27 to "Dis1",
        26 to "D1",
        25 to "Cis1",
        24 to "C1",
        23 to "H2",
        22 to "Ais2",
        21 to "A2",
        20 to "Gis2",
        19 to "G2",
        18 to "Fis2",
        17 to "F2",
        16 to "E2",
        15 to "Dis2",
        14 to "D2",
        13 to "Cis2",
        12 to "C2",
        11 to "H3",
        10 to "Ais3",
        9 to "A3",
        8 to "Gis3",
        7 to "G3",
        6 to "Fis3",
        5 to "F3",
        4 to "E3",
        3 to "Dis3",
        2 to "D3",
        1 to "Cis3",
        0 to "C3"
    )
    val midiToFreq = mapOf(
        0 to "8",
        1 to "9",
        2 to "9",
        3 to "10",
        4 to "10",
        5 to "11",
        6 to "12",
        7 to "12",
        8 to "13",
        9 to "14",
        10 to "15",
        11 to "15",
        12 to "16",
        13 to "17",
        14 to "18",
        15 to "19",
        16 to "21",
        17 to "22",
        18 to "23",
        19 to "25",
        20 to "26",
        21 to "28",
        22 to "29",
        23 to "31",
        24 to "33",
        25 to "35",
        26 to "37",
        27 to "39",
        28 to "41",
        29 to "44",
        30 to "46",
        31 to "49",
        32 to "52",
        33 to "55",
        34 to "58",
        35 to "62",
        36 to "65",
        37 to "69",
        38 to "73",
        39 to "78",
        40 to "82",
        41 to "87",
        42 to "93",
        43 to "98",
        44 to "104",
        45 to "110",
        46 to "117",
        47 to "123",
        48 to "131",
        49 to "139",
        50 to "147",
        51 to "156",
        52 to "165",
        53 to "175",
        54 to "185",
        55 to "196",
        56 to "208",
        57 to "220",
        58 to "233",
        59 to "247",
        60 to "262",
        61 to "277",
        62 to "294",
        63 to "311",
        64 to "330",
        65 to "349",
        66 to "370",
        67 to "392",
        68 to "415",
        69 to "440",
        70 to "466",
        71 to "494",
        72 to "523",
        73 to "554",
        74 to "587",
        75 to "622",
        76 to "659",
        77 to "698",
        78 to "740",
        79 to "784",
        80 to "831",
        81 to "880",
        82 to "932",
        83 to "988",
        84 to "1047",
        85 to "1109",
        86 to "1175",
        87 to "1245",
        88 to "1319",
        89 to "1397",
        90 to "1480",
        91 to "1568",
        92 to "1661",
        93 to "1760",
        94 to "1865",
        95 to "1976",
        96 to "2093",
        97 to "2217",
        98 to "2349",
        99 to "2489",
        100 to "2637",
        101 to "2794",
        102 to "2960",
        103 to "3136",
        104 to "3322",
        105 to "3520",
        106 to "3729",
        107 to "3951",
        108 to "4186",
        109 to "4435",
        110 to "4699",
        111 to "4978",
        112 to "5274",
        113 to "5588",
        114 to "5920",
        115 to "6272",
        116 to "6645",
        117 to "7040",
        118 to "7459",
        119 to "7902",
        120 to "8372",
        121 to "8870",
        122 to "9397",
        123 to "9956",
        124 to "10548",
        125 to "11175",
        126 to "11840",
        127 to "12544",
        128 to "13290"
    )
    val uniqueTones = mutableSetOf<Int>()

    // Add all tones to the set
    for ((midiValue, _) in tonesWithDuration) {
        uniqueTones.add(midiValue)
    }
    // Vytvoř obsah pro soubor
    val content = buildString {
        appendLine("from machine import Pin, PWM")
        appendLine("from time import sleep")
        appendLine()


        for (midiValue in uniqueTones) {
            appendLine("${midiToConstant[midiValue]} = const(${midiToFreq[midiValue]})")
        }

        appendLine()
        appendLine("def ZahrajTón(buzzer, tón, trvanie, pauza=0):")
        appendLine("    buzzer.init(freq=tón, duty_u16=2**15)")
        appendLine("    sleep(trvanie)")
        appendLine("    buzzer.duty_u16(0)")
        appendLine("    sleep(pauza)")
        appendLine()

        appendLine("buzzer = PWM(Pin(2))")
        appendLine("buzzer.deinit()")
        appendLine("sleep(1)")

        for ((midiValue, duration, pause) in tonesWithDurationAndPause) {
            if (pause > 0) {
                appendLine("ZahrajTón(buzzer, ${midiToConstant[midiValue]}, $duration, $pause)")
                appendLine(pause)
            } else {
                appendLine("ZahrajTón(buzzer, ${midiToConstant[midiValue]}, $duration)")
                appendLine(pause)
            }
        }
    }

    // Ulož do souboru
    File("${filename}_sample.py").writeText(content)
}

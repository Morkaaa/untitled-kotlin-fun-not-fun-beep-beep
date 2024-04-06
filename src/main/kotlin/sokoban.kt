val lvl1 = listOf(
    "..#####.",
    "###...#.",
    "#.B.#..#",
    "#.#..O.#",
    "#....#.#",
    "##.#...#",
    ".#P..###",
    ".#####..",
)
fun map(){

}
fun isWall(x: Int, y: Int) = lvl1[y][x] == '#'
fun isFree(x: Int, y: Int) = !isWall(x, y)

fun main() {
    for(i in 0 until lvl1.size)
        println(lvl1[i])
}
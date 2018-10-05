import org.apache.spark.SparkContext

object wordCounts {
  def main(args: Array[String]): Unit = {
    val sc = new SparkContext("local[*]", "wordCounts")

    val lines = sc.textFile("./src/bible.txt", 1)
    val ordinary = (('a' to 'z') ++ " ").toSet
    val words = lines.flatMap(line => line.toLowerCase.filter(ordinary).split(" ")).filter(_ != "")
    val pairs = words.map(word => (word, 1))
    val wordCounts = pairs.reduceByKey(_ + _)
    wordCounts.sortBy(wc => -wc._2).foreach(wc => println(wc._1 + " appears: " + wc._2 + " times."))

  }
}

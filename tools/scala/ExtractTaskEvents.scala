import org.apache.spark.SparkContext

/**
 * Created by wkj on 2015/7/2.
 */
object ExtractTaskEvents {
  val etcMap = scala.collection.mutable.Map[String, String]()

  def main(args: Array[String]) {
    val sc = new SparkContext("local", "machine resource count", System.getenv("SPARK_HOME"))
    val file = sc.textFile("F:\\data\\task_events\\")
    val etc = sc.textFile("F:\\output\\etc\\fail_200_next_3k.csv")
    etc.foreach(line => if( ! line.startsWith("#") ) etcMap(line.split(',')(0)+'#'+line.split(',')(1) ) = "1" )
    println(etcMap.size)
    val task = file.filter(line =>
      etcMap.contains(line.split(',')(2) + '#' + line.split(',')(3))
    )
    task.saveAsTextFile("F:\\output\\fail_200_next_3k")
    println("ended")
  }
}

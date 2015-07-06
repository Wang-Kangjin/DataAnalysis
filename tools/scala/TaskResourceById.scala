/**
 * Created by wkj on 2015/6/6.
 */
import org.apache.spark.SparkContext
object TaskResourceById {
  val targetMap = scala.collection.mutable.Map[String, String]()


  def main(args: Array[String]) {
    val sc = new SparkContext("local", "machine resource count", System.getenv("SPARK_HOME"))
    val file = sc.textFile("F:\\data\\task_usage_csv\\")
    val etc = sc.textFile("F:\\output\\etc\\fail_1_time_top100.csv")
    etc.foreach(line => targetMap(line.split(',')(1)+'#'+line.split(',')(2) ) = "1" )
    val task = file.filter(line =>
      targetMap.contains(line.split(',')(2) + '#' + line.split(',')(3))
      )
    task.saveAsTextFile("F:\\output\\fail_1_top100")
    println("ended")
  }
}

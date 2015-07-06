/**
 * Created by wkj on 2015/6/23.
 */
/**
 * Created by wkj on 2015/6/6.
 */
import org.apache.spark.SparkContext
object TaskResourceById_1_and_2900ResourceById {
  val targetMap = scala.collection.mutable.Map[String, String]()


  def main(args: Array[String]) {
    val sc = new SparkContext("local", "machine resource count", System.getenv("SPARK_HOME"))
    val file = sc.textFile("F:\\data\\task_usage_csv\\")
    val etc = sc.textFile("F:\\output\\etc\\fail_1_and_top3000.csv")
    etc.foreach(line => if( ! line.startsWith("#") ) targetMap(line.split(',')(0)+'#'+line.split(',')(1) ) = "1" )
    println(targetMap.size)
    val task = file.filter(line =>
      targetMap.contains(line.split(',')(2) + '#' + line.split(',')(3))
    )
    task.saveAsTextFile("F:\\output\\fail_1_top2900")
    println("ended")
  }
}

/**
 * Created by wkj on 2015/6/28.
 */
import org.apache.spark.SparkContext
object ExtractTaskFailTime {
  val targetMap = scala.collection.mutable.Map[String, String]()

  def have(k:String, v:String): Boolean= {
    val key = k + "," + v
    targetMap.contains(key)
  }

  def main(args: Array[String]) {
    val sc = new SparkContext("local", "taskFailTime", System.getenv("SPARK_HOME"))
    val etc = sc.textFile("F:\\output\\etc\\fail_200_next_3k.csv")
    etc.foreach(line => targetMap(line.split(',')(0) + "," + line.split(',')(1)) = line.split(',')(1))
    val file = sc.textFile("F:\\data\\task_events\\")
    //    val task  = file.filter(line => have(line.split(',')(2), line.split(',')(3)) && line.split(',')(5) == "3")
    //    .map(line => (line.split(',')(2) + "," + line.split(',')(3), ((line.split(',')(0).toFloat - 600000000)/300000000) ))
    //    .sortByKey()
    //    task.saveAsTextFile("F:\\task\\fail_time_spark")
    val task_evict  = file.filter(line => have(line.split(',')(2), line.split(',')(3)) && line.split(',')(5) == "2")
      .map(line => (line.split(',')(2) + "," + line.split(',')(3), ((line.split(',')(0).toFloat - 600000000)/300000000) ))
      .sortByKey()
    task_evict.saveAsTextFile("F:\\task\\fail_200_next_3k_evicttime_spark")
    val task_kill  = file.filter(line => have(line.split(',')(2), line.split(',')(3)) && line.split(',')(5) == "5")
      .map(line => (line.split(',')(2) + "," + line.split(',')(3), ((line.split(',')(0).toFloat - 600000000)/300000000) ))
      .sortByKey()
    task_kill.saveAsTextFile("F:\\task\\fail_200_next_3k_killtime_spark")
    //    val etc = sc.textFile("F:\\task\\fail_1_time_top100.csv")
    //    etc.foreach(line => targetMap(line.split(',')(1) + "," + line.split(',')(2)) = line.split(',')(2))
    //    val file = sc.textFile("F:\\task_events\\")
    //    val task  = file.filter(line => have(line.split(',')(2), line.split(',')(3)) && line.split(',')(5) == "5")
    //      .map(line => (line.split(',')(2) + "," + line.split(',')(3), ((line.split(',')(0).toFloat - 600000000)/300000000) ))
    //      .sortByKey()
    //    task.saveAsTextFile("F:\\task\\fail_1_killtime_spark")
  }
}

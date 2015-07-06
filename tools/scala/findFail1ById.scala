/**
 * Created by wkj on 2015/6/21.
 */

import org.apache.spark.SparkContext


object FindFailOne {
  val targetMap = scala.collection.mutable.Map[String, Long]()
  def have(k: String): Boolean ={
    targetMap.contains(k)
  }
  def map_line(line : String):(String,Long)= {
    val key: String = line.split(',')(2) + '#' + line.split(',')(3)
    val timestamp = line.split(',')(0).toLong
    if (targetMap.get(key).get == 0)
      targetMap(key) = timestamp
    (key,timestamp - targetMap(key))
  }

  def main(args: Array[String]) {
    val sc = new SparkContext("local", "machine resource count", System.getenv("SPARK_HOME"))
    val file = sc.textFile("F:\\data\\task_events\\")
    val etc = sc.textFile("F:\\output\\etc\\targetjob_fail_1.csv")
    etc.foreach(line => targetMap(line.split(',')(0)+'#'+line.split(',')(1) ) = 0 )
    println(targetMap.size)
    val task = file.filter(line =>
      targetMap.contains(line.split(',')(2) + '#' + line.split(',')(3))
    ).map(map_line)
     .reduceByKey((value1, value2) => if( value1 > value2 ) value1 else value2)
     .map( item => (item._2/300000000/12, item._1) )
     .sortByKey()
    task.saveAsTextFile("F:\\output\\fail_1")
    println("ended")
  }
}

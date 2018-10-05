import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;
import scala.Tuple2;

import java.util.Arrays;
import java.util.Iterator;

public class wordCounts {
    public static void main(String[] args) {
        SparkConf conf = new SparkConf()
                .setAppName("wordCounts")
                .setMaster("local[*]");

        JavaSparkContext sc = new JavaSparkContext(conf);
        JavaRDD<String> lines = sc.textFile("./src/bible.txt", 1);
        JavaRDD<String> words = lines.flatMap(new FlatMapFunction<String, String>() {
            @Override
            public Iterator<String> call(String s) throws Exception {
                return Arrays.asList(s.toLowerCase().replaceAll("[\\pP|~|$|^|<|>|\\||\\+|=`�[0-9]]*", "").split(" ")).iterator();
            }
        });
        JavaPairRDD<String, Integer> pairs = words.mapToPair(
                new PairFunction<String, String, Integer>() {
                    @Override
                    public Tuple2<String, Integer> call(String s) throws Exception {
                        return new Tuple2<String, Integer>(s, 1);
                    }
                }
        );
        JavaPairRDD<String, Integer> lineCounts = pairs.reduceByKey(
                new Function2<Integer, Integer, Integer>() {
                    @Override
                    public Integer call(Integer integer, Integer integer2) throws Exception {
                        return integer + integer2;
                    }
                }
        );
        lineCounts.foreach(new VoidFunction<Tuple2<String, Integer>>() {
                               @Override
                               public void call(Tuple2<String, Integer> t) throws Exception {
                                   System.out.println(t._1 + " appears " + t._2 + " times.");
                               }
                           }
        );

        sc.close();
    }
}

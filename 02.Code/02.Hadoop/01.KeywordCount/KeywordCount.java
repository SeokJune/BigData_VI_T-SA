/**
 * @KeywordCount
 * @Title: 드라이버 클래스(맵과 리듀스를 등록하는 일 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modifier: Lee_yun_Hyuck
 * @Modify_on: 2019-04-09
 * @text: 주석 추가, 클래스명 변경
 */
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class KeywordCount {
	public static void main(String[] args) throws Exception {
            // Create the conf object needed for Hadoop implementation (hdfs-site, core-site)	
	    Configuration conf = new Configuration();
	    // Create job object for job execution
	    Job job = Job.getInstance(conf, "Keywordcount");
	    // Specify the library file to be used for job execution
	    job.setJarByClass(KeywordCount.class);
	    // Set the classes to use in the job
	    job.setMapperClass(KeywordCountMapper.class);
	    job.setCombinerClass(KeywordCountReducer.class);
	    job.setReducerClass(KeywordCountReducer.class);
	    // Set key and value type of output data of mapper and reducer class
	    job.setOutputKeyClass(Text.class);
	    job.setOutputValueClass(IntWritable.class);
	    // Set the I / O data path.
	    // The first parameter is the input parameter, the second parameter is the output parameter
	    FileInputFormat.addInputPath(job, new Path(args[0]));
	    FileOutputFormat.setOutputPath(job, new Path(args[1]));
	    // If the same values as the path needed for execution are entered
	    System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}

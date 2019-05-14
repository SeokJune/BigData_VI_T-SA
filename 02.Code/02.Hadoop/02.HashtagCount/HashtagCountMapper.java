
/**
 * @HashtagCount
 * @Title: 맵 클래스(raw 데이터를 가져와 key와 value로 바꾸는 작업 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-28
 */

import java.io.IOException;
import java.util.StringTokenizer;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//The generic type of the Mapper class <input key, input value, output key, output value>
//It can be changed to the type corresponding to long, int, String required by Hadoop. 
public class HashtagCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    //Stores the constant 1 as an IntWritable value.
    //Used to count words with the value of IntWritable in the Reduce.
    private final static IntWritable one = new IntWritable(1);
    //Text object to save the word from output
    private Text word = new Text();
 
 
    //Mapping keys and values to keys and values to reduce
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
       
       // Breaks text that comes in as a blank space.
    	  StringTokenizer itr = new StringTokenizer(value.toString());
         // Repeat as long as there is no next token to return (false).
         while(itr.hasMoreTokens()) {
         // Call the next variable in the ktr variable, save it by removing leading and trailing spaces.
             String ktr = itr.nextToken().trim(); 

          // If the length of the word stored in ktr is more than one character but less than 5 characters
          if(ktr.getBytes().length > (byte)3 && ktr.getBytes().length < (byte)16) {
                 
                 // Load the word ktr in text in the word object.
                 word.set(ktr);
                 // Define the value to pass to the redox
                 context.write(word, one);
             	}
         }
    }
}

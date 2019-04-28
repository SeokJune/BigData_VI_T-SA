
/**
 * @HashtagCount
 * @Title: 매퍼 클래스(맵과 리듀스를 등록하는 일 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-28
 */

import java.io.IOException;
import java.util.StringTokenizer;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
 
public class HashtagCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
 
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
    	  StringTokenizer itr = new StringTokenizer(value.toString());
         while(itr.hasMoreTokens()) {
             String ktr = itr.nextToken().trim(); 
             if(ktr.getBytes().length > (byte)3 && ktr.getBytes().length < (byte)16) {
                 word.set(ktr);
                 context.write(word, one);
             	}
         }
    }
}
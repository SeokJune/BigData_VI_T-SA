/**
 * @KeywordCountReducer
 * @Title: 리듀스 클래스(맵에서 선별한 데이터(key, value)를 같은 키를 기준으로 더하는 작업 수행 )
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modifier: Lee_yun_Hyuck
 * @Modify_on: 2019-04-09
 * @text: 주석 추가, 클래스 명 변경
 */
import java.io.IOException;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
// Reducer class inheritance, output the same type of input and output.
public class KeywordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
    private IntWritable result = new IntWritable();
 
    // Redefine methods to add outputting parameters and override methods Method overrides
    // Iterable <> is to extract values only because the values stored in IntWritable are tied in the map.
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values,
            Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
     // Variable that stores a value that increases by the number of words
     int sum = 0;
     // Find the number of each character and add up the words.
        for (IntWritable val : values) {
            sum += val.get();
        }
        // Set the output value to the result that generated the IntWritable object which is the input / output type of the MapReduce.
        // At this time, the output value is the sum of words.
        result.set(sum);
        // Use the key of the input data as the output key through the write method of the context object.
        context.write(key, result);
    }
}


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

//Mapper 클래스의 generic 타입  <입력키, 입력값, 출력키, 출력값>
//하둡에서 요구되는 long, int, String에 대응되는 타입으로 변경해서 사용
public class HashtagCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    //IntWritable값으로 상수 1을 저장한다.
   	//리듀스에서 IntWritable의 값을 가지고 단어 카운트 할 때 사용.
    private final static IntWritable one = new IntWritable(1);
    //출력물에서 나오는 단어를 저장하고자 하는 Text 객체
    private Text word = new Text();
 
 
    //입력되는 키와 값에 대해 리듀스로 넘어갈 키와 값으로 매핑 
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
       //공백 단위로 들어온 텍스트를 끊어 온다.
    	  StringTokenizer itr = new StringTokenizer(value.toString());
         //리턴할 다음 토큰이 없을 때(false) 만큼 반복. 
         while(itr.hasMoreTokens()) {
             //ktr 변수에 다음 변수를 불러오는데 앞, 뒤 공백을 제거하여 저장.
             String ktr = itr.nextToken().trim(); 
             //ktr에 저장되는 단어의 길이가 한글자 이상 5글자 이하인 경우 조건
             if(ktr.getBytes().length > (byte)3 && ktr.getBytes().length < (byte)16) {
                 // word 객체에 text 형식으로 ktr단어 적재.
                 word.set(ktr);
                 // 리듀스에 넘겨줄 값 정의
                 context.write(word, one);
             	}
         }
    }
}

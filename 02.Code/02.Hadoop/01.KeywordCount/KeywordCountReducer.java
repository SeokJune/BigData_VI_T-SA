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
//Reducer 클래스 상속, 입력과 출력을 같은 타입으로 출력.
public class KeywordCountReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
    private IntWritable result = new IntWritable();
 
    //출력 파라미터를 가져와서 더해주는 기능을 추가하기 위한 리듀스 메서드 재정의
    //Iterable<>로 감싸진 이유는 맵에서 IntWritable에 저장된 값들이 묶여 있기 때문에 values 값들만 추출하기 위해서이다.
    @Override
    protected void reduce(Text key, Iterable<IntWritable> values,
            Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
      //단어의 수만큼 증가하는 값을 저장하는 변수
    	int sum = 0;
    	//각각의 글자 수를 알아내어 단어를 합산한다.
        for (IntWritable val : values) {
            sum += val.get();
        }
        //맵리듀스의 입출력 타입인 IntWritable객체를 생성한 result에 출력값을 설정.
        //이 때, 출력값은 단어의 합산한 값.
        result.set(sum);
        //context객체의 write메서드를 통해  출력 키로 입력 데이터의 키를 그대로 사용한다.
        context.write(key, result);
    }
}

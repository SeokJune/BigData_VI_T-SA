/**
 * @KeywordCountMapper
 * @Title: 맵 클래스(raw 데이터를 가져와 key와 value로 바꾸는 작업 수행)
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modify_on: 2019-04-15
 * @text: 주석 추가, 클래스 명 변경, 자연어 처리
 */
import java.io.IOException;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.snu.ids.kkma.index.Keyword;
import org.snu.ids.kkma.index.KeywordExtractor;
import org.snu.ids.kkma.index.KeywordList;




//Mapper 클래스의 generic 타입  <입력키, 입력값, 출력키, 출력값>
//하둡에서 요구되는 long, int, String에 대응되는 타입으로 변경해서 사용 
public class KeywordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    //IntWritable값으로 상수 1을 저장한다.
	//리듀스에서 IntWritable의 값을 가지고 단어 카운트 할 때 사용.
	private final static IntWritable one = new IntWritable(1);
     //출력물에서 나오는 단어를 저장하고자 하는 Text 객체
	private Text word = new Text();
 
     //입력되는 키와 값에 대해 리듀스로 넘어갈 키와 값으로 매핑 	
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
        //------------------------------------자연어 처리부분-----------------------------------------
    	KeywordExtractor ke = new KeywordExtractor();
		KeywordList kl = ke.extractKeyword(value.toString(), true);
       //------------------------------------------------------------------------------------------
    	
    	//공백 단위로 들어온 텍스트를 끊어 온다.
    	//DB에서 가져온 데이터는 ,로 구분되어 있기 때문에 replaceAll 명령을 통해 ,를 공백으로 바꾼다.
    	//StringTokenizer itr = new StringTokenizer(value.toString().replaceAll(",", " "));
        /*
          while(itr.hasMoreTokens()) {
    		word.set(itr.nextToken());
    		word.set(itr.next());
    		context.write(word, one);
        }
         */
    	//리턴할 다음 토큰이 없을 때(false) 만큼 반복. 
		for( int i = 0; i < kl.size(); i++ ) {
    		//다음 토큰을 리턴하고, 이전 토큰은 제거 한다.
			Keyword kwrd = kl.get(i);
    		word.set(kwrd.getString());
    		//context 객체는 키-값쌍으로 내보낼 때 사용되며, 출력타입으로 인자화 된다.
    		context.write(word, one);
        }
    }
}
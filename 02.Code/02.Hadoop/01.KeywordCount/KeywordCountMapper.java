
/**
 * @KeywordCountMapper
 * @Title: 매퍼 클래스(맵에서 선별한 데이터(key, value)를 같은 키를 기준으로 더하는 작업 수행 )
 * @author: Lee_yun_Hyuck
 * @Create_at: 2019-04-06
 * @Modifier: Lee_yun_Hyuck
 * @Modify_on: 2019-04-28
 * @text: 주석 추가, 클래스 명 변경, 자연어처리(한글자 이상 5글자 이하로 제한, 사용자 사전 추가)
 */

import java.io.IOException;
import java.util.Iterator;
import java.util.List;
import java.util.StringTokenizer;
 
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import kr.co.shineware.nlp.komoran.constant.DEFAULT_MODEL;
import kr.co.shineware.nlp.komoran.core.Komoran;
import kr.co.shineware.nlp.komoran.model.KomoranResult;

//The generic type of the Mapper class <input key, input value, output key, output value>
//It can be changed to the type corresponding to long, int, String required by Hadoop. 
public class KeywordCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    //Stores the constant 1 as an IntWritable value.
    //Used to count words with the value of IntWritable in the Reduce.
    private final static IntWritable one = new IntWritable(1);
    //Text object to save the word from output
    private Text word = new Text();
 
    //Mapping keys and values to keys and values to reduce
    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
            throws IOException, InterruptedException {
         //Breaks text that comes in blank spaces. Process the remaining characters including the remaining special characters
        StringTokenizer itr = new StringTokenizer(value.toString(), " \t\n\r,.'\"-=%…()[]{}“▷+ⓒ!?:;#\'");
        
         //Repeat as long as there is no next token to return (false)
        while(itr.hasMoreTokens()) {
        	  //
        	  String token = itr.nextToken();
              //---------------------------------------------Natural language processing---------------------------------------
        	  //Create Como objects DEFAULT_MODEL Use default dictionary << Predefined
        	  Komoran komoran = new Komoran(DEFAULT_MODEL.FULL);
        	  //Add user dictionary path (user noun can be defined)
        	  komoran.setUserDic("/home/vi/eclipse-workspace/KeywordCount/src/dic.user");
        	  //Analyze the words you read
            KomoranResult analyzeResultList = komoran.analyze(token);
            //tokens list, then categorized and loaded for nouns.
            List<String> tokens = analyzeResultList.getMorphesByTags("SL","NNP","NNG");
              //After creating an Iterator to read the elements, load the tokens content.
            Iterator<String> itrs = tokens.iterator();
      	      //----------------------------------------------------------------------------------------------------------------
            //The context object is used when exporting key-value pairs, and is parameterized as an output type.
            while(itrs.hasNext()) {
            //Save the word processed by natural language by creating ktr variable. (Remove word, space)
            String ktr = itrs.next().trim();
            //The condition when the word stored in ktr is more than one character or less than 5 characters.
            if(ktr.getBytes().length > (byte)3 && ktr.getBytes().length < (byte)16) {
            	  //Insert ktr into the word object.
                word.set(ktr);
                //The context object is used when exporting key-value pairs, and is parameterized as an output type.
                context.write(word, one);
            	}
            }
        }
    }
}

#%%
## import package
import os
import random
import json
from k_sat_func import *
import time
from nltk import sent_tokenize, word_tokenize
from itertools import combinations, permutations

## preset for question_dict
question_dict_sample={'passageID':None,
                    'question_type':None,
                    'question':None, 
                    'new_passage':None,
                    'answer':None,## 1~5번
                    'e1':None, 'e2':None, 'e3':None, 'e4':None, 'e5':None}

#%% 다음 글의 목적/주장/요지로 가장 적절한 것은?
class Q1:
    def __init__(self):
        self.question_type=1
        self.qlist=['목적으로', '주장으로', '요지로']
        self.question=f'다음 글의 {random.choice(self.qlist)} 가장 적절한 것은?'

    def get_ans(self, passage:str)->str:
        return get_paraphrased_sentences_1(passage)

    def get_dist(self, passage:str)->list:
        return get_false_sentences_n(passage, 4)
    
    def make_json(self, passageID:int, passage:str, is_Korean=False):
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID'] = int(passageID)
        question_dict['question_type'] = self.question_type
        question_dict['question'] = self.question
        question_dict['new_passage'] = passage

        answer_sentence=self.get_ans(passage)
        dist_list=self.get_dist(passage)

        if answer_sentence == None or dist_list == None: return None
        
        ## choose answer
        ansidx=random.randint(0, 4)    # ans: 0~4
        question_dict['answer'] = ansidx + 1   ## 0~4 -> 1~5

        dist_list.insert(ansidx, answer_sentence)

        ex_list=[]
        for i in dist_list:
            ex_list.append(check_punctuation_capital_sentence(i))
        
        if len(ex_list) == 5:
            question_dict['e1'] = ex_list[0]
            question_dict['e2'] = ex_list[1]
            question_dict['e3'] = ex_list[2]
            question_dict['e4'] = ex_list[3]
            question_dict['e5'] = ex_list[4]
        else: return None
        return json.dumps(question_dict, ensure_ascii = False)

#%% 윗글에 관한 내용으로 가장 적절한/적절하지 않은 것은?
class Q2:
    def __init__(self):
        self.question_type=2
        self.qlist =['적절한', '적절하지 않은']
        choice = random.choice(self.qlist)
        # choice =  '적절하지 않은'
        self.flag = True
        if choice=='적절하지 않은': self.flag = False

        self.question=f'윗글에 관한 내용으로 가장 {choice} 것은?'

    def get_ans(self, passage:str):
        if self.flag == True: return get_paraphrased_sentences_1(passage)
        else: return get_paraphrased_sentences_n(passage, 4)

    def get_dist(self, passage:str):
        if self.flag == True: return get_false_sentences_n(passage, 4)
        else: return get_false_sentences_1(passage)

    def make_json(self, passageID:int, passage:str, is_Korean=False):
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question
        question_dict['new_passage'] = passage

        ans=self.get_ans(passage)
        dist=self.get_dist(passage)
        if ans == None or dist == None: return None

        if self.flag==True:
            ## ans: str, dist: list
            ansidx=random.randint(0, 4)    # ans: 0~4
            question_dict['answer'] = ansidx+1   ## 0~4 -> 1~5

            dist.insert(ansidx, ans)
            tmp_ex_list = dist

        else:
            ## ans: list, dist: str
            ansidx=random.randint(0, 4)    # ans: 0~4
            question_dict['answer'] = ansidx+1   ## 0~4 -> 1~5

            ans.insert(ansidx, dist)
            tmp_ex_list = ans


        ex_list=[]
        for i in tmp_ex_list:
            ex_list.append(check_punctuation_capital_sentence(i))
        
        if len(ex_list) == 5:
            question_dict['e1'] = ex_list[0]
            question_dict['e2'] = ex_list[1]
            question_dict['e3'] = ex_list[2]
            question_dict['e4'] = ex_list[3]
            question_dict['e5'] = ex_list[4]
        else: return None
        return json.dumps(question_dict, ensure_ascii = False)

#%% 주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.
class Q3:
    def __init__(self):
        self.question_type=3
        self.question='주어진 글 다음에 이어질 글의 순서로 가장 적절한 것을 고르시오.'

    def separate(self, passage:str):

        sent=sent_tokenize(passage)
        sent_num=len(sent)
        output_passage_list=[]
        new_passage=sent[0]+'\n\n'

        a=int((sent_num-1)/3)
        if a==0: return None

        output_passage_list.append(sent[1:1+a])
        output_passage_list.append(sent[1+a:1+2*a])
        output_passage_list.append(sent[1+2*a:])

        dist_list=[['A','C','B'],['B','A','C'],['B','C','A'],['C','A','B'],['C','B','A']]
        ansidx=random.randint(0, 4)    ## ans: 0~4

        output=[0 for i in range(3)]
        outputidx_dict={'A':0, 'B':1, 'C':2}

        for i in range(3):
            outputidx=outputidx_dict[dist_list[ansidx][i]]
            sent='('+dist_list[ansidx][i]+')   '
            for j in output_passage_list[i]:
                sent=sent+j
            output[outputidx]=(sent.replace('.', '. '))

        for i in output:
            new_passage=new_passage+'\n'+i

        for i in range(len(dist_list)):
            ex_str=''
            for j in dist_list[i]:
                ex_str=ex_str+'('+j+')\t'
            dist_list[i]=ex_str.strip().replace('\t', '-')

        return new_passage, ansidx, dist_list

    def make_json(self, passageID:int, passage:str)->dict:
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question

        separate_output = self.separate(passage)
        if separate_output == None: return None
        new_passage, ansidx, ex_list=separate_output[0], separate_output[1], separate_output[2]

        question_dict['new_passage'] = new_passage
        question_dict['answer']=ansidx+1


        if len(ex_list)==5:
            question_dict['e1']=ex_list[0]
            question_dict['e2']=ex_list[1]
            question_dict['e3']=ex_list[2]
            question_dict['e4']=ex_list[3]
            question_dict['e5']=ex_list[4]
        else:
            return None
        return json.dumps(question_dict, ensure_ascii = False)

#%% 다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.
class Q4:
    def __init__(self):
        self.question_type = 4
        self.question = '다음 빈칸에 들어갈 말로 가장 적절한 것을 고르시오.'

    def get_ans(self, passage:str)->str:
        kwd_list = get_kwd_n_list(passage, 1)
        if kwd_list == None: return None
        return kwd_list[0][0]

    def get_dist(self, kwd:str)->list:    ## 오답 단어 4개 만들기
        kwd_lmtzr=get_lmtzr(kwd)

        antonym= get_antonym_list_gpt(kwd_lmtzr, 5)
        if antonym == None: return None
        antonym_list, _ = antonym[0], antonym[1]

        synonym = get_synonym_list_gpt(kwd_lmtzr, 5)
        if synonym == None: return None
        synonym_list, _ = synonym[0], synonym[1]

        if len(antonym_list)+len(synonym_list) < 4: return None
        if len(antonym_list)+len(synonym_list) == 4: return antonym_list+synonym_list

        distractors_pre = del_same_start(del_same_lemmatization(antonym_list+synonym_list))
        if distractors_pre == None or len(distractors_pre) == 0: return None

        ## 정답과 4글자 이상 유사한거 삭제, None이 선지에 들어가지 않도록 처리하기
        distractors = []
        if len(kwd) >= 4:
            kwd_start = kwd[:4]
        else: kwd_start = kwd
        for i in distractors_pre:
            if kwd_start not in i and i != 'None':
                distractors.append(i)

        if len(distractors) < 4: return None
        distractors = random.sample(distractors, 4)
        return distractors

    def make_new_passage(self, passage:str, answer:str)->str:
        space = '_'*int(len(answer)*0.6)

        cnt_ans = passage.count(answer)
        cnt_ans_l = passage.count(answer.lower())
        
        if cnt_ans == 0 and cnt_ans_l == 0: return None

        elif cnt_ans == 0 and cnt_ans_l == 1:
            new_passage = passage.replace(answer.lower(), space, 1)

        elif cnt_ans == 0 and cnt_ans_l > 1: 
            loc = random.randint(1, cnt_ans_l)

            new_passage = passage.replace(answer.lower(), space, loc)
            new_passage = new_passage.replace(space, answer.lower(), loc-1)

        elif cnt_ans == 1: 
            new_passage = passage.replace(answer, space, 1)

        else:
            loc = random.randint(1, cnt_ans_l)
            new_passage = passage.replace(answer.lower(), space, loc)
            new_passage = new_passage.replace(space, answer.lower(), loc-1)

        return new_passage

      
    def make_json(self, passageID:int, passage:str):
        question_dict = question_dict_sample.copy()
        question_dict['passageID'] = int(passageID)
        question_dict['question_type'] = self.question_type
        question_dict['question'] = self.question

        ans = self.get_ans(passage)
        if ans == None: 
            return None

        dist_list = self.get_dist(ans)    ## list(4개)
        if dist_list == None: 
            return None


        new_passage=self.make_new_passage(passage, ans)   ##str
        if new_passage==None: 
            return None

        question_dict['new_passage']=new_passage

        ansidx=random.randint(0, 4)    ## ans: 0~4
        question_dict['answer']=ansidx+1
        dist_list.insert(ansidx, ans)

        ex_list=[]
        for w in dist_list:
            ex_list.append(w.capitalize().strip())

        if len(ex_list) == 5:
            question_dict['e1']=ex_list[0]
            question_dict['e2']=ex_list[1]
            question_dict['e3']=ex_list[2]
            question_dict['e4']=ex_list[3]
            question_dict['e5']=ex_list[4]
        else: 
            return None
        return json.dumps(question_dict, ensure_ascii = False)

#%% 다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?
class Q5:
    def __init__(self):
        
        self.question_type=5
        self.question='다음 글의 밑줄 친 부분 중, 문맥상 낱말의 쓰임이 적절하지 않은 것은?'

    def get_keyword_list(self, passage: str)->list:
        kwd=get_kwd_n_list(passage, 5)
        if kwd == None: return None
        if kwd[1] == False: return None
        return kwd[0]

    def get_antonym_and_ansidx(self, passage:str, kwd_list:list)->str:
        ansidx_list=[]
        antonym_list=[]
        ansidx = -1

        for i in range(len(kwd_list)):
            keyword=kwd_list[i]
            antonym = get_antonym_list_gpt(keyword, 1)
            if antonym != None:
                antonym_w = antonym[0][0]
                ansidx = i
                break
            time.sleep(5)
            if ansidx < 0: return None

        return antonym_w, ansidx

    def make_new_passage_exlist_ansidx(self, passage:str, keyword_list:list, tmp_ansidx:int, antonym:str):
        new_passage=''+passage

        if len(keyword_list) !=5: return None

        for i in range(len(keyword_list)):
            kwd=keyword_list[i]
            space = '(__index__) '+kwd

            if i == tmp_ansidx: space = '(__index__) '+ antonym
            cnt_kwd = passage.count(kwd)
            cnt_kwd_l = passage.count(kwd.lower())

            if cnt_kwd == 0 and cnt_kwd_l == 0: 
                return None

            elif cnt_kwd == 0 and cnt_kwd_l == 1:
                new_passage = new_passage.replace(kwd.lower(), space.lower(), 1)

            elif cnt_kwd == 0 and cnt_kwd_l > 1: 
                loc = random.randint(1, cnt_kwd_l)
                new_passage = new_passage.replace(kwd.lower(), space.lower(), loc)
                new_passage = new_passage.replace(space.lower(), kwd.lower(), loc-1)

            elif cnt_kwd == 1: 
                new_passage = new_passage.replace(kwd, space, 1)

            else:
                loc = random.randint(1, cnt_kwd_l)
                new_passage = new_passage.replace(kwd.lower(), space.lower(), loc)
                new_passage = new_passage.replace(space.lower(), kwd.lower(), loc-1)
        
        new_passage_word=word_tokenize(new_passage)
        ex_list=[]

        for i in range(len(new_passage_word)):
            if new_passage_word[i] == '(__index__)' or (new_passage_word[i-1].endswith('_') and new_passage_word[i]==')'):
                ex_list.append(new_passage_word[i+1])

        for i in range(5):
            new_passage = new_passage.replace('(__index__)', '('+str(i+1)+')', 1)
        
        if antonym in ex_list:
            ansidx=ex_list.index(antonym)
        elif antonym.lower() in ex_list:
            ansidx=ex_list.index(antonym.lower())

        else: return None

        return new_passage, ex_list, ansidx
    
    def make_json(self, passageID:int, passage:str):
        question_dict=question_dict_sample.copy()
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] =self.question
        
        keyword_list=self.get_keyword_list(passage)
        if keyword_list == None or len(keyword_list) == 0: 
            # print(question_dict['passageID'], ': keyword_list == None' )
            return None

        get_antonym_and_ansidx_output=self.get_antonym_and_ansidx(passage, keyword_list)
        if get_antonym_and_ansidx_output == None: 
            # print(question_dict['passageID'], ': get_antonym_and_ansidx == None' )
            return None
        antonym, tmp_ansidx = get_antonym_and_ansidx_output[0], get_antonym_and_ansidx_output[1]


        output= self.make_new_passage_exlist_ansidx(passage, keyword_list, tmp_ansidx, antonym)
        if output == None: 
            # print(question_dict['passageID'], ': make_new_passage_exlist_ansidx == None' )
            return None
        new_passage, ex_list,ansidx = output[0], output[1], output[2]
        
        question_dict['new_passage']=new_passage
        question_dict['answer']=ansidx+1


        if len(ex_list)==5:
            question_dict['e1'] = ex_list[0].capitalize().strip()
            question_dict['e2'] = ex_list[1].capitalize().strip()
            question_dict['e3'] = ex_list[2].capitalize().strip()
            question_dict['e4'] = ex_list[3].capitalize().strip()
            question_dict['e5'] = ex_list[4].capitalize().strip()
        else: 
            # print(question_dict['passageID'], ': ex_list == None' )
            return None
        return json.dumps(question_dict, ensure_ascii = False)

#%% 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.
'''class Q6:
    def __init__(self):
        self.question_type=6
        self.question='글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.'
    
    def separate(self,passage:str):
        sent=sent_tokenize(passage)
        s_sentence=sent[0]
        sent.remove(s_sentence)

        ans_sentence=random.choice(sent)
        ansidx=sent.index(ans_sentence)
        sent.remove(ans_sentence)

        if len(sent) < 5: return None
        sample = random.sample(sent, 5)

        cnt=1
        for i in range(len(sent)):
            if sent[i] in sample:
                sent[i]='('+str(cnt)+') '+sent[i]
                cnt+=1
        new_passage=ans_sentence+'\n\n'+s_sentence
        for i in sent:
            new_passage=new_passage+i
        
        return new_passage, ansidx


    def make_json(self, passageID:int, passage:str):# , passage:str)->dict:
        # 글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question

        separate_output=self.separate(passage)
        if separate_output==None : return None
        new_passage, ansidx=separate_output[0], separate_output[1]
        
        question_dict['new_passage'] = new_passage
        question_dict['answer']=ansidx+1

        question_dict['e1'] = '1'
        question_dict['e2'] = '2'
        question_dict['e3'] = '3'
        question_dict['e4'] = '4'
        question_dict['e5'] = '5'
        return json.dumps(question_dict, ensure_ascii = False)
'''
class Q6:
    def __init__(self):
        self.question_type=6
        self.question='글의 흐름으로 보아, 주어진 문장이 들어가기에 가장 적절한 곳을 고르시오.'
    
    #문장단위로 쪼개기
    def separate(self,passage:str):
        temp=passage.split('.')
        l=len(temp)

        if(l-1<7):
            return 0,0,0,False
        
        answer_list=[1,2,3,4,5]
        ans=random.randint(1,5)

        num=range(1,l-1)          # 문장 번호

        if len(num)>=5:
            select=random.sample(num,5) # 그 중에 5개
            select.sort()
        else:
            return 0, 0, 0,False


        distractors=[x for x in answer_list if x!=ans] 

        # 정답 문장
        ans_text=temp[select[ans-1]]
        ans_text_num=select[ans-1]


        head=range(1,ans_text_num)
        tail=range(ans_text_num+2,l)

        if (ans==1):
            tail_select=random.sample(tail,4)
            tail_select.sort()
            select=tail_select
            select.append(ans_text_num)
        if(ans==5):
            head_select=random.sample(head,4)
            head_select.sort()
            select=head_select
            select.append(ans_text_num)
        if(ans==2 or ans==3 or ans==4):
            head_select=random.sample(head,ans-1)
            head_select.sort()
            tail_select=random.sample(tail,5-ans)
            tail_select.sort()
            select=head_select+tail_select
            select.append(ans_text_num)
        
        select.sort()

        for i in range(0,5):
            temp[select[i]]='('+str(answer_list[i])+')'+str(temp[select[i]])
        
        temp[select[ans-1]]='('+str(ans)+')'+str(temp[select[ans-1]+1])
        del temp[select[ans-1]+1]


        ## 문제 출력
        new_passage='. '.join(temp)
        new_passage=str(ans_text)+'\n\n'+str(new_passage)

        return new_passage, ans, distractors, True


    def make_json(self, passageID:int, passage:str):
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question
        new_passage, ans, distractors, flag=self.separate(passage)
        if flag==False:return None
        
        question_dict['new_passage'] = new_passage
        question_dict['answer']=ans
        N=0
        for i in range(1,6):
            if (i==ans): 
                question_dict['e'+str(i)]=ans
                continue
            question_dict['e'+str(i)]=distractors[N]
            N+=1

        return json.dumps(question_dict, ensure_ascii = False)
#
#%% 다음 글에서 전체 흐름과 관계 없는 문장은?
class Q7:
    def __init__(self):
        self.question_type=7
        self.question='다음 글에서 전체 흐름과 관계 없는 문장은?'

    def get_ans(self, passage: str)->str:
        return get_false_sentences_1(passage).strip()

    def make_new_passage_and_ansidx(self, passage: str, answer: str)->str:
        sent=sent_tokenize(passage)
        s_sentence=sent[0]
        sent.remove(s_sentence)
        new_passage=s_sentence

        if len(sent) < 5: return None
        sample=random.sample(sent, 5)
        ansidx=random.randint(0, 4)

        cnt=0
        for i in range(len(sent)):
            if sent[i] in sample:
                snt = '('+str(cnt+1)+')'+sent[i]
                if cnt == ansidx:
                    tmp=sent[i]
                    snt ='('+str(cnt+1)+')'+answer+' '+tmp
                sent[i]=snt
                cnt+=1
        for i in sent:
            new_passage=new_passage+' '+i
        return new_passage, ansidx

    def make_json(self, passageID:int, passage:str)->dict:
        question_dict=question_dict_sample.copy()
        
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question   ## 다음 글에서 전체 흐름과 관계 없는 문장은?

        ans_sent=self.get_ans(passage)  ## list5개
        if ans_sent == None : return None

        make_new_passage_and_ansidx_output=self.make_new_passage_and_ansidx(passage, ans_sent)    ## dict
        if make_new_passage_and_ansidx_output == None: return None
        new_passage, ansidx = make_new_passage_and_ansidx_output[0], make_new_passage_and_ansidx_output[1]
        
        question_dict['new_passage'] = new_passage
        question_dict['answer'] = ansidx+1
        question_dict['e1'] = '1'
        question_dict['e2'] = '2'
        question_dict['e3'] = '3'
        question_dict['e4'] = '4'
        question_dict['e5'] = '5'
        return json.dumps(question_dict, ensure_ascii = False)

#%% 다음 글의 내용을 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?
class Q8:
    def __init__(self):
        self.question_type=8
        self.question='다음 글의 내용을 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?'

    def paraphrase(self, passage:str)->str:
        return get_paraphrased_sentences_1(passage, 'Q8')

    def get_keyword(self, paraphrase:str) ->list:
        keyword= get_kwd_n_list(paraphrase, 2)
        if keyword == None: return None
        if keyword[1] == False: return None
        return keyword[0]
    
    def get_distractors_fromPassage(self, passage:str, keyword:list, paraphrase:str)->list:    ## 오답 단어 2개 만들기
        kwd=get_kwd_n_list(passage, 5)

        if kwd == None: return None
        kwd_list, _ = kwd[0], kwd[1]

        passage_keyword=del_same_start(del_same_lemmatization(kwd_list+keyword))
        if passage_keyword == None: return None

        passage_dist_list=[]
        for i in passage_keyword:
            if i.lower() not in paraphrase.lower():
                passage_dist_list.append(i)

        if len(passage_dist_list) == 0: return None
        return passage_dist_list
    
    def get_distractors_fromWord(self, keyword: str):
        synonym=get_synonym_list_gpt(keyword, 2)
        if synonym == None: synonym_list=[]
        else: synonym_list = synonym[0]

        time.sleep(2)

        antonym=get_antonym_list_gpt(keyword, 2)
        if antonym == None: antonym_list=[]
        else: antonym_list = antonym[0]

        return synonym_list, antonym_list

    def get_distractors(self, passage:str, keyword:list, paraphrase:str)->list:
        a, b=keyword[0], keyword[1]

        a_synonym_list, a_antonym_list = self.get_distractors_fromWord(a)
        b_synonym_list, b_antonym_list = self.get_distractors_fromWord(b)
        if a_synonym_list + a_antonym_list == [] or b_synonym_list + b_antonym_list == []: return None

        passage_dist_list=self.get_distractors_fromPassage(passage, keyword, paraphrase)
        if passage_dist_list== None: passage_dist_list = []

        a_dist=[]; b_dist=[]    ## 둘 다 3개

        if len(a_synonym_list) >= 1 and len(a_antonym_list) >= 2:
            a_dist=[random.choice(a_synonym_list)]+random.sample(a_antonym_list, 2)
        elif len(a_synonym_list) + len(a_antonym_list) >= 3 :
            a_dist=random.sample(a_synonym_list+a_antonym_list, 3)
        elif len(a_synonym_list) + len(a_antonym_list) + len(passage_dist_list) >= 3 :
            a_dist=random.sample(a_synonym_list+a_antonym_list+passage_dist_list, 3)

        
        if len(b_synonym_list) >= 1 and len(b_antonym_list) >= 2:
            b_dist=[random.choice(b_synonym_list)]+random.sample(b_antonym_list, 2)
        elif len(b_synonym_list) + len(b_antonym_list) >= 3 :
            b_dist=random.sample(b_synonym_list+b_antonym_list, 3)
        elif len(b_synonym_list) + len(b_antonym_list) + len(passage_dist_list) >= 3 :
            b_dist=random.sample(b_synonym_list+b_antonym_list+passage_dist_list, 3)
        
        if a_dist==[] or b_dist==[]: return None

        dist_list_pre=[]
        idx = 0

        for a in a_dist:
            for b in b_dist:
                if a!=b:  dist_list_pre.append((a, b))
    
        while True:
            dist_list=random.sample(dist_list_pre, 4)
            a_dist=[];b_dist=[]
            for i in dist_list:
                a_dist.append(i[0])
                b_dist.append(i[1])
            if len(list(set(a_dist))) >= 2 and len(list(set(b_dist))) >= 2: 
                break
        return dist_list
        
    def make_new_passage(self, passage:str, paraphrase:str, keyword:list)->str:
        # self.question='다음 글의 내용을 요약하고자 한다. 빈칸 (A), (B)에 들어갈 말로 가장 적절한 것은?'
        new_passage=passage + '\n\n==>'
        new_paraphrase='' + paraphrase
        space='__(index)__'
        
        for kwd in keyword:
            if kwd in paraphrase or kwd.lower() in paraphrase:
                cnt_kwd = paraphrase.count(kwd)
                cnt_kwd_l = paraphrase.count(kwd.lower())
                # print(kwd, cnt_kwd, cnt_kwd_l)

                if cnt_kwd == 0 and cnt_kwd_l == 0: 
                    return None

                elif cnt_kwd == 0 and cnt_kwd_l == 1:
                    new_paraphrase = new_paraphrase.replace(kwd.lower(), space.lower(), 1)

                elif cnt_kwd == 0 and cnt_kwd_l > 1: 
                    loc = random.randint(1, cnt_kwd_l)
                    new_paraphrase = new_paraphrase.replace(kwd.lower(), space.lower(), loc)
                    new_paraphrase = new_paraphrase.replace(space.lower(), kwd.lower(), loc-1)

                elif cnt_kwd == 1: 
                    new_paraphrase = new_paraphrase.replace(kwd, space, 1)

                else:
                    loc = random.randint(1, cnt_kwd_l)
                    new_paraphrase = new_paraphrase.replace(kwd.lower(), space.lower(), loc)
                    new_paraphrase = new_paraphrase.replace(space.lower(), kwd.lower(), loc-1)
        
        ascci_A = 65  ##'A'의 아스키코드
        for i in range(new_paraphrase.count(space)):
            new_paraphrase = new_paraphrase.replace(space, '('+chr(ascci_A+i)+')', 1)

        new_passage = new_passage+new_paraphrase
        # print(new_passage)
        return new_passage

    def make_json(self, passageID:int, passage:str):
        question_dict=question_dict_sample.copy()
        question_dict['passageID']=int(passageID)
        question_dict['question_type']=self.question_type
        question_dict['question'] = self.question

        paraphrase=self.paraphrase(passage)   ## list
        if paraphrase == None: 
            return None
        paraphrase=check_punctuation_capital_sentence(paraphrase)
        if paraphrase == None: 
            return None

        keyword=self.get_keyword(paraphrase)    ## list
        if keyword == None: 
            return None

        new_passage=self.make_new_passage(passage, paraphrase, keyword) ## str
        if new_passage == None: 
            return None
        question_dict['new_passage'] = new_passage
        
        dist_list =self.get_distractors(passage, keyword, paraphrase)
        if dist_list==None: 
            return None

        ans=random.randint(0, 4)
        question_dict['answer']=ans+1

            
        ex_list = []
        for i in dist_list:
            ex_list.append('(A)'+i[0].title()+' (B) '+i[1].title())
        ex_list.insert(ans, '(A)'+keyword[0].title()+' (B) '+keyword[1].title())

        if len(ex_list)==5:
            question_dict['e1']=ex_list[0]
            question_dict['e2']=ex_list[1]
            question_dict['e3']=ex_list[2]
            question_dict['e4']=ex_list[3]
            question_dict['e5']=ex_list[4]
        else:
            return 
            None
        
        return json.dumps(question_dict, ensure_ascii = False)

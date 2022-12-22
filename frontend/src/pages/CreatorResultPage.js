import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import Header from "../components/Header";
import { Link, useLocation } from "react-router-dom";
import QuestionBox from "../components/QuestionBox";
import { ExampleQuestionList } from "../assets/bank/Example-QuestionList";
import axios from "axios";
import Button from "../components/Button";
import { BoxWrapper, WordFileButton, Description } from "../components/Wrapper";

const CreatorResultPage = () => {
    const location = useLocation();
    const [isLoading, setIsLoading] = useState(false); //로딩중임을 표시하는 state
    const [questionList, setQuestionList] = useState(ExampleQuestionList);
    let i=0; //문제 번호

    useEffect(()=> {
        const fetchData = async() => {
            console.log(location.state.passageValue);
            setIsLoading(true);
            let response;
            try {
                response = await axios.post(`http://localhost:9000/new_question/`, { "passage" : location.state.passageValue });
            } catch(error) {
                console.log(error);
            }
            response = response.data;
            console.log(response);
            setQuestionList(response);
            setIsLoading(false);
        }
        fetchData();
    }, [location]);

    return (
        <>
        <Header category={'creator'}/>
        <BoxWrapper>
        {
        isLoading? (
            <BoxWrapper>
                <div class="clock"></div>
                <div className="strong-font load-more">
                    입력한 지문을 바탕으로 SOULMATE AI가 문제를 제작하는 중이에요.<br/>
                    최대 120초가 걸려요.
                </div>
            </BoxWrapper>
        ) : (
        <>
            <Description>
                새로운 지문으로부터 문제를 생성했어요!
            </Description>
            <WordFileButton href="http://localhost:9000/get_docx">
                <Button
                    className={'word-file-btn'}
                    label="시험지로 저장하기"
                />
            </WordFileButton>
            <>
            {
                questionList.map((it) => ( 
                    <QuestionBox key={i++} id={i} 
                        title={it.question} type={it.question_type} 
                        paragraph={it.new_passage} answer={it.answer} 
                        e1={it.e1} e2={it.e2} e3={it.e3} e4={it.e4} e5={it.e5}/>
                    )
                )
            }
            </></>
            )
        }
        </BoxWrapper>
        </>
    );
};


export default CreatorResultPage;
import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import Header from "../components/Header";
import { Link, useLocation } from "react-router-dom";
import QuestionBox from "../components/QuestionBox";
import { ExampleQuestionList } from "../assets/bank/Example-QuestionList";
import axios from "axios";

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

const BoxWrapper = styled.div`
    width: 100%;
    padding: 2rem 8rem 2rem 8rem;

    @media(max-width: 1880px){
        padding: 2rem 2rem 2rem 2rem;
    }
`;
const Description = styled.span`
    font-size: 1.5rem;
    font-weight: 700;
    padding: 2rem 0 2rem 0;
`;
const GR = styled.span`
    color: green;
`;
export default CreatorResultPage;
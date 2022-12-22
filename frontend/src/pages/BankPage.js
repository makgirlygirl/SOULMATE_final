import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import Header from "../components/Header";
import { Link, useNavigate } from "react-router-dom";
import QnumDescription from "../assets/bank/bank_qnum_description.png";
import Arrow from '../assets/main/arrow.svg';
import { isElementOfType } from "react-dom/test-utils";
import QuestionTypeButton from "../components/QuestionTypeButton";
import { GoButton, QuestionWrapper, TextWrapper, TypeWrapper, Wrapper } from "../components/Wrapper";

export const qTypeList = [ 
    {id:1, label:"글의 목적/주제"},
    {id:2, label:"일치/불일치"},
    {id:3, label:"순서 배열"},
    {id:4, label:"빈칸 추론"},
    {id:5, label:"어휘"},
    {id:6, label:"문장 삽입"},
    {id:7, label:"흐름과 관계 없는 문장 찾기"},
    {id:8, label:"요약문"},
];
const BankPage = () => {
    const navigate = useNavigate();
    const [qTypeNum, setQTypeNum] = useState(0);
    const [qNum, setQNum] = useState(0);
    const onChangeQNum = (e) => {
        setQNum(e.target.value);
    }
    return (
      <Wrapper>
      <Header category='bank'/>
        <div>
            <TextWrapper>Step 1. 검색할 문제의 유형을 선택하세요.</TextWrapper>
            {
                qTypeList.map((it) => (
                    <TypeWrapper>
                        <QuestionTypeButton key={it.id} {...it} onClick={() => {setQTypeNum(it.id)}} selected={qTypeNum}/>
                    </TypeWrapper>
            ))}
        </div>
        <TextWrapper><img src={Arrow}/></TextWrapper>
        <div>
        <TextWrapper>Step 2. 문제 개수를 지정해주세요.</TextWrapper>
        <Wrapper><DescImg src={QnumDescription}/></Wrapper>
        <TypeWrapper>
            <InputLine
                key="qNum"
                value={qNum}
                onChange={onChangeQNum}
            />
            <TextWrapper>개</TextWrapper>
        </TypeWrapper>
        </div>
        <TextWrapper><img src={Arrow}/></TextWrapper>
        <QuestionWrapper>
            <GoButton onClick={() => {
                if(qTypeNum===0 || qNum===0)
                    console.log("incomplete input"); // 뒤로 넘기지 않고, alert 보내주기
                else {
                    console.log(qTypeNum);
                    navigate("/bank/result", { state: { qTypeValue:qTypeNum, qNumValue:qNum } });
                }
            }}>GO!</GoButton>
        </QuestionWrapper>
      </Wrapper>
      
    );
}
const DescImg = styled.img`
    @media (max-width: 720px) {
        width: 13rem;
    }
`;
const InputLine = styled.input`
    resize: none;
    width: 12rem;
    height: 2rem;
    font-size: 2rem;
    font-weight: 900;
    padding: 3rem;
    border-right:0px; 
    border-top:0px; 
    border-left:0px; 
    border-bottom-width:1;
    background: transparent;
    text-align: center;
    outline: none;
    @media (max-width: 720px) {
        width: 40%;
        height: 1.5rem;
        font-size: 1rem;
        padding: 2.5rem;
    }
`; 
export default BankPage;
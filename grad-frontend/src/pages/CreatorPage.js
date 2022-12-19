import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import Header from "../components/Header";
import { useNavigate } from "react-router-dom";
import Arrow from '../assets/main/arrow.svg';

const CreatorPage = () => {
  const navigate = useNavigate();
  const [passage, setPassage] = useState("");
  const onChangePassage = (e) => {
    setPassage(e.target.value);
  }
  return (
      <Wrapper>
        <Header category='creator'/>
        <div>
          <TextWrapper>문제를 만들 지문을 입력하세요.</TextWrapper>
          <TypeWrapper>
            <InputBox
              key="passage"
              value={passage}
              onChange={onChangePassage}
            />
          </TypeWrapper>
        </div>
        <TextWrapper><img src={Arrow}/></TextWrapper>
        <QuestionWrapper>
            <Button onClick={() => {
                navigate("/creator/result", { state: { passageValue:passage } });
            }}>GO!</Button>
        </QuestionWrapper>
      </Wrapper>
    );
}

const Wrapper = styled.div`
    width: 100%;
`;
const QuestionWrapper = styled.div`
    display: flex;
    justify-content:center;
    padding: 4rem;
`;
const TextWrapper = styled.div`
    display: flex;
    justify-content:center;
    padding: 2.5rem;
    font-size: 1.5rem;
    font-weight: bold;
`;
const TypeWrapper = styled.div`
    width: 100%;
    display: flex;
    justify-content:center;
`;
const Button = styled.button`
    width: 36rem;
    height: 4rem;
    background: rgba(1, 129, 51, 0.78);
    border: 5px solid rgba(58, 166, 100, 0.64);
    box-shadow: 1px 1px 20px #ddd;
    border-radius: 3rem;
    font-size: 2rem;
    font-family: 'Noto Sans KR';
    font-weight: 700;
    color: white;
    &:hover{  
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
      }
`;
const InputBox = styled.textarea`
  box-sizing: border-box;
  width: 45%;
  min-height: 500px;
  padding: 1rem;
  resize: none;
  font-size: 1rem;
  font-family: 'Gothic A1', sans-serif;
  background: rgba(1, 129, 51, 0.13);
  border: 6px solid rgba(58, 166, 100, 0.64);
  border-radius: 6px;
  @media(max-width: 1880px){
    width: 60%;
  }@media(max-width: 1280px){
    width: 80%;
  }
`;
export default CreatorPage;
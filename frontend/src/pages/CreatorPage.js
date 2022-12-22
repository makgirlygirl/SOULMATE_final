import React, { useEffect, useState } from "react";
import styled from 'styled-components';
import Header from "../components/Header";
import { useNavigate } from "react-router-dom";
import Arrow from '../assets/main/arrow.svg';
import { GoButton, QuestionWrapper, TextWrapper, TypeWrapper, Wrapper } from "../components/Wrapper";

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
            <GoButton onClick={() => {
                navigate("/creator/result", { state: { passageValue:passage } });
            }}>GO!</GoButton>
        </QuestionWrapper>
      </Wrapper>
    );
}
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
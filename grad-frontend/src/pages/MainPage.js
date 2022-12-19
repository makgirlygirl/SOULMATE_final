import React, { useState } from "react";
import styled from "styled-components";
import Header from "../components/Header";
import MainImage1 from "../assets/main/001.png";
import MainImage2 from "../assets/main/002.png";
import MainImage3 from "../assets/main/003.jpeg";
import { Link } from "react-router-dom";

const MainPage = () => {
    return (
      <Wrapper>
          <Header main={true}/>
          <MainContent1>
            <div className='main-content-text-right'>
              <h2>영어 공부, 이제 SOULMATE와 함께 하세요.</h2>
              <h1>자기주도 영어 학습 플랫폼, <br/> SOULMATE</h1>
            </div>
            <MainImg src={MainImage1}/>
            </MainContent1>
          <MainContent2>
            <MainImg src={MainImage3}/>
            <div className='main-content-text-left'>
              <h2>
              SOULMATE AI가 제작한<br/>
              1,600+개의 <br/>
              수능 기출 변형 문제 은행<br/>
              </h2>
              <Link to="/bank">
                <h5 className="green-font">SOULMATE 문제 은행 바로 가기 →</h5>
            </Link>
            </div>
          </MainContent2>
          <MainContent3>
            <div className='main-content-text-right'>
              <h2>
              원하는 지문을 입력하면<br/>
              수능 유형의 문제 자동 생성<br/>
              </h2>
              <Link to="/creator">
                <h5 className="green-font">실시간 문제 제작하러 가기 →</h5>
              </Link>
            </div>
            <MainImg src={MainImage2}/>
          </MainContent3>
          <Footer>Copyright 2022. makgirlygirl. All rights reserved.</Footer>
      </Wrapper>
    
    )
  }
  const Wrapper = styled.div`
    width: 100%;
    font-family: 'IBM Plex Sans KR', sans-serif;
  `;
  //font-family: 'Nanum Gothic', sans-serif;
  
  const MainContent1 = styled.div`
    width: 100%;
    min-height: 60vh;
    display: flex;
    background: #00B247;
    padding: 5%;
    justify-content: center;
    text-align: center;
    line-height: 5rem;
    color: #FFFFFF;
    @media (max-width: 1080px) {
      display: inline-block;
      line-height: 4rem;
      min-height: 40vh;
    }
  `;
  const MainContent2 = styled.div`
    width: 100%;
    min-height: 60vh;
    display: flex;
    background: white;
    padding: 10%;
    justify-content: center;
    text-align: center;
    line-height: 3.5rem;
    @media (max-width: 1080px) {
      display: inline-block;
      line-height: 3rem;
      min-height: 40vh;
    }
  `;
  const MainContent3 = styled.div`
    width: 100%;
    min-height: 40vh;
    display: flex;
    background: #A6D8BA;
    padding: 8%;
    justify-content: center;
    text-align: center;
    line-height: 3.5rem;
    @media (max-width: 1080px) {
      display: inline-block;
      min-height: 30vh;
    }
  `;
  const Footer = styled.div`
    width: 100%;
    min-height: 5vh;
    padding: 1rem;
    text-align: center;
    font-family: 'Nanum Gothic', sans-serif;
    font-size: 12px;
  `;
  const MainImg = styled.img`
    width: 23rem;
    height: fit-content;
    margin: 0 2rem 0 2rem;
    @media (max-width: 1580px) {
      width: 20rem;
    }@media (max-width: 1080px) {
      width: 7rem;
    }
  `;
  export default MainPage;
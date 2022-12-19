import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import styled from 'styled-components';
import Button from "./Button";
import SelectNum from "./SelectNum";
import Swal from "sweetalert2";

const QuestionBox = ({id, title, paragraph, answer, e1,e2,e3,e4,e5}) => {
    const [selected, setSelected] = useState(0);
    
    /* 제출 시 토글로 정답을 보여주기 위한 state */
    const [toggleStatus, setToggleStatus] = useState(false);
    const onClickToggle = (e) => {
        setToggleStatus(prevStatus => prevStatus ? false : true);
    }
    const submitAnswer = ({selected, answer}) => {
        if(selected==answer) return <ToggleMenu isCorrect={true} selected={selected} answer={answer}/>;
        else return <ToggleMenu isCorrect={false} selected={selected} answer={answer}/>;
    };
    const ToggleMenu = ({isCorrect, selected, answer}) => (
        <div className="pt-4 pb-8">
        <div className="flex flex-col w-full mx-auto px-4">
            <div className="flex flex-col space-y-2 text-gray-500 general-font">
                <Box>
                    <div className="strong-font">
                    {isCorrect ? 
                        <div>정답이에요!</div> : 
                        <div>정답이 아니에요. 정답은 {answer}번이에요.</div>
                    }
                    </div>
                    선택한 답: {selected}<br/>
                    정답: {answer}<br/>
                </Box>
            </div>
        </div>
        </div>
    );
    /* 잘못된 문제 신고 시 */
    const showAlert = () => {
        const Toast = Swal.mixin({
          toast:true,
          position:'center-center',
          showConfirmButton: false,
                    timer: 1500,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
        })
        Toast.fire({
            icon: 'success',
            title: `잘못된 문제 신고가 접수되었어요.`
          });
    } 
    return (
            <BoxWrapper>
                <UpperBox>
                    <div>#{id+1} {title}</div>
                </UpperBox>
                <Box>
                    <Paragraph>{paragraph}</Paragraph>
                    <ChoiceBox>
                    <ChoiceList>
                        <SelectNum id={1} selected={selected} onClick={()=>{setSelected(1)}}/>
                        <span>{e1}</span>
                    </ChoiceList>
                    <ChoiceList>
                        <SelectNum id={2} selected={selected} onClick={()=>{setSelected(2)}}/>
                        <span>{e2}</span>
                    </ChoiceList>
                    <ChoiceList>
                        <SelectNum id={3} selected={selected} onClick={()=>{setSelected(3)}}/>
                        <span>{e3}</span>
                    </ChoiceList>
                    <ChoiceList>
                        <SelectNum id={4} selected={selected} onClick={()=>{setSelected(4)}}/>
                        <span>{e4}</span>
                    </ChoiceList>
                    <ChoiceList>
                        <SelectNum id={5} selected={selected} onClick={()=>{setSelected(5)}}/>
                        <span>{e5}</span>
                    </ChoiceList>
                    <UnderBox>
                        <Button 
                            label='정답 확인'
                            className={'show-answer-btn' + (toggleStatus? " active":"")} 
                            onClick={() => {onClickToggle()}}/>
                        <Button 
                            label='잘못된 문제 신고하기'
                            className='show-answer-btn' 
                            onClick={() => {showAlert()}}/> 
                    </UnderBox>
                    </ChoiceBox>
                    {toggleStatus ? 
                            submitAnswer({selected, answer}) : null}
                </Box>
            </BoxWrapper>
    ); 
}
export default QuestionBox;

const BoxWrapper = styled.div`
    box-sizing: border-box;
    display: block;
    justify-content : center;
    width: 80%;
    margin: auto;
    padding: 2rem;
    @media(max-width: 1580px){
        width: 90%;
    } @media(max-width: 1080px){
        width: 100%;
        padding: 2rem 0 0 0;
    }
`;
const Box = styled.div`
    box-sizing: border-box;
    border: 1px solid #999999;
    padding: 1.5rem;
    display: block;
    width: 100%;
`;
const UpperBox = styled.div`
    box-sizing: border-box;
    display: block;
    padding: 1rem;
    font-size: 1rem;
    font-weight: 900;
    color: black;
    background: rgba(58, 166, 100, 0.4);
    border: 2px solid rgba(1, 129, 51, 0.78);
    border-radius: 5px;
`;
const Paragraph = styled.div`
    border: 2px solid #999999;  
    padding: 1rem;
`;
const ChoiceList = styled.div`
    padding-top: .5rem;
    display:flex;
`; 
const ChoiceBox = styled.div`
    padding-top: 1rem;
`
const UnderBox = styled.div`
    box-sizing: border-box;
    padding: 1.5rem 2rem 1rem 2rem;
    display:flex;
`;
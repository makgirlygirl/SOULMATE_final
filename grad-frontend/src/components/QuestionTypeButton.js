import React, { useState } from "react";
import styled from 'styled-components';

import { u1, u2, u3, u4, u5, u6, u7, u8 } from './FileIndex';
import { c1, c2, c3, c4, c5, c6, c7, c8 } from './FileIndex';

// 버튼 하나를 구현
const QuestionTypeButton = ({id, selected, onClick}) => {
    
    const uncheckedButtonList = [u1, u2, u3, u4, u5, u6, u7, u8];
    const checkedButtonList = [c1, c2, c3, c4, c5, c6, c7, c8];

    return (
    <>
    {
        id == selected ?
        <TypeButton onClick={onClick} src={checkedButtonList[id-1]} alt="type_checked"/> : 
        <TypeButton onClick={onClick} src={uncheckedButtonList[id-1]} alt="type_unchecked"/>
    }
    </>
)};
const TypeButton = styled.img`    
    padding: 0.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
`;
export default QuestionTypeButton;

/**
    width: 214px;
    height: 51px;
    left: 718px;
    top: 404px;

    border: 3px solid #018133;
    border-radius: 25px;

 */
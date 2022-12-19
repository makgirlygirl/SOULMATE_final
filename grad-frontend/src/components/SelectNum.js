import React, { useState } from "react";
import styled from "styled-components";

const SelectNum = ({id, selected, onClick}) => {
    return (
      <CircleBtn 
        onClick={onClick}
        className={"btn" + (id==selected ? " active" : "")}
      >{id}</CircleBtn>
    );  
  };

const CircleBtn = styled.button`
    display: block;
    font-size: 1rem;
    font-weight: bold;
    width: 30px;
    height: 30px;
    margin: 0 .5rem 0 .5rem;
    background: white;
    display: inline-block;
    text-align: center;

    border-radius: 1rem;
    line-height: 1rem;
    border: .15rem solid green;
`;
export default SelectNum;
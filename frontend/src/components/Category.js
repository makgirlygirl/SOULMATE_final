import React, { useState } from "react";
import { Link } from "react-router-dom";
import styled from 'styled-components';
import Bank from "../assets/category/bank_unchecked.svg";
import Creator from "../assets/category/creator_unchecked.svg";
import Bank_checked from '../assets/category/bank_checked.svg';
import Creator_checked from "../assets/category/creator_checked.svg";

const Category = ({label}) => {

    if(label=='bank'){
        return (
            <CategoryWrapper>
                <Link to='/bank'><CategoryLogo src={Bank_checked} alt="bank_checked"/></Link>
                <Link to='/creator'><CategoryLogo src={Creator} alt="creator_unchecked"/></Link>
            </CategoryWrapper>
        );
    } else if(label=='creator'){
        return (
            <CategoryWrapper>
                <Link to='/bank'><CategoryLogo src={Bank} alt="bank_unchecked"/></Link>
                <Link to='/creator'><CategoryLogo src={Creator_checked} alt="creator_checked"/></Link>
            </CategoryWrapper>
            );
    } else {
        return (
            <CategoryWrapper>
                <Link to='/bank'><CategoryLogo src={Bank} alt="bank_unchecked"/></Link>
                <Link to='/creator'><CategoryLogo src={Creator} alt="creator_unchecked"/></Link>
            </CategoryWrapper>
            );
    }      
    };
const CategoryWrapper = styled.div`
    width: 100%;
    display: flex;
    justify-content : center;
    padding: 1rem;
    padding-bottom: 3rem;
    @media (max-width: 1080px) {
        padding-bottom: 0;
      }
`;
const CategoryLogo = styled.img`
    height: 3.5rem;
    padding: 0 1rem 0 1rem;
    @media(max-width: 1080px){
        height: 2rem;
    }
`;
  
  export default Category;
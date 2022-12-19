import React, { useState } from "react";
import styled from "styled-components";
const Button = ({label, className, onClick}) => {
    return (
      <button className={className} onClick={onClick}>{label}</button>
    ); // 
  };
export default Button;

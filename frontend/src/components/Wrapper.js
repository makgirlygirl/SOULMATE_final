/** styled component를 이용해 BankPage, CreatorPage 에서 사용할 Wrapper를 정의하는 파일 */
import styled from 'styled-components';

/** Intro page */
export const Wrapper = styled.div`
    width: 100%;
    text-align: center;
`;
export const QuestionWrapper = styled.div`
    display: flex;
    justify-content:center;
    padding: 4rem;
`
export const TextWrapper = styled.div`
    display: flex;
    justify-content:center;
    padding: 2.5rem;
    font-size: 1.5rem;
    font-weight: bold;
    @media (max-width: 720px) {
        font-size: .8rem;
      }
`;
export const TypeWrapper = styled.div`
    width: 100%;
    display: flex;
    justify-content:center;
`;

/** Result pages */
export const BoxWrapper = styled.div`
    width: 100%;
    padding: 2rem 8rem 2rem 8rem;
    @media(max-width: 1580px){
        padding: 2rem 1rem 2rem 1rem;
    }
`;
export const Description = styled.span`
    font-size: 1.5rem;
    font-weight: 700;
    padding: 2rem 0 2rem 0;
    @media(max-width: 720px){
        font-size: 1rem;
    }
`;
/** Buttons */
export const GoButton = styled.button`
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
export const WordFileButton = styled.a`
    width: 100%;
    display: flex;
    justify-content : right;
    padding-right: 2rem;
`;

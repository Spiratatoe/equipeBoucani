import React, { useState } from "react";
import styled from "styled-components";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import { faTrashCan,faPen } from '@fortawesome/free-solid-svg-icons';
import CommentAPIService from "../../pages/BACKEND_DEBUG/CommentAPIService";
//import React, { useState } from "react";
import Modal from "react-modal";
export const CardTitle = styled.h1`
    font-size: 2em;
`;
export const CardGivenTitle = styled.h4`
    font-size: 1.25em;
`;
export const CardArticle = styled.div`
    border: 1px solid darkblue;
    margin: 10px;
    width: 100%;
    align-self: stretch;
`;
export const CardText = styled.p`
`;
export const CardDate = styled.b`
`;
export const CardDeleteButton = styled.button`
    float: right;
    margin-right: 3.5em;
    font-size: 2ch;
    background: none;
    
    
`;
export const CardEditButton = styled.button`
    float: right;
    margin-right: 3.5em;
    font-size: 2ch;
    background: none;
    color: green;
    
`;

export const SubmitCancelButton = styled.button`
    margin: 1.5em;
    font-size: 2ch;
    text-align: center;
    width: 5em;
    color: black;
`;
const CoreUICard = ({title,body,id,date,editDate}) => {
    const [jobTitle, setJobTitle] = useState("");
    const [jobDescription, setJobDescription] = useState("");
    const [toBeEditedID, setToBeEditedID] = useState("");
    const [isOpen, setIsOpen] = useState(false);

    const toggleModal = () => {
        setIsOpen(!isOpen);
    };

    const handleEdit = (event) => {

        CommentAPIService.UpdateCommentPut(toBeEditedID, {"title" : jobTitle, "body" : jobDescription})
            //.then((response) => props.postedComment(response))
            .then((any)=> window.location.reload())
            .catch(error => console.log('Following error occured after fetching from API: ',error))
        setJobTitle('')
        setJobDescription('')
    };
return (<>
    <CardArticle>



        <CardTitle>Job post ID#{id} </CardTitle>
        <CardDeleteButton onClick={() => handleDelete(id)}><FontAwesomeIcon icon={faTrashCan}/></CardDeleteButton>
        <CardEditButton onClick={() => {setToBeEditedID(id); toggleModal(); setJobTitle(title); setJobDescription(body)}}><FontAwesomeIcon icon={faPen}/></CardEditButton>

        <CardGivenTitle >{title}</CardGivenTitle>

        <CardText>

            {body}

        </CardText>

        <CardDate>Date Posted: {date}
        </CardDate>
        <CardText></CardText>
        <CardDate>{editDate !== "Invalid Date" ? "Date Edited: " + editDate : ""}
        </CardDate>


    </CardArticle>
    <Modal isOpen={isOpen} onRequestClose={toggleModal} ariaHideApp={false}>
        <form onSubmit={() => {handleEdit(); toggleModal()}}>
            <br/><br/>
            <label>
                Job Title:
                <input
                    type="text"
                    name="jobTitle"
                    id="jobTitle"
                    onChange={(e) => setJobTitle(e.target.value)}
                    value={jobTitle}
                />
            </label>
            <label>
                Job Description:
                <textarea
                    type="text"
                    name="jobDescription"
                    id="jobDescription"
                    rows="4" cols="75"
                    onChange={(e) => setJobDescription(e.target.value)}
                    value={jobDescription}
                />
            </label>
            <SubmitCancelButton type="submit">Submit</SubmitCancelButton>
            <SubmitCancelButton onClick={() => toggleModal()}>Cancel</SubmitCancelButton>
        </form>
        <form onClose={toggleModal} />
    </Modal>
    </>);};

    const handleDelete = (comment_id) => {
        //event.preventDefault();

        CommentAPIService.DeleteComment(comment_id)
            .then((any)=> window.location.reload())
            .catch(error => console.log('Following error occured after fetching from API: ',error))

        //console.log(window.location.href);

    };




export default CoreUICard;

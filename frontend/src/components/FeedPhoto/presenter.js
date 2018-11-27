import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";
import PhotoActions from "components/PhotoActions";
import PhotoComments from "components/PhotoComments";
import TimeStamp from "components/TimeStamp";
import CommentBox from "components/CommentBox";

const FeedPhoto = (props, context) => {
  return (
    <div className={styles.feedPhoto}>
      <header>
        <img
          src={props.creator.profile_image || require("images/noPhoto.jpeg")}
          alt={props.creator.username}
        />
        <div>
          <span> {props.creator.username}</span>
          <span>{props.location}</span>
        </div>
      </header>
      <img src={props.file} alt={props.caption} />
      <div>
        <PhotoActions
          number={props.like_count}
          isLiked={props.is_liked}
          photoId={props.id}
        />
        <PhotoComments
          caption={props.caption}
          creator={props.creator.username}
          comments={props.comments}
        />
        <TimeStamp time={props.created_at} />
        <CommentBox />
      </div>
    </div>
  );
};

FeedPhoto.propTypes = {
  creator: PropTypes.shape({
    profile_image: PropTypes.string,
    username: PropTypes.string.isRequired
  }).isRequired,
  location: PropTypes.string.isRequired,
  file: PropTypes.string.isRequired,
  like_count: PropTypes.number.isRequired,
  caption: PropTypes.string.isRequired,
  comments: PropTypes.arrayOf(
    PropTypes.shape({
      creator: PropTypes.shape({
        profile_image: PropTypes.string,
        username: PropTypes.string.isRequired
      }).isRequired,
      message: PropTypes.string.isRequired
    })
  ).isRequired,
  created_at: PropTypes.string.isRequired,
  is_liked: PropTypes.bool.isRequired
};

export default FeedPhoto;

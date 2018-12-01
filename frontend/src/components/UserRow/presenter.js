import React from "react";
import styles from "./styles.module.scss";
import PropTypes from "prop-types";

const UserRow = (props, context) => {
  return (
    <div className={styles.container}>
      <div className={styles.column}>
        <img
          src={props.user.profile_image || require("images/noPhoto.jpeg")}
          alt={props.user.user}
          className={props.big ? styles.bigAvatar : styles.avatar}
        />
        <div className={styles.user}>
          <span className={styles.username}>{props.user.username}</span>
          <span className={styles.name}>{props.user.name}</span>
        </div>
      </div>
      <span className={styles.column}>
        <button className={styles.button}> {context.t("Follow")}</button>
      </span>
    </div>
  );
};

UserRow.contextTypes = {
  t: PropTypes.func.isRequired
};

UserRow.propTypes = {
  user: PropTypes.shape({
    profile_image: PropTypes.string,
    username: PropTypes.string.isRequired,
    name: PropTypes.string
  }).isRequired,
  big: PropTypes.bool.isRequired
};

UserRow.defaultProps = {
  big: false 
};

export default UserRow;

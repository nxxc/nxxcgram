import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.module.scss";

const TimeStamp = (props, context) => props.time;
TimeStamp.propTypes = {
  time: PropTypes.string.isRequired
};
TimeStamp.contextTypes = {
  t: PropTypes.func.isRequired
};
export default TimeStamp;

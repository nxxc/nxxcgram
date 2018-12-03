import React, { Component } from "react";
import CommentBox from "./presenter";
import PropTypes from "prop-types";

class Container extends Component {
  state = {
    comment: ""
  };
  static propTypes = {
    photoId: PropTypes.number.isRequired,
    submitComment: PropTypes.func.isRequired
  };
  render() {
    return (
      <CommentBox
        handleInputChange={this._handleInputChange}
        handleKeyPress={this._handleKeyPress}
        {...this.state}
      />
    );
  }

  _handleInputChange = event => {
    const {
      target: { value }
    } = event;
    this.setState({
      comment: value
    });
  };
  _handleKeyPress = event => {
    const { submitComment } = this.props;
    const { comment } = this.state;
    const { key } = event;
    if (key === "Enter") {
      event.preventDefault();
      submitComment(comment);
      this.setState({
        comment: ""
      });
    }
  };
}

export default Container;
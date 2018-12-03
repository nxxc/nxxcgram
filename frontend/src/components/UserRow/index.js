import { connect } from "react-redux";
import Container from "./container";
import { actionCreators as UserActions } from "redux/modules/user";

const mapDispatchToProps = (dispatch, ownProps) => {
  const { user } = ownProps;
  return {
    handleClick: () => {
      if (user.following) {
        dispatch(UserActions.unfollowUser(user.id));
      } else {
        dispatch(UserActions.followUser(user.id));
      }
    }
  };
};

export default connect(
  null,
  mapDispatchToProps
)(Container);

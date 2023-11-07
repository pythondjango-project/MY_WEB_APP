import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

class UserForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      firstName: '',
      lastName: '',
      email: '',
      phoneNo: '',
      gender: 'None',
    
    };
  }

  handleChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  }

  handleSubmit = async (event) => {
    event.preventDefault();
    console.log(this.state);
   

  }

  render() {
    return (
      <div className="container d-flex justify-content-center align-items-center vh-100">
        <div className="form-container p-4 bg-light rounded">
          <h2 className="mb-4">NetServ Form</h2>
          <form onSubmit={this.handleSubmit}>
            <div className="mb-3">
              <label className="form-label label-text">Username</label>
              <input
                type="text"
                className="form-control"
                name="username"
                value={this.state.username}
                placeholder="Username"
                onChange={this.handleChange}
              />
            </div>
            <div className="mb-3">
              <label className="form-label label-text">First Name</label>
              <input
                type="text"
                className="form-control"
                name="firstName"
                value={this.state.firstName}
                placeholder="First Name"
                onChange={this.handleChange}
              />
            </div>
            <div className="mb-3">
              <label className="form-label label-text">Last Name</label>
              <input
                type="text"
                className="form-control"
                name="lastName"
                value={this.state.lastName}
                placeholder="Last Name"
                onChange={this.handleChange}
              />
            </div>
            <div className="mb-3">
              <label className="form-label label-text">Email</label>
              <input
                type="email"
                className="form-control"
                name="email"
                value={this.state.email}
                placeholder="Email"
                onChange={this.handleChange}
              />
            </div>
            <div className="mb-3">
              <label className="form-label label-text">PhoneNo</label>
              <input
                type="text"
                className="form-control"
                name="phoneNo"
                value={this.state.phoneNo}
                placeholder="PhoneNo"
                onChange={this.handleChange}
              />
            </div>
            <div className="mb-3">
              <label className="form-label label-text">Gender</label>
              <select
                className="form-select"
                name="gender"
                value={this.state.gender}
                onChange={this.handleChange}
              >
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
                <option value="None">None</option>
              </select>
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
          </form>

          {this.state.apiData && (
            <div className="mt-4">
              <h3>API Data:</h3>
              <pre>{JSON.stringify(this.state.apiData, null, 2)}</pre>
            </div>
          )}
          {this.state.error && (
            <div className="mt-4">
              <h3>Error:</h3>
              <p>{this.state.error}</p>
            </div>
          )}
        </div>
      </div>
    );
  }
}

export default UserForm;

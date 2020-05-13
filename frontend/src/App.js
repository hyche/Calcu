import React from 'react';
import axios from 'axios';
import { Container, Row, Col } from 'react-bootstrap';
import './App.css';

function FormulaRow(props) {
	return (
		<React.Fragment>
	        <input
	            style={{ width:'20%', marginLeft:'30%' }}
	            id='submit'
	            name='submit'
	            type='submit'
	            value={ props.formula }
	            onClick={ props.onSubmit }
	        >
	        </input>
	        <br></br>
       </React.Fragment>
	);
}

class App extends React.Component {
	constructor(props) {
		super(props)
    	this.state = {
    	    formula: '',
    	    result: '',
            message: '',
    	    formulas: []
    	};
	}

	onFieldChange = (e) => {
        const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value

        this.setState({
            [e.target.name]: value,
        });
    }

    onSubmit = (e, formula) => {
        const f = formula === undefined ? this.state.formula : formula
		axios.post(
			`${process.env.REACT_APP_API_DOMAIN}/calculate`,
			{formula: f}
		).then(response => {
			console.log('response', response)
			let clone_formulas = this.state.formulas.slice()
			this.setState({
				result: response.data['result'],
				message: response.data['message']
			})
			if (formula === undefined) {
				clone_formulas.push(f)
				this.setState({
					formulas: clone_formulas
				})
			}
		}).catch(error => {
			const data = error.response.data
			this.setState({
				result: data['result'],
				message: data['message']
			})
		});
    }

	render() {
		const formulaRows = this.state.formulas.map((formula, index) =>
			<FormulaRow key={index} onSubmit={(e) => this.onSubmit(e, formula)}
						formula={formula} />
		);
        return (
            <Container fluid>
	    		<Row>
                    Result: {this.state.result}, Message: {this.state.message}
                    <br></br>
                    <input
                       style={{ width:'20%' }}
                       id='formula'
                       name='formula'
                       type='text'
                       placeholder='Please input math formula.'
                       value={ this.state.formula }
                       onChange={ this.onFieldChange }
                    >
                    </input>
                    <br></br>
                    <input
                       style={{ width:'10%' }}
                       id='submit'
                       name='submit'
                       type='submit'
                       value='Submit'
                       onClick={ this.onSubmit }
                    >
                    </input>
                    <br></br>
					{formulaRows}
	    		</Row>
	    	</Container>
        );
    }
}

export default App;

import React, { useState } from 'react';
import { Button, TextField, Grid, Container } from '@mui/material';
// CUSTOM HOOKS
import useAxios from '../../hooks/axios/useAxios';
import Bar from '../../components/Bar';

const Login = ({ tryLogin, setTryLogin }) => {
    const { post, setJwtToken } = useAxios();
    const [username, setUserName] = useState();
    const [password, setPassword] = useState();

    const loginUser = async (credentials) => {

        let send_data = {
            "identifier": credentials.username,
            "password": credentials.password
        };
        const get_token = await post('/api/auth/local', send_data);
        setJwtToken(get_token.data)
        window.location.reload();

    }

    const capsFirst = (data) => {
        return data
    }

    const handleSubmit = async e => {
        e.preventDefault();
        try {
            await loginUser({
                username,
                password
            });
            setTryLogin(!tryLogin);
        }
        catch (e) {
            // window.location.reload();
        }
    }

    return (
        <Container style={{ paddingTop: "30vh" }} maxWidth="sm">
            <Container maxWidth="sm">
                <form style={{ textAlign: 'center' }} onSubmit={handleSubmit}>
                    <Grid container spacing={1}>
                        <Grid item xs={12}>
                            <TextField onChange={e => setUserName(e.target.value)} id="outlined-basic" label={capsFirst('login')} variant="outlined" />
                        </Grid>
                        <Grid item xs={12}>
                            <TextField type="password" onChange={e => setPassword(e.target.value)} id="outlined-basic" label={capsFirst('password')} variant="outlined" />
                        </Grid>
                        <Grid item xs={12}>
                            <Button color="primary" variant="outlined" type="submit">{capsFirst('login')}</Button>
                        </Grid>
                    </Grid>
                </form>
            </Container>
        </Container>

    )
}

export default Login

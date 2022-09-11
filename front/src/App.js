import React, { useState, useEffect, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

import Login from './pages/login/Login';
import useAxios from './hooks/axios/useAxios'
import Bar from './components/Bar';
import BasicPopup from './components/BasicPopup';

const MainPage = React.lazy(() => import('./pages/main/MainPage'));
const Charts = React.lazy(() => import('./pages/charts/Charts'));

export const ShowPopupContext = React.createContext();

function App() {

  const [confirmed, setConfirmed] = useState(null);
  const [tryLogin, setTryLogin] = useState(null);
  const [popup, setPopup] = useState({ open: false, content: false });
  const navigate = useNavigate();
  const { get } = useAxios();

  const updatePopup = ({ open, content }) => {
    setPopup({ open: open, content: content })
  }

  const popup_context = {
    popup: popup,
    updatePopup: updatePopup
  }


  useEffect(() => {
    if (!confirmed) {
      return navigate("/login");
    }
    else return navigate("/");
  }, [confirmed]);

  const verify = () =>{
    const verify_token = get('api/verify-token');
      verify_token.then((res) => {
        if (res?.data?.data?.attributes?.confirmed) setConfirmed(true);
      })
  }

  useEffect(() => {
    verify();
  },[])

  return (
    <>
      <ShowPopupContext.Provider value={popup_context} >
      <Suspense fallback={<div>Wczytywanie...</div>}>
        <Routes>
          <Route path="charts" element={<Charts />} />
          <Route path="login" element={<Login setTryLogin={setTryLogin} tryLogin={tryLogin} />} />
          <Route path="/" element={<MainPage />} />
        </Routes>
        <BasicPopup />
        </Suspense>
      </ShowPopupContext.Provider>
    </>


  );
}

export default React.memo(App);


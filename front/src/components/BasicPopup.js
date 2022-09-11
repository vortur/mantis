import React from 'react'
import { Dialog } from '@mui/material';
// CONTEXT
import { ShowPopupContext } from '../App'

/**
 * basic popup that is only a wrapper for its content
 * 
 */
const BasicPopup = () => {

  const { popup, updatePopup } = React.useContext(ShowPopupContext)

  const handleClose = () => {
    updatePopup({open:false, content:''});
  };
  
  return (
    <Dialog maxWidth={'md'} open={popup.open} onClose={handleClose}>
      {popup.content}
    </Dialog>
  )
}

export default BasicPopup

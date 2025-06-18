import React from 'react';
import { scanNetwork } from '../services/api';

const ScanButton = () => {
    const handleScan = async () => {
        try {
            const response = await scanNetwork();
            if (response.status === 200) {
                alert('Scansione completata con successo!');
                // Qui puoi gestire la risposta e aggiornare lo stato dell'app se necessario
            } else {
                alert('Errore durante la scansione della rete.');
            }
        } catch (error) {
            console.error('Errore:', error);
            alert('Si è verificato un errore durante la scansione della rete.');
        }
    };

    return (
        <button onClick={handleScan}>
            Scansiona Rete
        </button>
    );
};

export default ScanButton;
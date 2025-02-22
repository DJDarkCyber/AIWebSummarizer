import React, { useState } from 'react';
import axios from 'axios';
import { Container, Form, Button, Spinner, Card } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import { toast, ToastContainer, Bounce } from 'react-toastify';

import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'

import Header from "./header";

const Home = () => {
    document.title = "Web Summarized | Home";

    const [url, setUrl] = useState('');
    const [summarizedData, setSummarizedData] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSummarize = async () => {
        if (!url) {
            toast.error('Please enter a valid URL');
            return;
        }

        setIsLoading(true);

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/summarize/", {
                url: url,
            })
            if (response.data && response.data.summarized_data) {
                setSummarizedData(response.data.summarized_data);
            } else {
                toast.error('Unknown error occured');
            }
        } catch (err) {
            toast.error('An error occurred while summarizing the URL. Please try again.');
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    };

    
    return (
        <>
            <Header />
            <Container className="mt-5">

                <Container className="p-4 border rounded shadow-sm mb-4 bg-[#9e767698]">
                    <Form>
                    <Form.Group className="mb-3">
                        <Form.Control
                        type="text"
                        placeholder="Enter URL to summarize"
                        value={url}
                        onChange={(e) => setUrl(e.target.value)}
                        />
                    </Form.Group>

                    <div className="d-flex justify-content-center">
                        <Button
                        variant="primary"
                        onClick={handleSummarize}
                        disabled={isLoading}
                        style={{ backgroundColor: '#594545', borderColor: '#594545' }}
                        >
                        {isLoading ? (
                            <>
                            <Spinner
                                as="span"
                                animation="border"
                                size="sm"
                                role="status"
                                aria-hidden="true"
                            />
                            <span className="ms-2">Summarizing...</span>
                            </>
                        ) : (
                            'Summarize'
                        )}
                        </Button>
                    </div>
                    </Form>
                </Container>

                {summarizedData && (
                    <Container className="p-4 border rounded shadow-sm bg-[#9e767698]">
                    <Card className='border-0'>
                        <Card.Body className='bg-[#9e767698]'>
                        <Card.Title className='d-flex justify-content-center'>Summarized Content</Card.Title>
                        <div className="markdown-content">
                            <ReactMarkdown remarkPlugins={[remarkGfm]}>
                            {summarizedData}
                            </ReactMarkdown>
                        </div>
                        </Card.Body>
                    </Card>
                    </Container>
                )}
            </Container>

            <ToastContainer
                position="top-right"
                autoClose={5000}
                hideProgressBar={false}
                newestOnTop
                closeOnClick
                rtl={false}
                pauseOnFocusLoss
                draggable
                pauseOnHover
                theme="light"
                transition={Bounce}
            />

        </>
    )
}

export default Home;
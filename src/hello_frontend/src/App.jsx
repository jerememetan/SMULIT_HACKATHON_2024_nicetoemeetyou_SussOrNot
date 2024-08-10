import { useState } from 'react';
import { hello_backend } from 'declarations/hello_backend';

function App() {
  const [greeting, setGreeting] = useState('');
  const [linkGreeting, setLinkGreeting] = useState('');

  function handleImage(event) {
    event.preventDefault();
    const file = event.target.elements.file.files[0];
    const fileName = file ? file.name : '';

    // Generate a random number between 0 and 1
    const randomNumber = Math.random();

    // Check if the random number is greater than 0.5
    const isScam = randomNumber > 0.5;

    // Call the backend function with the file name
    hello_backend.greet(fileName).then((result) => {
      // Combine the random scam message with the backend result
      const greeting = `${result} ${isScam ? ' likely a scam! ' : ' not likely a scam!'}`;

      // Update the greeting state
      setGreeting(greeting);
    });

    return false;
  }

  function handleLink(event) {
    event.preventDefault();
    const link = event.target.elements.link.value;
  
    // Generate a random number between 0 and 1
    const randomNumber = Math.random();
  
    // Check if the random number is greater than 0.5
    const isScam = randomNumber > 0.5;
  
    // Call the backend function with the link
    hello_backend.greet(link).then((result) => {
      // Combine the random scam message with the backend result
      const linkGreeting = `${result} ${isScam ? 'likely a phishing website! ' : ' likely a legitimate website! '}`;
  
      // Update the linkGreeting state
      setLinkGreeting(linkGreeting);
    });
  
    return false;
  }

  return (
    <main className="container">
       <div>
        <h1 className="text-center">Scam or nah</h1>
        <h6 className="text-center">Input an image of a possible product Listing, and it will output a probability that it is likely a scam</h6>
        <form className="flex-column align-items-center" action="#" onSubmit={handleImage}>
          <label htmlFor="file">Enter image to check: &nbsp;</label>
          <input id="file" alt="file" type="file" accept="image/*" />
          <button type="submit" className="mt-2">Check Image</button>
        </form>
        <section id="greeting" className="mt-4">{greeting}</section>
      </div>

      <div>
        <h1 className="text-center">Phish or Nah</h1>
        <h6 className="text-center">Input an link, and it will check whether the website is a phishing website</h6>
        <form action="#" onSubmit={handleLink}>
          <label htmlFor="link">Enter link to check: &nbsp;</label>
          <input id="link" alt="link" type="text" />
          <button type="submit" className="mt-2">Check link</button>
        </form>
        <section id="greeting" className="mt-4">{linkGreeting}</section>
      </div>
    </main>
  );
}

export default App;

import { useState } from 'react';
import './App.css';
import axios from 'axios'
import load from './assests/load.gif'

function App() {
  const [model, setModel] = useState(null);
  const [imageType, setImageType] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);
  const [request, setRequest] = useState(null);
  const [insta, setIntsa] = useState(null);
  const [tweet, setTweet] = useState(null);

  const [loading, setLoading] = useState(false);

  const [url, setUrl] = useState(null);

  const submitHandler = () => {
    alert("foo")
  }
  const instaHandler = async () => {
    setLoading(true)
    axios
      .post("http://127.0.0.1:8000/insta", {
        username: insta
      })
      .then((response) => {
        console.log(response.data.img_url);
        setUrl(response.data.img_url);
        setLoading(false)
      });


  }
  const twitterHandler = () => {
    setLoading(true)
    axios
      .post("http://127.0.0.1:8000/tweet", {
        username: tweet
      })
      .then((response) => {
        console.log(response.data.img_url);
        setUrl(response.data.img_url);
        setLoading(false)
      });
  }

  return (
    <div className="App">
      <div className='mx-20'>
        <h2 className='heading text-3xl m-10'>API Testing</h2>
        {

          <div className='w-[40rem] mx-auto my-10'>
            <label for="countries" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Image Input type : </label>
            <select id="countries" value={imageType} onChange={(e) => setImageType(e.target.value)} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
              <option>Select a input</option>
              <option value="url">Image Url</option>
              <option value="instagram">Instagram Username</option>
              <option value="twitter">Twitter Username</option>
            </select>
          </div>
        }
        {

          imageType === "url" &&
          <>
            <div className='w-[40rem] mx-auto my-10'>

              <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Input: </label>
              <input type="text" id="default-input" placeholder='image url goes here' value={imageUrl} onChange={(e) => {
                setImageUrl(e.target.value)
                setUrl(e.target.value)
              }} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />

            </div>
            {url &&

              <div className='w-[40rem] mx-auto my-10 flex'>
                <img src={url} height={200} width={200} />
              </div>


            }

          </>

        }
        {

          imageType === "instagram" &&
          <>
            <div className='w-[40rem] mx-auto my-10 flex'>
              <div className='w-[35rem]'>
                <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Input: </label>
                <input type="text" id="default-input" placeholder='username of instagram' value={insta} onChange={(e) => setIntsa(e.target.value)} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
              </div>
              <button type="button" class=" text-blue-600 h-1 mt-5 p-5 font-medium rounded-lg text-sm mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" onClick={instaHandler}>verify</button>
            </div>
            {loading &&
              <div className='w-[40rem] mx-auto my-10 flex'>
                Loading ...
              </div>
            }
            {url &&

              <div className='w-[40rem] mx-auto my-10 flex'>
                <img src={url} height={200} width={200} />
              </div>


            }

          </>
        }
        {

          imageType === "twitter" &&
          <>
            <div className='w-[40rem] mx-auto my-10 flex'>
              <div className='w-[35rem]'>
                <label for="default-input" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Input: </label>
                <input type="text" id="default-input" placeholder='username of twitter' value={tweet} onChange={(e) => setTweet(e.target.value)} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" />
              </div>
              <button type="button" class=" text-blue-600 h-1 mt-5 p-5 font-medium rounded-lg text-sm mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" onClick={twitterHandler}>verify</button>
            </div>
            {loading &&
              <div className='w-[40rem] mx-auto my-10 flex'>
                Loading ...
              </div>

            }
            {url &&

              <div className='w-[40rem] mx-auto my-10 flex'>
                <img src={url} height={200} width={200} />
              </div>


            }
          </>
        }
        <div className='w-[40rem] mx-auto my-10'>
          <label for="countries" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select model:</label>
          <select id="countries" value={model} onChange={(e) => setModel(e.target.value)} class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
            <option>Select a model</option>
            <option value="/mp">Mediapipe</option>
            <option value="/cv">Cv</option>
            <option value="/haar">Haar Cascade</option>
          </select>
        </div>

        {
          <div className='w-[8rem] mx-auto mt-10 mb-5'>
            <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" onClick={submitHandler}>Get Results</button>
          </div>
        }
        {
          <div className='w-[15rem] mx-auto'>
            <span className="">_____________ or ____________</span>
          </div>
        }
        {
          <div className='border rounded-md border-gray-300 w-[40rem] mx-auto my-10'>
            <div className='flex justify-between'>
              <h1 className="text-lg m-4">Example Request</h1>
              <select name="request" id="request" value={request} onChange={(e) => setRequest(e.target.value)} className="p-2">
                <option value="/mp">Node.js</option>
                <option value="/cv">curl</option>
                <option value="/haar">Python</option>
              </select>
            </div>
            <div>
              <textarea id="message" rows="4" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Write your thoughts here..."></textarea>
            </div>
          </div>
        }
      </div>
    </div>
  );
}

export default App;

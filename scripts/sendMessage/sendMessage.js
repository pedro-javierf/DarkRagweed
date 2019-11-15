/*
    DarkRagweed - sendMessage script
    Copyright (C) 2019  pedro-javierf

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE
*/

//If the Gf object is present,we are running inside the Mobile app WebView
try
{
    //Obtain the oneclick token
    oneclick = Gf.data.Connect.CSRFToken;
    apiEndpoint=""; //fill with the new 2019 endpoint when they finish it
    
    //TODO
}
//Otherwise, the script is getting executed in a PC/Classic Browser
catch(e)
{
    //Obtain the oneclick token
    (document.getElementsByName('actionRequest')[0]===undefined?oneclick=document.getElementsByName('actionRequest')[1].value:oneclick=document.getElementsByName('actionRequest')[0].value)
    apiEndpoint='http://s39-es.ikariam.gameforge.com/index.php';
    
    //TODO
}

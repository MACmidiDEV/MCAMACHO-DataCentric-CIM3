const domain = 'meet.jit.si';
const options = {
	roomName: 'LittleLinksLearning',
	parentNode: document.querySelector('#meet')
};
const api = new JitsiMeetExternalAPI(domain, options);
